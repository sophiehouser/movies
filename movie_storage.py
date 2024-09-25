import random
import json

JSON_FILENAME = "data.json"


class Movie:
    def __init__(self, title: str, year_of_release: int, rating: float, poster: str) -> None:
        self.title = title
        self.year_of_release = year_of_release
        self.rating = rating
        self.poster = poster


class MovieDatabase:
    def __init__(self):
        self.movies = {}
        self.load_from_file(JSON_FILENAME)

    def save(self):
        """
        Saves all movies to JSON_FILENAME
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
        with open(JSON_FILENAME, 'w') as file:
            json.dump(movies_dict, file, indent=4)

    def load_from_file(self, filename):
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

        except FileNotFoundError:
            self.movies = {}

    def has_movie(self, title: str):
        """
        Checks if movie is in DB
        :param title: String
        :return: Bool
        """
        if title in self.movies:
            return True
        else:
            return False

    def add_movie(self, title: str, year_of_release: int, rating: float):
        """
        Adds a movie using user input
        :param title: String
        :param year_of_release: Int
        :param rating: Float
        """
        self.movies[title] = Movie(title, year_of_release, rating, "")

    def delete_movie(self, title: str):
        """
        Deletes a movie based on user input
        :param title: String
        """
        if title in self.movies:
            del self.movies[title]
            print(f"Movie {title} successfully deleted")
        else:
            print(f"Movie {title} doesn't exist!")

    def update_movie(self, title: str):
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

    def list_movies(self):
        """
        Prints all movies
        """
        print(f"{len(self.movies)} movies in total")

        for movie in self.movies.values():
            print(f"{movie.title} ({movie.year_of_release}): {movie.rating}")

    def get_highest_rated_movies(self):
        """
        Gets the highest rated movies
        :return: []Movies
        """
        if not self.movies:
            return []
        highest_rating = max(movie.rating for movie in self.movies.values())

        highest_rated_movies = []
        for movie in self.movies.values():
            if movie.rating == highest_rating:
                highest_rated_movies.append(movie)

        return highest_rated_movies

    def get_lowest_rated_movies(self):
        """
        Gets the lowest rated movies
        :return: []Movies
        """
        if not self.movies:
            return []
        lowest_rating = min(movie.rating for movie in self.movies.values())

        lowest_rated_movies = []
        for movie in self.movies.values():
            if movie.rating == lowest_rating:
                lowest_rated_movies.append(movie)

        return lowest_rated_movies

    def find_median_rated_movie(self):
        """
        Finds the median rated movie
        :return: Movie
        """
        if not self.movies:
            return None

        sorted_movies = sorted(self.movies.values(), key=lambda movie: movie.rating)
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
        if not self.movies:
            return 0.0
        total_rating = sum(movie.rating for movie in self.movies.values())
        return total_rating / len(self.movies)

    def get_random_movie(self):
        """
        Gets a random movie
        :return: Movie
        """
        if not self.movies:
            return None

        return random.choice(list(self.movies.values()))

    def search_movies(self, query: str):
        """
        Searches for movies that have query in the name
        :param query: String
        :return: []Movie
        """
        matching_movies = []
        for movie in self.movies.values():
            if query.lower() in movie.title:
                matching_movies.append(movie)

        return matching_movies

    def get_movies_sorted_by_rating(self):
        """
        Creates array of sorted movies by rating
        :return: []Movie
        """
        return sorted(self.movies.values(), key=lambda movie: movie.rating, reverse=True)
