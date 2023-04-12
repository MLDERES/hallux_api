from typing import Union

from fastapi import FastAPI
from src.model import get_bands_by_name, get_bands, get_band_by_id, get_persons_by_first_name, get_persons_by_last_name
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/bands/")
def get_band(q: Union[str, None] = None):
    return get_bands()


@app.get("/bands/{band_id}")
def read_item(band_id: int, q: Union[str, None] = None):
    return get_band_by_id(band_id)