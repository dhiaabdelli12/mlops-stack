FROM python:3.12-slim
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.in-project true
RUN poetry lock
RUN poetry install --with data_preparation --no-root
COPY data_preparation/src/ /app/src/
CMD ["sleep", "infinity"]
