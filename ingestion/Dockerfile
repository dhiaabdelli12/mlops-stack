FROM python:3.9
WORKDIR /app
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root
COPY fetch_data.py .

