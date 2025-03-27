FROM python:3.12-slim
WORKDIR /app
COPY . ./
RUN pip install poetry && poetry install --no-root --no-interaction --no-ansi
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH=/app

CMD ["poetry" ,"run" ,"python", "init.py"] 
# RUN not used here because the env variables are only accessible at runtime and not during build time 