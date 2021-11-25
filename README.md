# FastAPI Demo - Postgres

A simple project to show a couple examples of defining an API using [Tiangolo's FastAPI](https://fastapi.tiangolo.com/)
that connects to a PostgreSQL DB using  [Tiangolo's SQLModel](https://sqlmodel.tiangolo.com/).

## About this demo data

I just got a CSV file that contains a list of all sports facilities in Andalusia, hosted in
[Junta de Andalcía's Open Data portal](https://www.juntadeandalucia.es/datosabiertos/portal.html). Current file was
updated on 1st of July 2021. You can check it out if there is any update
[here](https://www.juntadeandalucia.es/datosabiertos/portal/dataset/censo-de-instalaciones-deportivas).

## Required environment variables

Only the parameters needed to reach our PostgreSQL database:

| Variable    | Description                     | Example         |
|-------------|---------------------------------|-----------------|
| `PG_USER`   | PostgresSQL DB Username         | `postgres`      |
| `PG_PASS`   | PostgresSQL DB Password         | `postgres`      |
| `PG_HOST`   | PostgresSQL DB Host URL or DNS  | `localhost`     |
| `PG_PORT`   | PostgresSQL DB Port             | `5432`          |
| `PG_DB`     | PostgresSQL DB Name             | `fast-api-demo` |

## Running with docker-compose (PostgreSQL + API)

You have a [docker-compose](docker-compose.yaml) file for testing this API.

```shell
docker-compose up
```

Note if it's the first time you run the DB, you will need to create and populate the `sports_facilities` table. You can
copy both files under [data](data) folder to, for example to `tmp` folder, inside your postgresql container and, after
that, load the data. Here you have some useful commands for doing that:

```shell
docker cp data/sports_facilities.sql fast-api-demo_postgres_1:/tmp
docker cp data/sports_facilities_census.csv fast-api-demo_postgres_1:/tmp
docker exec -it fast-api-demo_postgres_1  psql -U postgres -d fast-api-demo -f /tmp/sports_facilities.sql
```

## Running in docker (only API)

```shell
# Building local image
docker build -t fast-api-demo .

# We are asuming we have a postgresql running in localhost, change this to reach your instance
docker run --rm \
-p 5000:5000 \
-e PG_USER=postgres \
-e PG_PASS=postgres \
-e PG_HOST=localhost \
-e PG_PORT=5432 \
-e PG_DB=fast-api-demo \
--entrypoint /usr/src/app/docker-entrypoint.sh \
fast-api-demo
```

## API Doc

If you want to see this API documentation, you can take a look by accessing to your API endpoint and querying
to `/docs` (http://localhost:5000/docs if you're running it locally, for example).

## Running tests

We do use `Pytest` for running unit tests in this project. Note you need to install
[requirements_dev](requirements_dev.txt) before. It is as easy as running this couple commands (from the root folder of
this project):

```bash
# Running test
python -m pytest
# Check test coverage
python -m pytest --cov=.
```
