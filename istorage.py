from abc import ABC, abstractmethod
from movie import Movie


class IStorage(ABC):
    @abstractmethod
    def save(self, movies: dict[str, Movie]):
        pass

    @abstractmethod
    def get_movies(self) -> dict[str, Movie]:
        pass
