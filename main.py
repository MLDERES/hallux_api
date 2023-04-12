from typing import Union, List, Optional

from fastapi import FastAPI, HTTPException,status, Query
from src.model import get_bands, get_band_by_id, get_persons_by_first_name, get_persons_by_last_name,Band
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/bands", response_model=List[Band])
def get_band(name: str = '', offset: int=0, limit:int=Query(default=10,lte=100)):
    return get_bands(name, offset, limit)


@app.get("/bands/{band_id}", response_model=Band)
def read_band_by_id(band_id: int):
    band = get_band_by_id(band_id)
    if not band:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Band not found.')
    return band

@app.get("/bands/{band_name}", response_model=List[Band])
def read_band_by_id(band_name: str = '', offset: int=0, limit:int=Query(default=10,lte=100)):
    return get_bands_by_name(band_name, offset, limit)

