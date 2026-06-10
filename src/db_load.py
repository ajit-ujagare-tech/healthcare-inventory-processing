import pandas as pd
import configparser
from sqlalchemy import create_engine

config = configparser.ConfigParser()
config.read("config/config.ini")

host = config["DATABASE"]["HOST"]
database = config["DATABASE"]["DATABASE"]
user = config["DATABASE"]["USER"]
password = config["DATABASE"]["PASSWORD"]

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{database}"
)

df = pd.read_csv("data/output.csv")

df.to_sql(
    name="inventory",
    con=engine,
    if_exists="append",
    index=False
)

print("Data Loaded Successfully")
