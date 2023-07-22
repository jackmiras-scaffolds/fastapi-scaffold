## Deployment

Before deploying the application don't forget to check the following:

- Step1: Environment variables
    - Make sure DB_LOG_LEVEL is set to INFO
    - Make sure APP_LOG_LEVEL is set to INFO

## Vessel
Vessel got written to expose short versions of commands that are used too often when debugging, developing code, or executing CI actions such as running linters, fix-linters, and tests.

For example, without vessel, the process of executing a alembic command inside the container to create a migration would be  something like `docker-compose exec -T app sh -c "cd /app && alembic revision -m create_foo_table"` with vessel, the same result can be achieved by executing `./vessel alembic revision -m create_foo_table`.

Another good example of vessel usage would be the up command, with `./vessel up` the docker-compose.yml and its containers will be built.

### Commands available in Vessel

| Command                       | Description                                                     |
| ----------------------------- |-----------------------------------------------------------------|
| ./vessel up                   | Initialize docker-compose stack                                 |
| ./vessel down                 | Stop docker-compose stack                                       |
| ./vessel build                | Build Docker image                                              |
| ./vessel bash                 | Access bash of the app container                                |
| ./vessel clean-all            | Prune all possible containers, volumes, and networks            |
| ./vessel python  <ANY_FLAG>   | Run any python command                                          |
| ./vessel pytest  <ANY_FLAG>   | Run any pytest command                                          |
| ./vessel alembic <ANY_FLAG>   | Run any alembic command                                         |
| ./vessel tests                | Run test suite with code coverageusing Pytest test framework    |
| ./vessel linters              | Run linters                                                     |
| ./vessel fix-linters          | Run linter fixer                                                |

## Database

### Database credentials:

The project uses SQLAlchemy ORM, it has this name because the "SQL" part refers to the fact that the library works with SQL databases, while the "Alchemy" part is a nod to the library's ability to transform data from one form to another, similar to the way that alchemists in history sought to transform base metals into gold.

So here's why the database configuration was set to the values you see at the `docker-compose.yml` file.

```bash
POSTGRES_USER=zosimos # Is the oldest alchemist humankind has records of
POSTGRES_DB=panopolis # He lived in Panopolis Egypt
POSTGRES_PASSWORD=alchemy # And practiced alchemy
```

### Connection:

For quick database queriyng and connection you can use [pgcli](https://www.pgcli.com/) to access the database from your terminal.

Follow the installation instructions according to your OS from [pgcli install](https://www.pgcli.com/install) and run the command down below.

```bash
pgcli -h localhost -p 5434 -U zosimos panopolis
```

For quick usage or inspection of the SQLite database present at the project you can use [litecli](https://litecli.com/).

Follow the installation instructions according to your OS [litecli install](https://litecli.com/install/) and run the command down below.

```bash
litecli -D database/database.sqlite
```

### Generating migrations

To achieve the goal of create a new database migration we have to use a secondary CLI tool called Alembic.

Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.

Run the command down bellow on your terminal to create a new migration:

```bash
alembic revision -m create_<revision_name>_table
```
