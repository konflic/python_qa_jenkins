import random
import string
import socket
import allure

def random_string(lenght=10):
    return "".join([random.choice(string.ascii_letters) for _ in range(lenght)])


def random_phone():
    return "".join([random.choice(string.digits) for _ in range(10)])


def random_email():
    return random_string() + "@" + random_string(5) + "." + random.choice(["com", "ua", "org", "ru"])


@allure.step("Creating a user with random email in database")
def create_random_user(connection):
    """This user will have password test"""
    query = 'INSERT INTO oc_customer (customer_group_id, language_id, firstname, lastname, email, telephone, fax, password, salt, custom_field, ip, status, safe, token, code, date_added) VALUES (1, 1, %s, %s, %s, %s, "", %s, %s, "", %s, 1, 0, "", "", NOW())'
    email = random_email()
    test_password = "49dcc5aacf9491668e729c0c46bc815988f641e4" # equals to password "test"
    salt = "VGNUpQvgV"
    ip = socket.gethostbyname(socket.gethostname())
    connection.cursor().execute(query, (random_string(), random_string(), email, random_phone(), test_password, salt, ip))
    connection.commit()
    allure.attach(name=email, body=email)
    return email
