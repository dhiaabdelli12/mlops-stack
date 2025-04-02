# General Overview



# Dependencies


For dependency management, poetry is used. At the root directory the pyproject.toml, the shared dependencies accross services are defined under main and additional dependencies for each specific service are defined under groups where each group corresponds to a service. 

Each services reads from that file without having to init a new poetry project. This means that dependencies are managed on the host machine by updating the pyproject.toml file.

To add a package to a specific service, you can run the following command (either on the host machine or from within a running container)

```SHELL
poetry add <package> --group <service_name>
```


# Setup

For this project, you only need [Docker](https://www.docker.com/) and [poetry](https://python-poetry.org/) installed on the host machine.

After installing both docker and poetry, make sure the docker daemon is running.

Then you need to make sure that the virtual environment is created within the project directory. For that you can run this command:

```SHELL
poetry config virtualenvs.in-project true
```


Then create the lock file and install the dependencies: 

```SHELL
poetry lock
poetry install
```

Make sure now that you have `.venv/` directory in the the root of your project. 


Then you need to build the docker images and then start the containers:

```SHELL
docker-compose build
docker-compose up -d
```


# Services
## Datastore
## ingestion
## Data Exploration
## Data Preparation