from istorage import IStorage
import random
import json
from movie_storage import Movie


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self.movies = {}
        self.get_movies_from_file(file_path)

    def list_movies(self):
        """
        Prints all movies
        """
        print(f"{len(self.movies)} movies in total")

        for movie in self.movies.values():
            print(f"{movie.title} ({movie.year_of_release}): {movie.rating}")

    def add_movie(self, title, year, rating, poster):
        """
        Adds a movie using user input
        :param title: String
        :param year: Int
        :param rating: Float
        :param poster: String
        """
        self.movies[title] = Movie(title, year, rating, poster)

    def delete_movie(self, title):
        """
        Deletes a movie based on user input
        :param title: String
        """
        if title in self.movies:
            del self.movies[title]
            print(f"Movie {title} successfully deleted")
        else:
            print(f"Movie {title} doesn't exist!")

    def update_movie(self, title, rating):
        """
        Updates movie based on user input
        :param title: String
        """
        if title in self.movies:
            while True:
                year = input("Enter new movie year: ")
                try:
                    year_int = int(year)
                    break
                except ValueError:
                    print("Please enter a valid year")
            while True:
                rating = input("Enter new movie rating: ")
                try:
                    rating_float = float(rating)
                    break
                except ValueError:
                    print("Please enter a valid rating")
            self.add_movie(
                title,
                year_int,
                rating_float
            )
        else:
            print(f"Movie {title} doesn't exist!")

    def save(self):
        """
        Saves all movies to file_path
        """
        movies_dict = {}
        for title, movie in self.movies.items():
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
        return self.movies

    def get_movies_from_file(self, filename):
        """
        Loads all the movies from JSON_FILENAME
        :param filename: String
        """
        try:
            # Attempt to open and read the JSON file
            with open(filename, 'r') as file:
                movies_dict = json.load(file)

            # Convert the dictionaries back into Movie objects
            for title, movie_data in movies_dict.items():
                movie = Movie(
                    title=movie_data['title'],
                    year_of_release=movie_data['year_of_release'],
                    rating=movie_data['rating'],
                    poster=movie_data['poster']
                )
                self.movies[title] = movie

            return movies_dict

        except FileNotFoundError:
            self.movies = {}
