from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship,DateTime
from dotenv import load_dotenv
from os import getenv
import pyodbc

# Create a class called Person which inherits from SQLModel
class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, description="Person ID", sa_column_kwargs={"name":"Person_Id"})
    first_name: Optional[str] = Field(default=None, description="Person First Name",)
    last_name: Optional[str] = Field(default=None, description="Person Last Name",)
    address: Optional[str] = Field(default=None, description="Person's Address",sa_column_kwargs={"name":"street_address"})
    phone_number: Optional[str] = Field(default=None, description="Person's Phone Number")
    email: Optional[str] = Field(default=None, description="Person's Email Address")
    zip_code_ext: Optional[str] = Field(default=None, description="Person's Zip Code Extension")
    zip_code: Optional[str] = Field(default=None, description="Person's Zip Code")
    
    bands: List["Band"] = Relationship(back_populates="primary_contact")

class Band(SQLModel, table=True):
    # Specify a map to all the fields in the database table called Band
    id: Optional[int] =Field(default=None, primary_key=True, description="Band ID", sa_column_kwargs={"name":"Band_id"})
    status_code: Optional[str] = Field(default=None, description="Band Status Code", sa_column_kwargs={"name":"Band_Status_Code"})
    name: Optional[str] = Field(default=None, description="Name of the band", sa_column_kwargs={"name":"Band_Name"})
    formation_date: Optional[datetime] = Field(default=None, description="Date the band was formed")
    
    # The foreign key here must match the sa_column name
    primary_contact_id: Optional[int] = Field(default=None, description="ID of the primary contact for the band", foreign_key="person.Person_Id")

    # Create a relationship to the Person class
    primary_contact: Optional[Person] = Relationship(back_populates="bands")

class State(SQLModel, table=True):
    abbr: Optional[str] = Field(default=None, primary_key=True, sa_column_kwargs={"name":"State_Abbr"})
    name: Optional[str] = Field(default=None,sa_column_kwargs={"name":"State_Name"})
    zip_codes: List["Zip_Code"] = Relationship(back_populates="state")

class Zip_Code(SQLModel, table=True):
    zip_code : Optional[str] = Field(default=None, primary_key=True, description="Zip Code", sa_column_kwargs={"name":"Zip_Code"})
    state_abbr : Optional[str] = Field(default=None, description="State Abbreviation", sa_column_kwargs={"name":"State_Abbr"},foreign_key="state.State_Abbr")
    city : Optional[str] = Field(default=None, description="City")
    latitude : Optional[float] = Field(default=None, description="Latitude")
    longitude : Optional[float] = Field(default=None, description="Longitude")

    # Create a relationship to the State class
    state: Optional[State] = Relationship(back_populates="zip_codes")

# # Create a class called Instrument which inherits from SQLModel
# class Instrument(SQLModel, table=True):
#     pass


# # Create a class called Album which inherits from SQLModel
# class Album(SQLModel, table=True):
#     pass
# # Create a class called Song which inherits from SQLModel
# class Song(SQLModel, table=True):

#     pass
# # Create a class called Band_Instrument which inherits from SQLModel
# class Band_Instrument(SQLModel, table=True):
#     pass
# # Create a class called Band_Person which inherits from SQLModel
# class Band_Person(SQLModel, table=True):
#     pass
# # Create a class called Album_Song which inherits from SQLModel
# class Album_Song(SQLModel, table=True):
#     pass
# # Create a class called Person_Instrument which inherits from SQLModel
# class Person_Instrument(SQLModel, table=True):
#     pass
# # Create a class called Person_Song which inherits from SQLModel
# class Person_Song(SQLModel, table=True):
#     pass
# # Create a class called Band_Album which inherits from SQLModel
# class Band_Album(SQLModel, table=True):
#     pass
# # Create a class called Band_Song which inherits from SQLModel
# class Band_Song(SQLModel, table=True):
#     pass

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