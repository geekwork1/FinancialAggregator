#Берем образ из докера https://hub.docker.com/_/python за основу
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


#Создали переменную для того, чтобы к ней обращаться
ARG PROJ=/FinancialAggregator
ARG PROJ_DIR=/FinancialAggregator/backend



#ENV VIRTUAL_ENV /env
#ENV PATH /env/bin:$PATH



RUN apt-get update\
    && apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev gunicorn3

#сделаем отдельным слоем, чтобы был кеш и при последующей загрузке 
#при отсутствии изменений заново не грузить
ADD ./requirements.txt requirements.txt

#Обновим Pip и установим зависимости для проекта
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN pip3 install gunicorn




# Создадим папку и скопируем нашу директорию внутрь
RUN mkdir -p ${PROJ}
COPY . ${PROJ}

#Переходим в папку проекта
WORKDIR ${PROJ_DIR}

#RUN pip3 install gunicorn
# Скопируем файл entry.sh и запустим его
COPY entry.sh /entry.sh
RUN chmod +x /entry.sh
ENTRYPOINT ["/entry.sh"]
