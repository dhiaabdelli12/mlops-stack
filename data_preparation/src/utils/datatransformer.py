import logging

class DataTransformer:
    def __init__(self, raw_data_df, logger=None):
        self.data = raw_data_df
        self.logger = logger or self._init_logger()
        self.transformations = []

    def _init_logger(self):
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        logger = logging.getLogger(__name__)
        return logger

    def _log(self, transformation, details=""):
        self.transformations.append(f"{transformation}: {details}")
        self.logger.info(details)

    def write_to_table(self, table_name, engine):
        try:
            self.data.to_sql(table_name, con=engine, if_exists='replace', index=False)
            self.logger.info(f"Data has been loaded into the PostgreSQL table {table_name} successfully.")
        except Exception as e:
            self.logger.error(f"Error loading data into the database: {e}")
            raise

    def drop_na(self):
        n_cols = self.data.shape[1]
        self.data = self.data.dropna()
        n_dropped_cols = n_cols - self.data.shape[1]
        self._log("drop_column", f"Dropped {n_dropped_cols} columns")
        return self

    def compute_x(self, new_col_name):
        self.data[new_col_name] = self.data["fAlpha"] / self.data["fAsym"]
        self._log("add_column", f"Added X column")
        return self
    
    def build(self):
        return self.data