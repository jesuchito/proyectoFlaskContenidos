FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
COPY requeriments_sqlalchemy.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir -r requeriments_sqlalchemy.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "openapi_server"]