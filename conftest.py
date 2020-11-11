import pytest
import allure
import json
import requests
import time
import mysql.connector

from selenium import webdriver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# https://github.com/pytest-dev/pytest/issues/230#issuecomment-402580536
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


def url_data_exists(url, timeout=15):
    # Ожидание доступности ресурса по url
    with allure.step("Жду доступности ресура {}"):
        while timeout:
            response = requests.get(url)
            if response.ok:
                return True
            time.sleep(1)
            timeout -= 1
        return False


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://192.168.8.106", help="choose your browser")
    parser.addoption("--executor", "-E", action="store", default="192.168.8.106", help="grid host")
    parser.addoption("--local", action="store_true")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request, url, db_connection):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    local = request.config.getoption("--local")
    options = None

    if local:
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--ignore-certificate-errors")
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.accept_insecure_certs = True
            driver = webdriver.Firefox(options=options)
        else:
            raise NotImplementedError

        request.addfinalizer(driver.quit)
        driver.db = db_connection
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(url)
        return driver

    executor_url = f"http://{executor}:4444"

    capabilities = {
        "browserName": browser,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.accept_insecure_certs = True

    driver = webdriver.Remote(
        desired_capabilities=capabilities,
        command_executor=f"{executor_url}/wd/hub",
        options=options
    )

    def finalizer():
        video_url = f"{executor_url}/video/{driver.session_id}.mp4"
        driver.quit()

        if request.node.status == 'failed':

            if capabilities["selenoid:options"]["enableVideo"]:
                if url_data_exists(video_url):
                    allure.attach(
                        body=requests.get(video_url).content,
                        name="video_for_" + driver.session_id,
                        attachment_type=allure.attachment_type.MP4
                    )
            else:
                allure.attach(
                    name=driver.session_id,
                    body=driver.get_screenshot_as_png(),
                    attachment_type=allure.attachment_type.PNG
                )

        requests.delete(url=video_url)

    request.addfinalizer(finalizer)

    driver.implicitly_wait(3)
    driver.maximize_window()

    allure.attach(
        name=driver.session_id,
        body=json.dumps(str(driver.desired_capabilities)),
        attachment_type=allure.attachment_type.JSON
    )

    driver.get(url)
    driver.db = db_connection
    return driver


@pytest.fixture
def db_connection(request):
    db_host = request.config.getoption("--executor")
    connection = mysql.connector.connect(
        user='bn_opencart',
        password='',
        host=db_host,
        database='bitnami_opencart',
        port='3306'
    )
    request.addfinalizer(connection.close)
    return connection
