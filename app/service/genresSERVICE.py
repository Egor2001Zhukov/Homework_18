# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from app.dao.genreDAO import GenreDAO


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def create(self, data):
        self.dao.create(data)

    def update(self, gid, data):
        genre = self.get_one(gid)
        genre.name = data.get('name')
        self.dao.update(genre)


    def partial_update(self, gid, data):
        genre = self.get_one(gid)
        if 'name' in data:
            genre.name = data.get('name')
        self.dao.update(genre)

    def delete(self, gid):
        self.dao.delete(gid)
