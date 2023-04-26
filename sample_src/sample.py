from sqlalchemy import Column, ForeignKey, Integer, Table, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from dotenv import load_dotenv
from os import getenv

# This library allows the environment variables to be loaded from a file
load_dotenv()

# To get this working quickly, you can just replace these variables with your own values
svr = getenv("MSSQL_SERVER")
uid = getenv("HALLUX_USER")
pwd = getenv("HALLUX_PASSWORD")
db = getenv("HALLUX_DB")

# Setup the database connection

Base = declarative_base()

band_genre = Table("band_genre",
                   Base.metadata,
                   Column('genre_id', ForeignKey("Genre.genre_id"), primary_key=True),
                   Column('band_id', ForeignKey("Band.band_id"), primary_key=True))

class Band(Base):
    __tablename__ = "Band"
    band_id = Column(Integer,primary_key=True)

    band_name = Column(String)
    genres = relationship("Genre", secondary=band_genre, back_populates='bands')

class Genre(Base):
    __tablename__ = "Genre"
    genre_id = Column(Integer, primary_key=True)
    genre = Column(String)

    bands = relationship("Band", secondary="band_genre", back_populates='genres')
    

    def __repl__(self):
        return f"{self.genre_id}: {self.genre}"
    
    def __str__(self):
        return f"{self.genre_id}: {self.genre}"

engine = create_engine(
    f"mssql+pyodbc://{uid}:{pwd}@{svr}/{db}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes",
    fast_executemany=True,
)

Session = sessionmaker(bind=engine)

session = Session()
for r in session.query(Band):
    for g in r.genres:
        print(g)
