from dotenv import load_dotenv
from os import getenv
from sqlmodel import Session, SQLModel, create_engine, select
from src.model import Band, Person
# This library allows the environment variables to be loaded from a file
load_dotenv()

# To get this working quickly, you can just replace these variables with your own values
svr = getenv("MSSQL_SERVER")
uid = getenv("HALLUX_USER")
pwd = getenv("HALLUX_PASSWORD")
db = getenv("HALLUX_DB")


engine = create_engine(f"mssql+pyodbc://{uid}:{pwd}@{svr}/{db}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes", fast_executemany=True)
# Create the database tables
SQLModel.metadata.create_all(engine)