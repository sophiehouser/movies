from domain.movie import Movie
from storage.istorage import IStorage
import random
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")


class MovieService:
    def __init__(self, storage: IStorage):
        self._storage = storage
        self._movies = self._storage.get_movies()

    def get_movies(self) -> dict[str, Movie]:
        """ Returns all the movies from the storage"""
        return self._storage.get_movies()

    def save_movies(self):
        """ Saves all movies to storage """
        self._storage.save(self._movies)

    def add_movie(self, title: str):
        """
        Gets movies from api and adds to the DB
        """
        url = f"https://www.omdbapi.com/?apikey={API_KEY}&t={title}"

        response = requests.get(url)
        if response.status_code == 200:
            movie_data = response.json()
            if movie_data.get("Response") == "True":
                new_movie = Movie(
                    title=movie_data["Title"],
                    year_of_release=movie_data["Year"],
                    rating=movie_data["imdbRating"],
                    poster=movie_data["Poster"]
                )
                self._movies[new_movie.title] = new_movie
                return True
            else:
                print(f"Movie '{title}' not found.")
                return False
        else:
            print("Failed to fetch movie data from the API.")
            return False

    def delete_movie(self, title: str):
        """
        Deletes a movie based on user input
        :param title: String
        """
        if title in self._movies:
            del self._movies[title]
            print(f"Movie {title} successfully deleted")
        else:
            print(f"Movie {title} doesn't exist!")

    def update_movie(self, title: str):
        """
        Updates movie based on user input
        :param title: String
        """
        if title in self._movies:
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

    def list_movies(self):
        """
        Prints all movies
        """
        print(f"{len(self._movies)} movies in total")

        for movie in self._movies.values():
            print(f"{movie.title} ({movie.year_of_release}): {movie.rating}")

    def get_highest_rated_movies(self):
        """
        Gets the highest rated movies
        :return: []Movies
        """
        if not self._movies:
            return []
        highest_rating = max(movie.rating for movie in self._movies.values())

        highest_rated_movies = []
        for movie in self._movies.values():
            if movie.rating == highest_rating:
                highest_rated_movies.append(movie)

        return highest_rated_movies

    def get_lowest_rated_movies(self):
        """
        Gets the lowest rated movies
        :return: []Movies
        """
        if not self._movies:
            return []
        lowest_rating = min(movie.rating for movie in self._movies.values())

        lowest_rated_movies = []
        for movie in self._movies.values():
            if movie.rating == lowest_rating:
                lowest_rated_movies.append(movie)

        return lowest_rated_movies

    def find_median_rated_movie(self):
        """
        Finds the median rated movie
        :return: Movie
        """
        if not self._movies:
            return None

        sorted_movies = sorted(self._movies.values(), key=lambda movie: movie.rating)
        num_movies = len(sorted_movies)

        if num_movies % 2 == 1:  # Odd number of movies
            median_index = num_movies // 2
        else:  # Even number of movies
            median_index = (num_movies // 2) - 1

        return sorted_movies[median_index]

    def calculate_average_rating(self):
        """
        Calculates the average rating of all the movies
        :return: Float
        """
        if not self._movies:
            return 0.0
        total_rating = sum(movie.rating for movie in self._movies.values())
        return total_rating / len(self._movies)

    def get_random_movie(self):
        """
        Gets a random movie
        :return: Movie
        """
        if not self._movies:
            return None

        return random.choice(list(self._movies.values()))

    def search_movies(self, query: str):
        """
        Searches for movies that have query in the name
        :param query: String
        :return: []Movie
        """
        matching_movies = []
        for movie in self._movies.values():
            if query.lower() in movie.title.lower():
                matching_movies.append(movie)

        return matching_movies

    def get_movies_sorted_by_rating(self):
        """
        Creates array of sorted movies by rating
        :return: []Movie
        """
        return sorted(self._movies.values(), key=lambda movie: movie.rating, reverse=True)

    def generate_html_movies(self):
        """
        Gets movies as a string of html li items
        """
        html_movies = ""
        for movie in self._movies.values():
            html_movies += f"""
            <li>
                <div class="movie">
                    <img class="movie-poster" src="{movie.poster}" title="">
                    <div class="movie-title">{movie.title}</div>
                    <div class="movie-year">{movie.year_of_release}</div>
                </div>
            </li>
            """
        return html_movies
