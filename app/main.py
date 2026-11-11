from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Movie Recommender API",
    description="API for movie recommendations",
    version="0.1.0"
)

class Movie(BaseModel):
    id: int
    title: str
    year: int
    genre: str

movies = [
        {
            "id": 1,
            "title": "Interstellar",
            "year": 2014,
            "genre": "Sci-Fi"
        },
        {
            "id": 2,
            "title": "The Matrix",
            "year": 1999,
            "genre": "Sci-Fi"
        },
        {
            "id": 3,
            "title": "The Green Mile",
            "year": 1999,
            "genre": "Drama"
        },
        {
            "id": 4,
            "title": "Inception",
            "year": 2010,
            "genre": "Sci-Fi"
        },
    ]

@app.get("/")
def read_root():
    return {"message": "Movie Recommender API is running"}

@app.get("/movies", response_model=list[Movie])
def get_movies():
    return movies

@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie_by_id(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie

    raise HTTPException(
        status_code=404,
        detail="Movie not found")

@app.post("/movies",response_model=Movie, status_code=201)
def create_movie(movie: Movie):
    new_movie = movie.model_dump()
    movies.append(new_movie)
    return movie