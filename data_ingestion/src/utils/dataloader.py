import os
import logging
import pandas as pd
from ucimlrepo import fetch_ucirepo
from dotenv import load_dotenv


class DataLoader:
    def __init__(self, db_url=None, dataset_id=159, logger=None):
        self.db_url = db_url or self.get_db_url()
        self.dataset_id = dataset_id
        self.logger = logger or self._init_logger()

    def _init_logger(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(__name__)
        return logger

    def get_db_url(self):
        load_dotenv()
        db_url = os.getenv('DATABASE_URL')
        if not db_url:
            self.logger.error("DATABASE_URL environment variable is not set.")
            raise ValueError("DATABASE_URL environment variable is missing.")
        return db_url

    def fetch_dataset(self):
        self.logger.info("Fetching dataset from UCI Repository...")
        data = fetch_ucirepo(id=self.dataset_id)
        return data

    def combine_features_target(self, data):
        X = data.data.features
        y = data.data.targets
        self.logger.info("Combining features and target data into a single DataFrame...")
        combined_df = pd.concat([X, y], axis=1)
        return combined_df

    def write_to_table(self, data, table_name, engine):
        try:
            data.to_sql(table_name, con=engine, if_exists='replace', index=False)
            self.logger.info(f"Data has been loaded into the PostgreSQL table {table_name} successfully.")
        except Exception as e:
            self.logger.error(f"Error loading data into the database: {e}")
            raise



