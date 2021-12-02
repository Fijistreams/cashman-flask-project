FROM python:3.8.10

RUN apt-get update

RUN pip install --no-cache-dir pipenv


WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock bootstrap.sh ./
COPY cashman ./cashman


RUN pipenv install --system --deploy


EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]
