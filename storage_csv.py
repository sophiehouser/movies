from istorage import IStorage
from movie import Movie
import csv
import os.path


class StorageCSV(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, movies: dict[str, Movie]):
        with open(self.file_path, 'w', newline='') as file:
            fieldnames = ['title', 'rating', 'year', 'poster']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for movie in movies.values():
                writer.writerow({
                    'title': movie.title,
                    'rating': movie.rating,
                    'year': movie.year_of_release,
                    'poster': movie.poster
                })

    def get_movies(self) -> dict[str, Movie]:
        movies = {}
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', newline='') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    title = row['title']
                    movie = Movie(
                        title=title,
                        year_of_release=row['year'],
                        rating=row['rating'],
                        poster=row['poster']
                    )
                    movies[title] = movie
        return movies
