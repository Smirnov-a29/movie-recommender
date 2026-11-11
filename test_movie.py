from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    title: str
    year: int
    genre: str

movie = Movie(
    id = 4,
    title = "The Dark Knight",
    year = "2008",
    genre = "Aciton"
)
print(movie)
print(movie.title)
print(movie.year)
print(movie.model_dump())