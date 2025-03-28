# General Overview



# Dependencies

TBD: add base dockerfile 

For dependency management, poetry is used. At the root directory the pyproject.toml, the shared dependencies accross services are defined under main and additional dependencies for each specific service are defined under groups where each group corresponds to a service. 

Each services reads from that file without having to init a new poetry project. This means that dependencies are managed on the host machine by updating the pyproject.toml file.

To add a package to a specific service, you can run the following command:

```SHELL
poetry add <package> --group <service_name>
```

You then need to rebuild the image again, before running the container
```SHELL
docker-compose build <service>
docker-compose up <service>
```
TBD: this is not efficient and needs to be changed. It doesn't make sense to re-build the image, everytime a new dependency is added.


# Setup

Start by building the base docker file:

```SHELL
docker build -it mlops-stack-base -f Dockerfile.base .
```

This will create the base docker file that will be used by all the services in this project. This base image:
- Installs poetry
- Installs the shared dependencies using poetry
- Copies the .toml and .lock files to the container
- Setups up environment variables

Next, you can build all the services in the project using the following command:

```SHELL
docker-compose build
```

# Services
## Datastore
## ingestion
## Data Exploration
## Data Preparation