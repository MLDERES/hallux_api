from types import UnionType
from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship
from dotenv import load_dotenv
from os import getenv
from .model import Album, Band, Person, Song, SongReadWithAlbum

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

def get_session():
    with Session(engine) as session:
        yield session

# Get a list of bands using partial name match or if not supplied, all bands
def get_bands(session: Session, name: str = '', offset: int = 0, limit: int = 100):
    statement = select(Band).order_by(Band.id).where(Band.name.startswith(name)).offset(offset).limit(limit)
    results = session.exec(statement)
    return results.all() if results else None

# Get a band by id
def get_band_by_id(session:Session, id: int) -> Band:
    results = session.exec(select(Band).where(Band.id==id))
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
        results = session.exec(select(Person).where(Person.id==id))
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
    
# Get a list of songs for an album
def get_songs(session, name: str = '', offset: int = 0, limit: int = 100) :
        statement = select(Song).order_by(Song.album_id, Song.sequence).where(Song.name.startswith(name)).offset(offset).limit(limit)
        results = session.exec(statement)
        return results.all() if results else None

# Get a specific song by id
def get_song_by_id(session, song_id: int) -> SongReadWithAlbum:
        statement = select(Song).where(Song.id ==song_id)
        results = session.exec(statement)
        return results.first() if results else None
    

    