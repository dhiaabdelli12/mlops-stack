from sqlalchemy import create_engine
from utils.dataloader import DataLoader

if __name__ == "__main__":
    data_loader = DataLoader()
    data = data_loader.fetch_dataset()
    combined_df = data_loader.combine_features_target(data)
    engine = create_engine(data_loader.db_url)
    data_loader.write_to_table(combined_df, "magic_gamma_telescope", engine)
