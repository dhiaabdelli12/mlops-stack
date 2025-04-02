from utils.datatransformer import DataTransformer
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import yaml
import pandas as pd



with open("config.yml", "r") as file:
    config = yaml.safe_load(file) 


db_url = os.getenv("DATABASE_URL")
table_name = config["data_preparation"]["raw_data_table"]


engine = create_engine(db_url)


if __name__ == "__main__":
    load_dotenv()

    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM {table_name}"))
        raw_data_df = pd.DataFrame(result.fetchall(), columns=result.keys())


    data_transformer = DataTransformer(raw_data_df)

    processed_data = (
        data_transformer
        .drop_na()
        .compute_x(new_col_name="col_x")
        .write_to_table(table_name+"_processed", engine)
    ) 

    
