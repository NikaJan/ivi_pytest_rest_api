import json


class IviServerResponse:
    def __init__(self, code, data):
        self.code = code
        if self.code == 200:
            json_data = json.loads(data)
            self._result = json_data["result"]
        # elif self.code == 404:
        #     self._result = 'page not found'
        else:
            self._result = None
        self.msg = None
        self.data = None


class GetResponse(IviServerResponse):
    def __init__(self, code, data):
        IviServerResponse.__init__(self, code, data)

        if self.code == 200:
            if type(self._result) == str:
                self.msg = self._result
            else:
                self.data = self._result


class PostResponse(IviServerResponse):
    def __init__(self, code, data):
        IviServerResponse.__init__(self, code, data)

        if type(self._result) == str:
            self.msg = self._result
        else:
            self.data = self._result


class DeleteResponse(IviServerResponse):
    def __init__(self, code, data):
        IviServerResponse.__init__(self, code, data)

        self.msg = self._result[0]


class PutResponse(IviServerResponse):
    def __init__(self, code, data):
        IviServerResponse.__init__(self, code, data)

        if self.code == 200:
            self.data = self._result[0]
        else:
            self.msg = 'Internal error'
