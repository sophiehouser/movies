from istorage import IStorage
import json
from movie import Movie


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, movies: dict[str, Movie]):
        """
        Saves all movies to file_path
        """
        movies_dict = {}
        for title, movie in movies.items():
            movies_dict[title] = {
                "title": movie.title,
                "year_of_release": movie.year_of_release,
                "rating": movie.rating,
                "poster": movie.poster
            }

        # Write the dictionary to a JSON file
        with open(self.file_path, 'w') as file:
            json.dump(movies_dict, file, indent=4)

    def get_movies(self) -> dict[str, Movie]:
        """
        Loads all the movies from file_path
        """
        try:
            # Attempt to open and read the JSON file
            with open(self.file_path, 'r') as file:
                movies_dict = json.load(file)

            movies = {}
            # Convert the dictionaries back into Movie objects
            for title, movie_data in movies_dict.items():
                movie = Movie(
                    title=movie_data['title'],
                    year_of_release=movie_data['year_of_release'],
                    rating=movie_data['rating'],
                    poster=movie_data['poster']
                )
                movies[title] = movie

            return movies

        except FileNotFoundError:
            return {}
