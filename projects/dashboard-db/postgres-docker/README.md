A custom setup of postgres. The only thing it adds is to initialise the database with a table and some data already in it. To run this you should
run

```BASH
docker run --name custom-postgres -e POSTGRES_PASSWORD=password1234 -e POSTGRES_DB=mapper -e POSTGRES_USER=mapper postgres-map
```