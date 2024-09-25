from movie_app import MovieApp
from storage_json import StorageJson

if __name__ == '__main__':
    storage = StorageJson('data.json')
    movie_app = MovieApp(storage)
    movie_app.run()
