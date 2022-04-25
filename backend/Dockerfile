#Берем образ из докера https://hub.docker.com/_/python за основу
FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


#Создали переменную для того, чтобы к ней обращаться
ARG PROJ_DIR=/financialaggregator

# Создадим папку и скопируем нашу директорию внутрь
RUN mkdir -p ${PROJ_DIR}
COPY . ${PROJ_DIR}

#Переходим в эту папку
WORKDIR ${PROJ_DIR}

# Install dependencies required for psycopg2 python package
RUN apk update && apk add libpq
RUN apk update && apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

#Обновим Pip и установим зависимости для проекта
RUN pip install -U pip \
     pip install -r requirements.txt

# Скопируем файл entry.sh и запустим его
COPY entry.sh /entry.sh
RUN chmod +x /entry.sh
ENTRYPOINT ["/entry.sh"]