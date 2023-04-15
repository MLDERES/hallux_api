from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship
from dotenv import load_dotenv
from os import getenv

# Create a class called Genre which inherits from SQLModel
class Genre(SQLModel, table=True):
    # Specify a map to all the fields in the database table called Genre
    id: Optional[int] = Field(default=None, primary_key=True, description="Genre ID", sa_column_kwargs={"name":"Genre_Id"})
    name: Optional[str] = Field(default=None, description="Genre Name",sa_column_kwargs={"name":"Genre"})

# Create a class called Customer which inherits from SQLModel  
class Customer(SQLModel, table=True):
    # Specify a map to all the fields in the database table called Customer
    id: Optional[int] = Field(default=None, primary_key=True, description="Customer ID", sa_column_kwargs={"name":"Customer_Id"})
    first_name: Optional[str] = Field(default=None, description="Customer First Name",sa_column_kwargs={"name":"First_Name"})
    last_name: Optional[str] = Field(default=None, description="Customer Last Name",sa_column_kwargs={"name":"Last_Name"})
    name: Optional[str] = Field(default=None, description="Customer Name",sa_column_kwargs={"name":"Name"})
    address: Optional[str] = Field(default=None, description="Customer's Address",sa_column_kwargs={"name":"Street_Address"})
    phone_number: Optional[str] = Field(default=None, description="Customer's Phone Number",sa_column_kwargs={"name":"Phone_Number"})
    email: Optional[str] = Field(default=None, description="Customer's Email Address",sa_column_kwargs={"name":"Email"})
    zip_code_ext: Optional[str] = Field(default=None, description="Customer's Zip Code Extension",sa_column_kwargs={"name":"Zip_Code_Ext"})

    # Create a relationship to the zip_code class
    # The foreign key here must match the sa_column name
    zip_code: Optional[str] = Field(default=None, description="Customer's zip code", foreign_key="zip_code.Zip_Code")

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

# Create a class called Item_Type which inherits from SQLModel
class Item_Type(SQLModel, table=True):
    # Specify a map to all the fields in the database table called Item_Type
    id: Optional[int] = Field(default=None, primary_key=True, description="Item Type ID", sa_column_kwargs={"name":"Item_Type_Id"})
    item_type: Optional[str] = Field(default=None, description="Item Type Description", sa_column_kwargs={"name":"Item_Type"})

# Create a class called Producer which inherits from SQLModel
class Producer(SQLModel, table=True):
    # Specify a map to all the fields in the database table called Producer
    id: Optional[int] = Field(default=None, primary_key=True, description="Producer ID", sa_column_kwargs={"name":"Producer_Id"})
    name: Optional[str] = Field(default=None, description="Producer Name", sa_column_kwargs={"name":"Producer_Name"})

class AlbumBase(SQLModel):
    name: str = Field(default=None, description="Album Title", sa_column_kwargs={"name":"Album_Name"})
    release_date: Optional[datetime] = Field(default=None, description="Album Release Date")
    production_cost: Optional[float] = Field(default=None, description="Cost to produce the album", sa_column_kwargs={"name":"Production_Cost"})
    band_id: int = Field(default=None, description="Band ID", sa_column_kwargs={"name":"Band_Id"}, foreign_key="band.Band_id")

class Album(AlbumBase, table=True):
    # Specify a map to all the fields in the database table called Album
    id: Optional[int] = Field(default=None, primary_key=True, description="Album ID", sa_column_kwargs={"name":"Album_Id"})
    band: Optional["Band"] = Relationship(back_populates="albums")
    songs : List["Song"] = Relationship(back_populates="album")  

class AlbumRead(AlbumBase):
    id: int

# Create the base Person class with the fields that are common to all the Person types
# This class will be inherited by the other Person classes
class PersonBase(SQLModel):
    first_name: Optional[str] = Field(default=None, description="Person First Name",)
    last_name: Optional[str] = Field(default=None, description="Person Last Name",)
    address: Optional[str] = Field(default=None, description="Person's Address",sa_column_kwargs={"name":"street_address"})
    phone_number: Optional[str] = Field(default=None, description="Person's Phone Number")
    email: Optional[str] = Field(default=None, description="Person's Email Address")
    zip_code_ext: Optional[str] = Field(default=None, description="Person's Zip Code Extension")
    zip_code: Optional[str] = Field(default=None, description="Person's Zip Code")
    
# Create a class called Person which inherits from SQLModel
class Person(PersonBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, description="Person ID", sa_column_kwargs={"name":"Person_Id"})
    
    # Relationships can ONLY be defined in the table models
    bands: List["Band"] = Relationship(back_populates="primary_contact")

    band_links: List["Band_Member"] = Relationship(back_populates="member")

class PersonRead(PersonBase):
    id: int

# Create the Band base class
class BandBase(SQLModel):
    status_code: Optional[str] = Field(default=None, description="Band Status Code", sa_column_kwargs={"name":"Band_Status_Code"})
    name: Optional[str] = Field(default=None, description="Name of the band", sa_column_kwargs={"name":"Band_Name"})
    formation_date: Optional[datetime] = Field(default=None, description="Date the band was formed")
    # The foreign key here must match the sa_column name
    primary_contact_id: Optional[int] = Field(default=None, description="ID of the primary contact for the band", foreign_key="person.Person_Id")

class Band(BandBase, table=True):
    # Specify a map to all the fields in the database table called Band
    id: Optional[int] =Field(default=None, primary_key=True, description="Band ID", sa_column_kwargs={"name":"Band_id"})

    # Create a relationship to the Person class
    # Relationships can ONLY be defined in the table models
    primary_contact: Optional[Person] = Relationship(back_populates="bands")

    band_members: List["Band_Member"] = Relationship(back_populates="band")
    albums: List[Album] = Relationship(back_populates="band")

class BandRead(BandBase):
    id: int

class BandReadWithPersons(BandBase):
    primary_contact : Optional[PersonRead]=None
    members : Optional[PersonRead] = None

class Band_Member(SQLModel, table=True,):
    status : Optional[str] = None
    band_id : Optional[int] = Field(default=None, description="Band ID", sa_column_kwargs={"name":"Band_id"}, foreign_key="band.Band_id")
    member_id: int = Field(default=None, description="Member ID", 
                           sa_column_kwargs={"name":"Member_Id"}, foreign_key="person.Person_Id", primary_key=True)
    join_date: Optional[datetime] = Field(default=None, description="Date the band member joined the band")

    band: "Band" = Relationship(back_populates="band_members")
    member: "Person" = Relationship(back_populates="band_links")

# Create a class called Instrument which inherits from SQLModel
class Instrument(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, description="Instrument ID", sa_column_kwargs={"name":"Instrument_Id"})

class SongBase(SQLModel):
    name: Optional[str] = Field(default=None, description="Song Title", sa_column_kwargs={"name":"Song_Name"})
    duration: Optional[int] = Field(default=None, description="Duration in seconds", sa_column_kwargs={"name":"Duration_Seconds"})
    sequence: Optional[int] = Field(default=None, description="Sequence of the song in the album")

class Song(SongBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, description="Song ID", sa_column_kwargs={"name":"Song_Id"})
    album_id: Optional[int] = Field(default=None, description="Album ID where the song was recorded", sa_column_kwargs={"name":"Album_id"}, foreign_key="album.Album_Id")
    album: Optional[Album] = Relationship(back_populates="songs")

class SongRead(SongBase):
    id: int

class SongReadWithAlbum(SongBase):
    album : Optional[AlbumRead] = None

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

