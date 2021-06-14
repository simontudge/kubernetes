#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    
COPY mapper.murders
FROM '/data/murders.csv'
DELIMITER ','
CSV HEADER;

EOSQL

