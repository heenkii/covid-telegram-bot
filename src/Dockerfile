FROM python:3.13-alpine AS builder
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

FROM python:3.13-alpine
WORKDIR /usr/src/app
COPY --from=builder /usr/src/app /usr/src/app
COPY . .
ENTRYPOINT ["python3", "bot.py"]
