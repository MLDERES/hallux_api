from typing import Union, List, Optional

from fastapi import FastAPI, HTTPException,status, Query
from src.model import Band, Person, Instrument, Album 
from src.db import get_album_by_id, get_albums, get_bands, get_band_by_id, get_persons,get_bands, get_persons, get_person_by_id

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/bands", response_model=List[Band])
def read_band(name: str = '', offset: int=0, limit:int=Query(default=10,lte=100)):
    return get_bands(name, offset, limit)


@app.get("/bands/{band_id}", response_model=Band)
def read_band_by_id(band_id: int):
    band = get_band_by_id(band_id)
    if not band:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Band not found.')
    return band


@app.get("/persons", response_model=List[Person])
def read_persons(first_name: str = '', last_name:str ='', offset: int=0, limit:int=Query(default=10,lte=100)):
    persons = get_persons(first_name=first_name,last_name=last_name,offset=offset,limit=limit)
    return persons

@app.get("/persons/{person_id}", response_model=Person)
def read_persons_by_id(person_id: int):
    person = get_person_by_id(person_id)
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Person not found.')
    return person

@app.get("/albums", response_model=List[Album])
def read_albums(name: str = '', offset: int=0, limit:int=Query(default=10,lte=100)):
    return get_albums(name, offset, limit)

@app.get("/albums/{album_id}", response_model=Album)
def read_album_by_id(album_id: int):
    album = get_album_by_id(album_id)
    if not album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Album not found.')
    return album


