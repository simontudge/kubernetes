FROM postgres:13

RUN mkdir /data
COPY data.csv /data/murders.csv

#COPY 01_setup.sh /docker-entrypoint-initdb.d
COPY 02_make_tables.sh /docker-entrypoint-initdb.d
COPY 03_ingest.sh /docker-entrypoint-initdb.d
