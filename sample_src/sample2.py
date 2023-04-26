
from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship, ForeignKeyConstraint
from dotenv import load_dotenv
from os import getenv
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Table, create_engine


load_dotenv()

# To get this working quickly, you can just replace these variables with your own values
svr = getenv("MSSQL_SERVER")
uid = getenv("HALLUX_USER")
pwd = getenv("HALLUX_PASSWORD")
db = getenv("HALLUX_DB")

Base = declarative_base()

# band_genre = Table("band_genre",
#                    Base.metadata,
#                    Column('genre_id', ForeignKey("Genre.genre_id"), primary_key=True),
#                    Column('band_id', ForeignKey("Band.band_id"), primary_key=True))

class Band_Genre(SQLModel, table=True):
    genre_id: Optional[int] = Field(default=None, foreign_key="genre.genre_id", primary_key=True)
    band_id: Optional[int] = Field(default=None, foreign_key="band.band_id", primary_key=True)

    genre: "Genre" = Relationship(back_populates='band_links')
    band: "Band" = Relationship(back_populates='genre_links')
    # ForeignKeyConstraint(['band_id','genre_id'],['band.band_id','genre.genre_id'])

class Genre(SQLModel, table=True):
    genre_id: int = Field(
        default=None,
        primary_key=True,
        description="Genre ID",
        sa_column_kwargs={"name": "Genre_Id"},
    )
    name: Optional[str] = Field(
        default=None,
        description="Name of the genre",
        sa_column_kwargs={"name": "Genre"},
    )
    # bands: List[Band] = Relationship(sa_relationship_kwargs=dict(secondary="band_genre", back_populates='genre'))
    band_links: List[Band_Genre] = Relationship(back_populates='genre')

    def __str__(self):
        return f"{self.genre_id}: {self.genre}"
    
class Band(SQLModel, table=True):
    band_id: Optional[int] = Field(
        default=None,
        primary_key=True,
        description="Band ID",
        sa_column_kwargs={"name": "Band_id"},
    )
    band_name: Optional[str] = Field(
        default=None,
        description="Name of the band",
        sa_column_kwargs={"name": "Band_Name"},
    )
    #genres: List[Band] = Relationship(sa_relationship_kwargs=dict(secondary="band_genre", back_populates='bands'))
    genre_links: List[Band_Genre] = Relationship(back_populates='band')
    
    def __str__(self):
        return f"{self.band_id}: {self.band_name}"
 

engine = create_engine(
    f"mssql+pyodbc://{uid}:{pwd}@{svr}/{db}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes",
    # fast_executemany=True,
)

Session = sessionmaker(bind=engine)

session = Session()
statement = select(Band)
results = session.execute(statement)

for r in results.all():
    for g in r.genres:
        print(g)