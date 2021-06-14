#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    
    CREATE SCHEMA mapper;

    CREATE TABLE mapper.murders (
    name varchar,
    size double precision,
    lat double precision,
    long double precision,
    color INTEGER
    );
EOSQL

