"""Модуль содержит класс для работы с типом Character на сервере"""

import json


class Character:
    """Класс персонаж"""

    def __init__(self, req):
        """Конструктор

        :param IviServerRequests req: объект позволяющий отправить запросы на сервер
        """
        self.name = ""
        self.universe = ""
        self.education = ""
        self.identity = ""
        self.other_aliases = ""
        self.height = 0
        self.weight = 0
        self.__req = req
        self.__req.obj_type = 'character'

    def create(self):
        """Метод создает объект на сервере

        :return: возвращает объект содержащий ответ от сервера
        :rtype: IviServerResponse
        """
        data = self.to_json()
        res = self.__req.post(data)
        return res

    def read(self):
        """Метод читает объект с сервера

        :return: возвращает объект содержащий ответ от сервера
        :rtype: IviServerResponse
        """
        res = self.__req.get(self.name)
        if res.code == 200 and res.msg is None:
            self.from_json(res.data[0])

        return res

    def update(self):
        """Метод обновляет объект на сервере

        :return: возвращает объект содержащий ответ от сервера
        :rtype: IviServerResponse
        """
        data = self.to_json()
        return self.__req.put(self.name, data)

    def delete(self):
        """Метод удаляет данный объект с сервера

        :return: возвращает объект содержащий ответ от сервера
        :rtype: IviServerResponse
        """
        res = self.__req.delete(self.name)
        return res

    def to_json(self):
        """Метод получает JSON из данных в текущем объекте

        :return: возвращает объект содержащий ответ от сервера
        :rtype: Object
        """
        return json.JSONEncoder().encode(
            {
                "education": self.education,
                "height": self.height,
                "identity": self.identity,
                "name": self.name,
                "other_aliases": self.other_aliases,
                "universe": self.universe,
                "weight": self.weight
            }
        )

    def from_json(self, data):
        """Метод заполняет текущий объект данными из JSON

        :param Object data: объект содержащий JSON данные
        """
        self.education = data["education"]
        self.height = data["height"]
        self.identity = data["identity"]
        self.name = data["name"]
        self.other_aliases = data["other_aliases"]
        self.universe = data["universe"]
        self.weight = data["weight"]
