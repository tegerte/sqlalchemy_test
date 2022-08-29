> On basis of [SQLalchemy docs](https://docs.sqlalchemy.org/en/14/tutorial/index.html)

# Prep

1. Install docker and run postgres `docker pull postgres`
   , ` docker run --name my_postgres -p 5432:5432 -e POSTGRES_PASSWORD=mypassword -d postgres`  image
2. open console of postgres in Docker desktop
2. open psql as postgres: `psql -U postgres;`
3. create new database: `create database db_test;`
4. new user tegerte: `create user tegerte with password 'start1';`
5. grant usage to testuser tegerte: `grant all privileges on database "db_test" to tegerte;`