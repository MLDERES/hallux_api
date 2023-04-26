
from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship
from dotenv import load_dotenv
from os import getenv
from sqlmodel import SQLModel

load_dotenv()

# To get this working quickly, you can just replace these variables with your own values
svr = getenv("MSSQL_SERVER")
uid = getenv("HALLUX_USER")
pwd = getenv("HALLUX_PASSWORD")
db = getenv("HALLUX_DB")


# Create a class called Genre which inherits from SQLModel
class Genre(SQLModel, table=True):
    # Specify a map to all the fields in the database table called Genre
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
    bands: List["Band"] = Relationship(sa_relationship_kwargs=dict(secondary="Band_Genre", back_populates='genres'))

    def __str__(self):
        return f"{self.genre_id}: {self.genre}"
    
# There is never a reason to inherit from TABLE models
class Band(SQLModel, table=True):
    # Specify a map to all the fields in the database table called Band
    band_id: Optional[int] = Field(
        default=None,
        primary_key=True,
        description="Band ID",
        sa_column_kwargs={"name": "Band_id"},
    )

    status_code: Optional[str] = Field(
        default=None,
        description="Band Status Code",
        sa_column_kwargs={"name": "Band_Status_Code"},
    )
    band_name: Optional[str] = Field(
        default=None,
        description="Name of the band",
        sa_column_kwargs={"name": "Band_Name"},
    )
    formation_date: Optional[datetime] = Field(
        default=None, description="Date the band was formed"
    )
    # The foreign key here must match the sa_column name
    primary_contact_id: Optional[int] = Field(
        default=None,
        description="ID of the primary contact for the band",
        foreign_key="person.Person_Id",
    )
    # Create a relationship to the Person class
    # Relationships can ONLY be defined in the table models
    genres: List["Genre"] = Relationship(sa_relationship_kwargs=dict(secondary="Band_Genre",back_populates="bands"))
    
    def __str__(self):
        return f"{self.band_id}: {self.band_name}"
    
class Band_Genre(SQLModel):
    __tablename__ = 'Band_Genre'
    genre_id: Optional[int] = Field(default=None, foreign_key="Genre.genre_id", primary_key=True)
    band_id: Optional[int] = Field(default=None, foreign_key="Band.band_id", primary_key=True)

    # Get a list of bands using partial name match or if not supplied, all bands
def get_bands(session: Session, name: str = "", offset: int = 0, limit: int = 100):
    statement = (
        select(Band)
        .order_by(Band.band_id)
        .where(Band.band_name.startswith(name))
        .offset(offset)
        .limit(limit)
    )
    results = session.exec(statement)
    return results.all() if results else None

@app.get("/bands", response_model=List[BandRead])
def read_band(
    *,
    session: Session = Depends(get_session),
    name: str = "",
    offset: int = 0,
    limit: int = Query(default=10, lte=100)
):
    return get_bands(session, name, offset, limit)