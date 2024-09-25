from istorage import IStorage
import sys


class MovieApp:
    def __init__(self, storage: IStorage):
        self._storage = storage
        self._movies = self._storage.get_movies()

        self._menu_options_map = {
            "0": ("Exit", self._command_exit_option),
            "1": ("List movies", self._command_list_movies),
            # "2": ("Add movie", self._),
            # "3": ("Delete movie", delete_movie_option),
            # "4": ("Update movie", update_movie_option),
            "2": ("Stats", self._command_movie_stats),
            # "6": ("Random movie", random_movie_option),
            # "7": ("Search movie", search_movie_option),
            # "8": ("Movies sorted by rating", sorted_by_rating_option),
        }

    def _command_exit_option(self):
        """
        Saves movies and exits the program
        :param db: MovieDatabase
        """
        self._storage.save()
        print("Exiting after saving movies")
        sys.exit()

    def _command_list_movies(self):
        self._storage.list_movies()

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

    def _command_movie_stats(self):
        """
        Give stats about movies in db
        """
        if len(self._movies.values()) == 0:
            print("No movies to give stats on")
            return

        average = self.calculate_average_rating()
        median = self.find_median_rated_movie()
        best = self.get_highest_rated_movies()
        worst = self.get_lowest_rated_movies()

        print(f"Average rating: {average}")
        if median:
            print(f"Median rating: {median.rating}")
        for movie in best:
            print(f"Best movie: {movie.title}, {movie.rating}")
        for movie in worst:
            print(f"Worst movie: {movie.title}, {movie.rating}")

        ...

    def _generate_website(self):
        ...

    def _manage_user_input(self, user_input):
        """
        Decides which actions to take based on the user's input
        :param db: instance of MovieDatabase
        :param user_input: String
        """

        user_input_list = user_input.split()

        if len(user_input_list) == 0:
            return

        user_choice = user_input_list[0]

        if user_choice in self._menu_options_map.keys():
            option = self._menu_options_map[user_choice]
            option[1]()
        else:
            print("Unknown command")

    def _print_menu_options(self):
        """
        Prints all the menu options
        """
        for k, v in self._menu_options_map.items():
            print(str(k) + ". " + str(v[0]))

        print("Enter choice (0-10):")

    def run(self):
        print("********** My Movies Database **********")

        while True:
            try:
                self._print_menu_options()

                user_input = input()
                self._manage_user_input(user_input)

                input("Press enter to continue ")
            finally:
                self._storage.save()
