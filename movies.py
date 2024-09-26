# from movie_service import *
# import sys
#
#
# def exit_option(db: MovieService):
#     """
#     Saves movies and exits the program
#     :param db: MovieDatabase
#     """
#     db.save_movies()
#     print("Exiting after saving movies")
#     sys.exit()
#
#
# def list_movies_option(db: MovieService):
#     """
#     Lists all movies
#     :param db: MovieDatabase
#     """
#     db.list_movies()
#
#
# def add_movie_option(db: MovieService, title=""):
#     """
#     Adds a movie to the DB
#     :param db: MovieDatabase
#     :param title: String
#     """
#     while True:
#         title = input("Enter new movie name: ")
#         if title == "" or title.isspace():
#             print("Please enter a valid name")
#         else:
#             break
#     while True:
#         year = input("Enter new movie year: ")
#         try:
#             year_int = int(year)
#             break
#         except ValueError:
#             print("Please enter a valid year")
#     while True:
#         rating = input("Enter new movie rating: ")
#         try:
#             rating_float = float(rating)
#             break
#         except ValueError:
#             print("Please enter a valid rating")
#
#     db.add_movie(title, year_int, rating_float)
#
#
# def delete_movie_option(db: MovieService):
#     """
#     Deletes movie from database
#     :param db: MovieDatabase
#     """
#     name = input("Enter movie name to delete: ")
#     db.delete_movie(name)
#
#
# def update_movie_option(db: MovieService):
#     """
#     Update user input movie
#     :param db: MovieDatabase
#     """
#     name = input("Enter movie name to update: ")
#     if db.has_movie(name):
#         while True:
#             year = input("Enter new movie year: ")
#             try:
#                 year_int = int(year)
#                 break
#             except ValueError:
#                 print("Please enter a valid year")
#         while True:
#             rating = input("Enter new movie rating: ")
#             try:
#                 rating_float = float(rating)
#                 break
#             except ValueError:
#                 print("Please enter a valid rating")
#
#         db.add_movie(name, year_int, rating_float)
#     else:
#         print("Unknown movie")
#
#
# def stats_option(db: MovieService):
#     """
#     Give stats about movies in db
#     :param db: MovieDatabase
#     """
#     if len(db.movies) == 0:
#         print("No movies to give stats on")
#         return
#
#     average = db.calculate_average_rating()
#     median = db.find_median_rated_movie()
#     best = db.get_highest_rated_movies()
#     worst = db.get_lowest_rated_movies()
#
#     print(f"Average rating: {average}")
#     if median:
#         print(f"Median rating: {median.rating}")
#     for movie in best:
#         print(f"Best movie: {movie.title}, {movie.rating}")
#     for movie in worst:
#         print(f"Worst movie: {movie.title}, {movie.rating}")
#
#
# def random_movie_option(db: MovieService):
#     """
#     Prints a random movie
#     :param db: MovieDatabase
#     """
#     movie = db.get_random_movie()
#     if movie:
#         print(f"Random Movie: {movie.title} ({movie.year_of_release}), Rating: {movie.rating}")
#     else:
#         print("No movies available.")
#
#
# def search_movie_option(db: MovieService):
#     """
#     Prints all movies where the title contains the user input
#     :param db: MovieDatabase
#     """
#     query = input("Enter part of the movie name to search: ")
#     matching_movies = db.search_movies(query)
#
#     if not matching_movies:
#         print("No matching movies")
#     else:
#         for movie in matching_movies:
#             print(f"{movie.title}, {movie.rating}")
#
#
# def sorted_by_rating_option(db: MovieService):
#     """
#     Prints the movies sorted by rating
#     :param db: MovieDatabase
#     """
#     sorted_movies = db.get_movies_sorted_by_rating()
#
#     if sorted_movies:
#         print("Movies sorted by rating (highest to lowest):")
#         for movie in sorted_movies:
#             print(f"{movie.title} ({movie.year_of_release}), Rating: {movie.rating}")
#     else:
#         print("No movies available to sort.")
#
#
# menu_options_map = {
#     "0": ("Exit", exit_option),
#     "1": ("List movies", list_movies_option),
#     "2": ("Add movie", add_movie_option),
#     "3": ("Delete movie", delete_movie_option),
#     "4": ("Update movie", update_movie_option),
#     "5": ("Stats", stats_option),
#     "6": ("Random movie", random_movie_option),
#     "7": ("Search movie", search_movie_option),
#     "8": ("Movies sorted by rating", sorted_by_rating_option),
# }
#
#
# def print_menu_options():
#     """
#     Prints all the menu options
#     """
#     for k, v in menu_options_map.items():
#         print(str(k) + ". " + str(v[0]))
#
#     print("Enter choice (0-10):")
#
#
# def manage_user_input(user_input, db: MovieService):
#     """
#     Decides which actions to take based on the user's input
#     :param db: instance of MovieDatabase
#     :param user_input: String
#     """
#
#     user_input_list = user_input.split()
#
#     if len(user_input_list) == 0:
#         return
#
#     user_choice = user_input_list[0]
#
#     if user_choice in menu_options_map.keys():
#         option = menu_options_map[user_choice]
#         option[1](db)
#     else:
#         print("Unknown command")
#
#
# def main():
#     db = MovieService()
#     print("********** My Movies Database **********")
#
#     while True:
#         try:
#             print_menu_options()
#
#             user_input = input()
#             manage_user_input(user_input, db)
#
#             input("Press enter to continue ")
#         finally:
#             db.save_movies()
#
#
# if __name__ == '__main__':
#     main()
