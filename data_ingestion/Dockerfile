FROM python:3.12-slim
WORKDIR /app
RUN pip install poetry && poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install --with data_ingestion --no-root
COPY data_ingestion/src/ /app/src/
RUN poetry run pytest
CMD ["poetry", "run", "python", "src/main.py"]
