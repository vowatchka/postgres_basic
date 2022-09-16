#!/usr/bin/env bash
psql -aq -f /demo/demo-medium-20170815.sql --username "$POSTGRES_USER" --dbname "$POSTGRES_DB"
