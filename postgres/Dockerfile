FROM postgres:latest

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD gtadmin
ENV POSTGRES_DB gestao_materiais

COPY ./postgres/init.sql /docker-entrypoint-initdb.d/

