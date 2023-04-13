from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship
from dotenv import load_dotenv
from os import getenv

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

# Create a class called Album which inherits from SQLModel
class Album(SQLModel, table=True):
    # Specify a map to all the fields in the database table called Album
    id: Optional[int] = Field(default=None, primary_key=True, foreign_key='Item.Item_Id', description="Album ID", sa_column_kwargs={"name":"Album_Id"})
    name: Optional[str] = Field(default=None, description="Album Title", sa_column_kwargs={"name":"Album_Name"})
    release_date: Optional[datetime] = Field(default=None, description="Album Release Date")
    production_cost: Optional[float] = Field(default=None, description="Cost to produce the album", sa_column_kwargs={"name":"Production_Cost"})
    band_id: int = Field(default=None, description="Band ID", sa_column_kwargs={"name":"Band_Id"}, foreign_key="Band.Band_id")    
    
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


# Create a class called Instrument which inherits from SQLModel
class Instrument(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, description="Instrument ID", sa_column_kwargs={"name":"Instrument_Id"})


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

