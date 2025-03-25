import pandas as pd
from ucimlrepo import fetch_ucirepo
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()


logger.info("Fetching dataset from UCI Repository...")
data = fetch_ucirepo(id=159) 
X = data.data.features
y = data.data.targets

logger.info("Combining features and target data into a single DataFrame...")
combined_df = pd.concat([X, y], axis = 1)

db_url = os.getenv('DATABASE_URL')

if not db_url:
    logger.error("POSTGRES_DB environment variable is not set.")
    raise ValueError("POSTGRES_DB environment variable is missing.")

logger.info("Creating a connection to the PostgreSQL database...")
try:
    engine = create_engine(db_url)
    logger.info("Database connection established.")
except Exception as e:
    logger.error(f"Error connecting to the database: {e}")
    raise


logger.info("Loading data into the PostgreSQL table...")
try:
    combined_df.to_sql('magic_gamma_telescope', con=engine, if_exists='replace', index=False)
    logger.info("Data has been loaded into the PostgreSQL table successfully.")
except Exception as e:
    logger.error(f"Error loading data into the database: {e}")
    raise