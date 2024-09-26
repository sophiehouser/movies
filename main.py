from movie_app import MovieApp
from storage.storage_json import StorageJson
from movie_service import MovieService

if __name__ == '__main__':
    storage = StorageJson('data/data.json')
    # storage = StorageCSV('data.csv')
    service = MovieService(storage)
    movie_app = MovieApp(service)
    movie_app.run()
