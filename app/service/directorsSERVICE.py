# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from app.dao.directorDAO import DirectorDAO


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, did):
        return self.dao.get_one(did)

    def create(self, data):
        self.dao.create(data)

    def update(self, did, data):
        director = self.get_one(did)
        director.name = data.get('name')
        self.dao.update(director)

    def partial_update(self, did, data):
        director = self.get_one(did)
        if 'name' in data:
            director.name = data.get('name')
        self.dao.update(director)

    def delete(self, did):
        self.dao.delete(did)
