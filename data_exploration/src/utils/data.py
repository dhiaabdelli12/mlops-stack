import pandas as pd
from sqlalchemy import create_engine, text
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


def load_data(table_name, db_url):
    DATA_PATH = os.path.join(
        "/", "data", "cached_data.parquet"
    )  # caching under /data because don't want it persisted in host machine since I'm only mounting app/
    if os.path.exists(DATA_PATH):
        logger.info("Loading from parquet file...")
        return pd.read_parquet(DATA_PATH)


    if db_url is None:
        raise ValueError("DATABASE_URL is not set correctly.")

    engine = create_engine(db_url)

    logger.info("Fetching data from postgres database...")
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM {table_name}"))
        data = pd.DataFrame(result.fetchall(), columns=result.keys())

    logger.info("Caching data in parquet file...")
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    data.to_parquet(DATA_PATH, index=False)

    return data
