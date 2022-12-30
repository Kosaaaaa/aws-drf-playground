FROM python:3.11.0-alpine

ENV PYTHONUNBUFFERED 1

ARG DEV=false
ARG PORT=8000

COPY ./requirements.txt /tmp/requirements.txt
COPY ./src/app /app
WORKDIR /app
EXPOSE $PORT


# create python virtualenv, upgrade pip, install required linux and python packages
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
      build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt

# clean tmp resoursces
RUN rm -rf /tmp && \
    apk del .tmp-build-deps

# create user and create static directory with privilages - django-user : read, write, execute
RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol

ENV PATH="/py/bin:$PATH"

USER django-user
