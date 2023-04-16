from typing import Union, List, Optional
from fastapi import FastAPI, HTTPException, status, Query, Depends
from sqlmodel import Session
from src.model import (
    AgentRead,
    AlbumReadWithSongs,
    PersonRead,
    Album,
    BandRead,
    BandReadWithPersons,
    SongRead,
    BandReadWithPersons,
    BandRead,
    PersonRead,
    SongRead,
)
from src.db import (
    get_agents,
    get_album_by_id,
    get_albums,
    get_bands,
    get_band_by_id,
    get_persons,
    get_bands,
    get_persons,
    get_person_by_id,
    get_session,
    get_song_by_id,
    get_songs,
)

version = "0.1.0"

app = FastAPI()


@app.get("/")
def read_root():
    return {"Version": version}


@app.get("/bands", response_model=List[BandRead])
def read_band(
    *,
    session: Session = Depends(get_session),
    name: str = "",
    offset: int = 0,
    limit: int = Query(default=10, lte=100)
):
    return get_bands(session, name, offset, limit)
    # return get_bands(name, offset, limit)


@app.get("/bands/{band_id}", response_model=BandReadWithPersons)
def read_band_by_id(*, session: Session = Depends(get_session), band_id: int):
    band = get_band_by_id(session, band_id)
    if not band:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Band not found."
        )
    return band


@app.get("/persons", response_model=List[PersonRead])
def read_persons(
    first_name: str = "",
    last_name: str = "",
    offset: int = 0,
    limit: int = Query(default=10, lte=100),
):
    persons = get_persons(
        first_name=first_name, last_name=last_name, offset=offset, limit=limit
    )
    return persons


@app.get("/persons/{person_id}", response_model=PersonRead)
def read_persons_by_id(person_id: int):
    person = get_person_by_id(person_id)
    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Person not found."
        )
    return person


@app.get("/albums", response_model=List[Album])
def read_albums(
    name: str = "", offset: int = 0, limit: int = Query(default=10, lte=100)
):
    return get_albums(name, offset, limit)


@app.get("/albums/{album_id}", response_model=AlbumReadWithSongs)
def read_album_by_id(*, album_id: int, session: Session = Depends(get_session)):
    album = get_album_by_id(session, album_id)
    if not album:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Album not found."
        )
    return album


@app.get("/songs", response_model=List[SongRead])
def read_songs(
    *,
    session: Session = Depends(get_session),
    name: str = "",
    offset: int = 0,
    limit: int = Query(default=10, lte=100)
):
    return get_songs(session, name, offset, limit)


@app.get("/songs/{song_id}", response_model=SongRead)
def read_song_by_id(*, session: Session = Depends(get_session), song_id: int):
    song = get_song_by_id(session, song_id)
    if not song:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Song not found."
        )
    return song


@app.get("/agents", response_model=List[AgentRead])
def read_agents(
    *,
    session: Session = Depends(get_session),
    name: str = "",
    offset: int = 0,
    limit: int = Query(default=10, lte=100)
):
    return get_agents(session, name, offset, limit)
