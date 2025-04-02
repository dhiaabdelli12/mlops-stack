FROM python:3.12-slim
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.in-project true
RUN poetry lock
RUN poetry install --with data_exploration --no-root
COPY data_exploration/src/ /app/src/

#CMD ["poetry" ,"run" ,"python", "src/init.py"] 

# RUN not used here because the env variables are only accessible at runtime and not during build time 