
class Characters:
    def __init__(self, req):
        self.arr = []
        self.__req = req;
        self.__req.obj_type = 'characters'

    def get(self):
        res = self.__req.get()
        if res.code == 200:
            self.arr = res.data
        return res
