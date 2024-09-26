from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCSV
from movie_service import MovieService

if __name__ == '__main__':
    storage = StorageJson('data.json')
    # storage = StorageCSV('data.csv')
    service = MovieService(storage)
    movie_app = MovieApp(service)
    movie_app.run()
