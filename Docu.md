> On basis of [SQLalchemy docs](https://docs.sqlalchemy.org/en/14/orm/tutorial.html#building-a-relationship)

# Prep

1. Install docker and run postgres `docker pull postgres`
   , ` docker run --name my_postgres -p 5432:5432 -e POSTGRES_PASSWORD=mypassword -d postgres`  image
2. open console of postgres in Docker desktop
2. open psql as postgres: `psql -U postgres;`
3. create new database: `create database db_test;`
4. new user tegerte: `create user tegerte with password '****';`
5. grant usage to testuser tegerte: `grant all privileges on database "db_test" to tegerte;`
6. to maintain the database using PGAdmin4 start docker container: `docker run --name "pg_admin" -p 5050:80 -e "PGADMIN_DEFAULT_EMAIL=myemail@gmail.com" -e "PGADMIN_DEFAULT_PASSWORD=a12345678" -d  dpage/pgadmin4`
7.  [logIn on PGAdmin-webUI](http://localhost:5050/login?next=%2F)
8. if running two containerized connection partners (postgres-db and PGAdmin) the connction string for PGadmin must have `host.docker.internal` as hostname, Port is the common 5432
   `