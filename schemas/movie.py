from typing import Optional

from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=15, min_length=5)
    overview: str = Field(max_length=50, min_length=15)
    year: int = Field(default=2022, le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)

    class Config:
        schema_extra = {
            'example': {
                'id': 1,
                'title': 'Mi Pelicula',
                'overview': 'Descripcion de la pelicula',
                'year': 2022,
                'rating': 9.8,
                'category': 'Accion'
            }
        }