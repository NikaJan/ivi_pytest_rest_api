from requests.auth import HTTPBasicAuth
from pack import IviServerRequests
from pack import Character
import os
import requests
import json



def test_0_reset():
    res = requests.post('http://rest.test.ivi.ru/reset', auth=HTTPBasicAuth('v.milchakova9887@gmail.com', 'hgJH768Cv23'))
    assert res.status_code == 200


def test_1_update_existing_character():
    """Тест обновляет существующего персонажа на сервере
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
    some.education = 'High School2'
    some.universe = 'Marvel2'
    some.identity = 'Publicly2'
    some.height = 155
    some.weight = 105
    some.other_aliases = 'True'
    res = some.update()
    code2 = res.code
    message = res.msg

    assert code2 == 200
    assert res.data.get('education') == 'High School2'
    assert res.data.get('height') == 155
    assert res.data.get('weight') == 105
    assert res.data.get('identity') == 'Publicly2'
    assert res.data.get('other_aliases') == 'True'
    assert res.data.get('universe') == 'Marvel2'


def test_2_update_not_exist_character():
    """Тест обновляет несуществующего персонажа на сервере
    """

    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests.IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    some = Character.Character(iviReq)

    some.name = 'Ivanov2'
    some.education = 'High School'
    some.universe = 'Marvel'
    some.identity = 'Publicly'
    some.height = 150
    some.weight = 100
    some.other_aliases = 'None'
    res = some.update()
    code = res.code

    assert code == 500


def test_3_merge_type_fields():
    """Тест обновляет персонажа с измененными типами полей
    """

    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests.IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    some = Character.Character(iviReq)

    some.name = 'Ivanov'
    some.education = 456
    some.universe = 678
    some.identity = 890
    some.height = 'to big'
    some.weight = 'to fat'
    some.other_aliases = 1
    res = some.update()
    code = res.code

    assert code == 200
    assert res.data.get('education') == 456
    assert res.data.get('height') == 'to big'
    assert res.data.get('weight') == 'to fat'
    assert res.data.get('identity') == 890
    assert res.data.get('other_aliases') == 1
    assert res.data.get('universe') == 678


def test_4_empty_fields():
    """Тест обновляет персонажа с пустыми полями
    """

    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests.IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    some = Character.Character(iviReq)

    some.name = 'Ivanov'
    some.education = ''
    some.universe = ''
    some.identity = ''
    some.height = 0
    some.weight = 0
    some.other_aliases = ''
    res = some.update()
    code = res.code

    assert code == 200
    assert res.data.get('education') == ''
    assert res.data.get('height') == 0
    assert res.data.get('weight') == 0
    assert res.data.get('identity') == ''
    assert res.data.get('other_aliases') == ''
    assert res.data.get('universe') == ''


def test_5_too_big_fields():
    """Тест обновляет персонажа большими значениями полей
    """

    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests.IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    some = Character.Character(iviReq)

    with open('lorem', 'r') as file:
        data = file.read().replace('\n', '')

    with open('ints', 'r') as file:
        ints = file.read().replace('\n', '')

    some.name = 'Ivanov'
    some.education = data
    some.universe = data
    some.identity = data
    some.height = ints
    some.weight = ints
    some.other_aliases = data
    res = some.update()
    code = res.code

    assert code == 200
    assert res.data.get('education') == data
    assert res.data.get('height') == ints
    assert res.data.get('weight') == ints
    assert res.data.get('identity') == data
    assert res.data.get('other_aliases') == data
    assert res.data.get('universe') == data


def test_6_update_character_and_check_get():
    """Тест обновляет персонажа и проверяет через get, обновился ли он
    """

    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests.IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    some = Character.Character(iviReq)
    some.name = 'Ivanov'
    some.education = 'High School 1'
    some.universe = 'Marvel 1'
    some.identity = 'Publicly 1'
    some.height = 160
    some.weight = 110
    some.other_aliases = 'False'
    res = some.update()
    code = res.code

    assert code == 200

    some.name = 'Ivanov'
    res = some.read()
    code = res.code

    assert code == 200
    assert res.data[0].get('education') == 'High School 1'
    assert res.data[0].get('height') == 160
    assert res.data[0].get('identity') == 'Publicly 1'
    assert res.data[0].get('other_aliases') == 'False'
    assert res.data[0].get('universe') == 'Marvel 1'
    assert res.data[0].get('weight') == 110


def test_7_update_fields_not_exist():
    """Тест обновляет персонажа несуществующими полями
    """

    url = "http://rest.test.ivi.ru/character/Ivanov"
    root_dir = os.path.abspath(os.curdir)
    file = open(root_dir + "\\" + "not_exist_fields.json")
    json_input = file.read()
    json_request = json.loads(json_input)
    headers = {'content-type': 'application/json'}
    response = requests.put(url,
                            auth=HTTPBasicAuth('v.milchakova9887@gmail.com', 'hgJH768Cv23'),
                            data=json.dumps(json_request),
                            headers=headers)
    assert response.status_code == 500


if __name__ == "__main__":
    test_0_reset()
    test_1_update_existing_character()
    test_2_update_not_exist_character()
    test_3_merge_type_fields()
    test_4_empty_fields()
    test_5_too_big_fields()
    test_6_update_character_and_check_get()
    test_7_update_fields_not_exist()