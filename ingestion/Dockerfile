FROM python:3.12-slim
WORKDIR /app
RUN pip install poetry
ENV PATH="/root/.local/bin:$PATH"
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-interaction --no-ansi
COPY fetch_data.py .
CMD ["sleep", "infinity"]