from abc import ABC, abstractmethod
from movie_storage import Movie


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        pass

    @abstractmethod
    def delete_movie(self, title):
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def get_movies(self) -> dict[str, Movie]:
        pass