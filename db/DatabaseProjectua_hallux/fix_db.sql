ALTER TABLE album
ALTER COLUMN Album_Name nvarchar(100);

UPDATE Album
SET Album_Name = Trim(Album_Name)

ALTER TABLE Band
ALTER COLUMN Band_Name nvarchar(100);

UPDATE Band
SET Band_Name = Trim(Band_Name)

ALTER TABLE Customer
ALTER COLUMN Phone_Number nvarchar(20);

ALTER TABLE Customer
ALTER COLUMN First_Name nvarchar(50);

ALTER TABLE Customer
ALTER COLUMN Last_Name nvarchar(50);

ALTER TABLE Customer
ALTER COLUMN Street_Address nvarchar(100);

ALTER TABLE Customer
ALTER COLUMN "Name" nvarchar(100);

ALTER TABLE Customer
ALTER COLUMN Email nvarchar(100);

UPDATE Customer
SET Phone_Number= trim(phone_number)
	,first_name = trim(first_name)
	,last_name = trim(last_name)
	,Street_Address = trim(Street_Address)
	,"Name"=trim("Name")
	,email = trim(email)

ALTER TABLE Genre
ALTER COLUMN Genre nvarchar(50);
UPDATE Genre
SET Genre = TRIM(Genre)

ALTER TABLE Instrument
ALTER COLUMN Instrument_Name nvarchar(50);

UPDATE Instrument
SET Instrument_Name = TRIM(Instrument_Name)

ALTER TABLE Item
ALTER COLUMN Item_Description nvarchar(200);
UPDATE Item
SET Item_Description = TRIM(Item_Description)

ALTER TABLE Item_Type
ALTER COLUMN Item_Type nvarchar(20);
UPDATE Item_Type
SET Item_Type = TRIM(Item_Type)

ALTER TABLE Order_Source
ALTER COLUMN Source_Description nvarchar(200);
ALTER TABLE Order_Source
ALTER COLUMN Source_Name nvarchar(100);

UPDATE Order_Source
SET Source_Description=TRIM(Source_Description)
	,Source_Name = TRIM(Source_Name)

ALTER TABLE Person
ALTER COLUMN Phone_Number nvarchar(20);
ALTER TABLE Person
ALTER COLUMN First_Name nvarchar(50);
ALTER TABLE Person
ALTER COLUMN Last_Name nvarchar(50);
ALTER TABLE Person
ALTER COLUMN Street_Address nvarchar(100);
ALTER TABLE Person
ALTER COLUMN Email nvarchar(100);

UPDATE Person
SET Phone_Number= trim(phone_number)
	,first_name = trim(first_name)
	,last_name = trim(last_name)
	,Street_Address = trim(Street_Address)
	,Email=Trim(email)

ALTER TABLE Producer
ALTER COLUMN Producer_Name nvarchar(100);

UPDATE Producer
SET Producer_Name = TRIM(Producer_Name)

ALTER TABLE Song
ALTER COLUMN Song_Name nvarchar(100);

UPDATE Song
SET Song_Name = TRIM(Song_Name)

ALTER TABLE State
ALTER COLUMN State_Name nvarchar(100);

UPDATE State
SET State_Name = TRIM(State_Name)

ALTER TABLE Venue
ALTER COLUMN Venue_Name nvarchar(100);

ALTER TABLE Venue
ALTER COLUMN Street_Address nvarchar(100);

ALTER TABLE Venue
ALTER COLUMN Contact_Phone nvarchar(20);

UPDATE Venue
SET Venue_Name = TRIM(Venue_Name)
	, Street_Address = TRIM(Street_Address)
	, Contact_Phone = TRIM(Contact_Phone)

ALTER TABLE Video
ALTER COLUMN Video_Name nvarchar(100);
UPDATE Video
SET Video_Name = Trim(Video_Name)

ALTER TABLE Zip_Code
ALTER COLUMN City nvarchar(50);
UPDATE Zip_Code
SET City = TRIM(City)

















