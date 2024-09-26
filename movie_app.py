from movie_service import MovieService
import sys


class MovieApp:
    def __init__(self, service: MovieService):
        self._movies_service = service

        self._menu_options_map = {
            "0": ("Exit", self._command_exit_option),
            "1": ("List movies", self._command_list_movies),
            "2": ("Add movie", self._command_add_movie),
            "3": ("Delete movie", self._command_delete_movie),
            "4": ("Stats", self._command_movie_stats),
            "6": ("Random movie", self._command_random_movie),
            "7": ("Search movie", self._command_search_movie),
            "8": ("Movies sorted by rating", self._command_sorted_by_rating),
        }

    def _command_delete_movie(self):
        """
        Deletes movie from database
        """
        name = input("Enter movie name to delete: ")
        self._movies_service.delete_movie(name)

    def _command_exit_option(self):
        """
        Saves movies and exits the program
        """
        self._movies_service.save_movies()
        print("Exiting after saving movies")
        sys.exit()

    def _command_list_movies(self):
        """
        Prints all movies
        """
        print(f"{len(self._movies_service.movies)} movies in total")

        for movie in self._movies_service.movies.values():
            print(f"{movie.title} ({movie.year_of_release}): {movie.rating}")

    def _command_movie_stats(self):
        """
        Give stats about movies in db
        """
        if len(self._movies_service.movies) == 0:
            print("No movies to give stats on")
            return

        average = self._movies_service.calculate_average_rating()
        median = self._movies_service.find_median_rated_movie()
        best = self._movies_service.get_highest_rated_movies()
        worst = self._movies_service.get_lowest_rated_movies()

        print(f"Average rating: {average}")
        if median:
            print(f"Median rating: {median.rating}")
        for movie in best:
            print(f"Best movie: {movie.title}, {movie.rating}")
        for movie in worst:
            print(f"Worst movie: {movie.title}, {movie.rating}")

    def _command_add_movie(self):
        """
        Adds a movie to the DB
        """
        while True:
            title = input("Enter new movie name: ")
            if title == "" or title.isspace():
                print("Please enter a valid name")
            else:
                break

        self._movies_service.add_movie(title)

    def _command_random_movie(self):
        """
        Prints a random movie
        """
        movie = self._movies_service.get_random_movie()
        if movie:
            print(f"Random Movie: {movie.title} ({movie.year_of_release}), Rating: {movie.rating}")
        else:
            print("No movies available.")

    def _command_search_movie(self):
        """
        Prints all movies where the title contains the user input
        """
        query = input("Enter part of the movie name to search: ")
        matching_movies = self._movies_service.search_movies(query)

        if not matching_movies:
            print("No matching movies")
        else:
            for movie in matching_movies:
                print(f"{movie.title}, {movie.rating}")

    def _command_sorted_by_rating(self):
        """
        Prints the movies sorted by rating
        """
        sorted_movies = self._movies_service.get_movies_sorted_by_rating()

        if sorted_movies:
            print("Movies sorted by rating (highest to lowest):")
            for movie in sorted_movies:
                print(f"{movie.title} ({movie.year_of_release}), Rating: {movie.rating}")
        else:
            print("No movies available to sort.")

    def _generate_website(self):
        ...

    def _manage_user_input(self, user_input):
        """
        Decides which actions to take based on the user's input
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
                self._movies_service.save_movies()
