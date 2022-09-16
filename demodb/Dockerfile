FROM postgres:latest

# install packages
RUN apt-get update -y && \
    apt-get install -y wget && \
    apt-get install -y unzip

# download demo database
WORKDIR /demo
RUN wget -q https://edu.postgrespro.ru/demo-medium.zip && \
    unzip demo-medium.zip

# copy initialization script
COPY init-demo-db.sh /docker-entrypoint-initdb.d/

# workdir is root
WORKDIR /
