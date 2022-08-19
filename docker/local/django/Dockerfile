FROM python:3.10.0-slim-buster

ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME


LABEL maintainer='api.imperfect@gmail.com'
LABEL decription="Development image for Calendar_App"

# prevent python to write pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
# python output transmit to terminal without being buffered and allowed the application to display live.
ENV PYTHONUNBUFFERED 1

# -y is for say yes to user promt
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev \
    && apt-get install -y gettext \
    && apt-get -y install netcat gcc postgresql \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

# we use entrypoint and start shell script to be sure the database is up can be used.
COPY ./docker/local/django/entrypoint /entrypoint
# convert any windows line ending to unix line endings
RUN sed -i 's/\r$//g' /entrypoint
# make entrypoint shell script executable
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start


#COPY ./docker/local/django/celery/worker/start /start-celeryworker
#RUN sed -i 's/\r$//g' /start-celeryworker
#RUN chmod +x /start-celeryworker

#COPY ./docker/local/django/celery/flower/start /start-flower
#RUN sed -i 's/\r$//g' /start-flower
#RUN chmod +x /start-flower


ENTRYPOINT [ "/entrypoint"]
