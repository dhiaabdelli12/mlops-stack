FROM python:3.12-slim
WORKDIR /app
RUN pip install poetry && poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install --with data_preparation --no-root
COPY data_preparation/src/ /app/src/
CMD ["sleep", "infinity"]
