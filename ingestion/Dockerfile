FROM python:3.12-slim
WORKDIR /app
RUN pip install poetry
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH=/app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root 
COPY . .
RUN poetry run pytest

CMD ["poetry", "run", "python", "main.py"]