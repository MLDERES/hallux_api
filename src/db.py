from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship
from dotenv import load_dotenv
from os import getenv
from .model import Album, Band, Person

# This library allows the environment variables to be loaded from a file
load_dotenv()

# To get this working quickly, you can just replace these variables with your own values
svr = getenv("MSSQL_SERVER")
uid = getenv("HALLUX_USER")
pwd = getenv("HALLUX_PASSWORD")
db = getenv("HALLUX_DB")

# Setup the database connection
engine = create_engine(f"mssql+pyodbc://{uid}:{pwd}@{svr}/{db}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes", fast_executemany=True)
# Create the database tables
SQLModel.metadata.create_all(engine)


# Get a list of bands using partial name match or if not supplied, all bands
def get_bands(name: str = '', offset: int = 0, limit: int = 100):
    with Session(engine) as session:
        statement = select(Band).order_by(Band.id).where(Band.name.startswith(name)).offset(offset).limit(limit)
        results = session.exec(statement)
        return results.all() if results else None

# Get a band by id
def get_band_by_id(id: int) -> Band:
    with Session(engine) as session:
        statement = select(Band).where(Band.id==id)
        results = session.exec(statement)
        return results.first() if results else None
    
# Get persons by first_name, last_name, or both
def get_persons(first_name: str = '', last_name: str = '', offset: int = 0, limit: int = 100):
    with Session(engine) as session:
        fname_filter = Person.first_name.startswith(first_name)
        lname_filter = Person.last_name.startswith(last_name)
        statement = select(Person).order_by(Person.id).where(fname_filter).where(lname_filter).offset(offset).limit(limit)
        results = session.exec(statement)
        return results.all() if results else None

# Look up a person with a given id
def get_person_by_id(id: int) -> Person:
    with Session(engine) as session:
        statement = select(Person).where(Person.id==id)
        results = session.exec(statement)
        return results.first() if results else None
    
# Get a list of albums using partial name match or if not supplied, all albums
def get_albums(name: str = '', offset: int = 0, limit: int = 100):
    with Session(engine) as session:
        statement = select(Album).order_by(Album.id).where(Album.name.startswith(name)).offset(offset).limit(limit)
        results = session.exec(statement)
        return results.all() if results else None

# Get an album by id
def get_album_by_id(id: int) -> Album:
    with Session(engine) as session:
        statement = select(Album).where(Album.id==id)
        results = session.exec(statement)
        return results.first() if results else None
    