FROM node:16-alpine


#Создали переменную для того, чтобы к ней обращаться
ARG PROJ_DIR=/FinancialAggregator/frontend
#


#Переходим в эту папку
WORKDIR ${PROJ_DIR}

RUN npm install -g npm

COPY package.json ${PROJ_DIR}
COPY package-lock.json ${PROJ_DIR}

RUN npm install



## Создадим папку и скопируем нашу директорию внутрь
RUN mkdir -p ${PROJ_DIR}
COPY . ${PROJ_DIR}
#for develop
CMD ["npm", "run", "serve"]

#for production


#RUN apk update
#RUN apk add nginx
#
#RUN npm run build
#RUN cp -R dist /var/www/
#
#COPY nginx.conf /etc/nginx/nginx.conf
##  Nginx останется «на переднем плане», так что Docker сможет правильно отслеживать процесс (в противном случае контейнер остановится сразу после запуска).
#ENTRYPOINT ["nginx", "-g", "daemon off;"]

#FROM nginx:1.21.6-alpine
#
#COPY ./dist /var/www
#COPY nginx.conf /etc/nginx/nginx.conf