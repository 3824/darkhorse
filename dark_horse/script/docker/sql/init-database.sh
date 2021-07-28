#!/usr/bin/env bash
#wait for the MySQL Server to come up
#sleep 30s

#run the setup script to create the DB and the schema in the DB
#mysql -u horse -phorse dark_horse < "/docker-entrypoint-initdb.d/001-create-tables.sql"
mysql -u root -proot dark_horse < "/docker-entrypoint-initdb.d/001-create-tables.sql"