import os
from utils.data import *
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    db_url = os.getenv("DATABASE_URL")
    print(db_url)
    load_data(table_name="magic_gamma_telescope", db_url=db_url)
