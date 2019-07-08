import json


class Character:
    """Класс персонаж"""

    def __init__(self, req):
        """Конструктор"""
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
        """
        create
        """
        data = self.to_json()
        res = self.__req.post(data)
        return res

    def read(self):
        """
        read
        """
        res = self.__req.get(self.name)
        if res.code == 200 and res.msg is None:
            self.from_json(res.data[0])

        return res

    def update(self):
        """
        update
        """
        data = self.to_json()
        return self.__req.put(self.name, data)

    def delete(self):
        """
        delete
        """
        res = self.__req.delete(self.name)
        return res

    def to_json(self):
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
        self.education = data["education"]
        self.height = data["height"]
        self.identity = data["identity"]
        self.name = data["name"]
        self.other_aliases = data["other_aliases"]
        self.universe = data["universe"]
        self.weight = data["weight"]
