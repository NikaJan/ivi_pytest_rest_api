import requests
from requests.auth import HTTPBasicAuth
from pack.IviServerResponse import *


class IviServerRequests:

    def __init__(self, url, login, password):
        self._url = url
        self._login = login
        self._password = password
        self._headers = {'content-type': 'application/json'}
        self._auth = HTTPBasicAuth(login, password)

    def get(self, name=None):
        url = self._url + '/' + self.obj_type
        if name is not None:
            url += '/' + name
        response = requests.get(url, auth=self._auth, headers=self._headers)
        return GetResponse(response.status_code, response.text)

    def post(self, data):
        url = self._url + '/' + self.obj_type
        response = requests.post(url, auth=self._auth, data=data, headers=self._headers)
        # TODO дополнительно логирование
        return PostResponse(response.status_code, response.text)

    def put(self, name, data):
        url = self._url + '/' + self.obj_type + '/' + name
        response = requests.put(url, auth=self._auth, data=data, headers=self._headers)
        return PutResponse(response.status_code, response.text)

    def delete(self, name):
        url = self._url + '/' + self.obj_type + '/' + name
        response = requests.delete(url, auth=self._auth, headers=self._headers)
        res = DeleteResponse(response.status_code, response.text)
        # тут можно обработать идентификатор удаленного объекта
        if "is deleted" in res.msg:
            res.msg = None

        return res
