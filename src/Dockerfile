FROM python:3.11.4-alpine
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /usr/src/app/

ENTRYPOINT ["python3", "bot.py"]
