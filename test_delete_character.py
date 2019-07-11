from requests.auth import HTTPBasicAuth
from pack import IviServerRequests
from pack import Character
import requests


def test_0_reset():
    res = requests.post('http://rest.test.ivi.ru/reset', auth=HTTPBasicAuth('v.milchakova9887@gmail.com', 'hgJH768Cv23'))
    assert res.status_code == 200


def test_1_delete_existing_character():
    """Тест удаляет существующий обьект на сервере
    """

    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests.IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    some = Character.Character(iviReq)

    some.name = 'Ivanov'
    some.education = 'High School'
    some.universe = 'Marvel'
    some.identity = 'Publicly'
    some.height = 150
    some.weight = 100
    some.other_aliases = 'None'
    res = some.create()
    code = res.code

    assert code == 200

    some.name = 'Ivanov'
    res = some.delete()
    code = res.code
    message = res.msg

    assert code == 200

    some.name = 'Ivanov'
    res = some.read()
    code = res.code

    assert code == 200
    assert res.msg == 'No such name'


def test_2_delete_not_exist_character():
    """Тест удаляет не существующий обьект на сервере
    """

    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests.IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    some = Character.Character(iviReq)

    some.name = 'Ivanov2'
    res = some.update()
    code = res.code
    assert code == 500


if __name__ == "__main__":
    test_0_reset()
    test_1_delete_existing_character()
    test_2_delete_not_exist_character()