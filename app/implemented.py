# файл для создания DAO и сервисов чтобы импортировать их везде
from app.dao.directorDAO import DirectorDAO
from app.dao.genreDAO import GenreDAO
from app.dao.model.director import DirectorSchema
from app.dao.model.genre import GenreSchema
from app.dao.model.movie import MovieSchema
from app.dao.movieDAO import MovieDAO
from app.service.directorsSERVICE import DirectorService
from app.service.genresSERVICE import GenreService
from app.service.moviesSERVICE import MovieService
from app.setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)
