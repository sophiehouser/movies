
class StorageCSV(IStorage):  # pylint: disable=too-few-public-methods
    def __init__(self, file_path):
        self.file_path = file_path
        self.movies = {}
        self.get_movies_from_file(file_path)

    def list_movies(self):
        """
        Prints all movies
        """
        print(f"{len(self.movies)} movies in total")