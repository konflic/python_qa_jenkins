FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -U pip && pip install -r requirements.txt

COPY . .

ENTRYPOINT ["pytest"]
