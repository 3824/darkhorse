#!/bin/sh

# docker pull mysql

# docker run -it --name darkhorse-mysql -e MYSQL_ROOT_PASSWORD=password -d mysql:latest
docker-compose exec db bash -c "chmod 0775 docker-entrypoint-initdb.d/init-database.sh"
docker-compose exec db bash -c "./docker-entrypoint-initdb.d/init-database.sh"

