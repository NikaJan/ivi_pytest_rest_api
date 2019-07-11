from requests.auth import HTTPBasicAuth
import os
import requests
import json
from pack import config
from pack.config import ivi_user


def test_0_reset():
    res = requests.post('http://rest.test.ivi.ru/reset', auth=HTTPBasicAuth('v.milchakova9887@gmail.com', 'hgJH768Cv23'))
    assert res.status_code == 200


def test_1_create_new_character_and_get(case_data):
    """Тест создает персонажа, проверяет ответ
    """

    some = case_data
    some.name = ivi_user
    some.education = config.get_random_str()
    some.universe = config.get_random_str()
    some.identity = config.get_random_str()
    some.height = config.get_random_int()
    some.weight = config.get_random_int()
    some.other_aliases = config.get_random_str()
    res = some.create()
    code = res.code

    assert code == 200
    assert res.data.get("name") == ivi_user
    assert res.data.get('education') == some.education
    assert res.data.get('other_aliases') == some.other_aliases

    some.name = ivi_user
    res = some.read()
    code = res.code

    assert code == 200
    assert res.data[0].get('height') == some.height
    assert res.data[0].get('identity') == some.identity
    assert res.data[0].get('universe') == some.universe
    assert res.data[0].get('weight') == some.weight


def test_2_create_already_exists(case_data):
    """Тест создает персонажа, который уже существует
    """

    some = case_data
    some.name = ivi_user
    some.education = config.get_random_str()
    some.universe = config.get_random_str()
    some.identity = config.get_random_str()
    some.height = config.get_random_int()
    some.weight = config.get_random_int()
    some.other_aliases = config.get_random_str()
    res = some.create()
    code = res.code
    message = res.msg
    assert code == 200
    assert message == "Ivanov is already exists"


def test_3_merge_type_fields(case_data):
    """Тест создает персонажа с измененным типом полей
    """
    some = case_data
    some.name = config.get_random_int()
    some.education = config.get_random_int()
    some.universe = config.get_random_int()
    some.identity = config.get_random_int()
    some.height = config.get_random_str()
    some.weight = config.get_random_str()
    some.other_aliases = config.get_random_int()
    res = some.create()
    code = res.code
    assert code == 200
    assert res.data.get("name") == some.name
    assert res.data.get('education') == some.education
    assert res.data.get('height') == some.height
    assert res.data.get('weight') == some.weight
    assert res.data.get('identity') == some.identity
    assert res.data.get('other_aliases') == some.other_aliases
    assert res.data.get('universe') == some.universe


def test_4_empty_fields(case_data):
    """Тест создает персонажа с пустыми полями
    """

    some = case_data
    some.name = ''
    some.education = ''
    some.universe = ''
    some.identity = ''
    some.height = 0
    some.weight = 0
    some.other_aliases = ''
    res = some.create()
    code = res.code
    assert code == 200
    assert res.data.get("name") == ''
    assert res.data.get('education') == ''
    assert res.data.get('height') == 0
    assert res.data.get('weight') == 0
    assert res.data.get('identity') == ''
    assert res.data.get('other_aliases') == ''
    assert res.data.get('universe') == ''


def test_5_too_big_fields(case_data):
    """Тест создает персонажа с полями с большим обьемом данных
    """

    with open('lorem', 'r') as file:
        data = file.read().replace('\n', '')
    with open('ints', 'r') as file:
        ints = file.read().replace('\n', '')
    some = case_data
    some.name = data
    some.education = data
    some.universe = data
    some.identity = data
    some.height = ints
    some.weight = ints
    some.other_aliases = data
    res = some.create()
    code = res.code
    assert code == 200
    assert res.data.get("name") == data
    assert res.data.get('education') == data
    assert res.data.get('height') == ints
    assert res.data.get('weight') == ints
    assert res.data.get('identity') == data
    assert res.data.get('other_aliases') == data
    assert res.data.get('universe') == data


def test_6_create_fields_not_exist():
    """Тест создает персонажа с измененными названиями полей
    """

    url = "http://rest.test.ivi.ru/character"
    file = open(os.path.join(os.path.abspath(os.curdir), "not_exist_fields.json"))
    json_input = file.read()
    json_request = json.loads(json_input)
    headers = {'content-type': 'application/json'}
    response = requests.post(url,
                            auth=HTTPBasicAuth('v.milchakova9887@gmail.com', 'hgJH768Cv23'),
                            data=json.dumps(json_request),
                            headers=headers)
    assert response.status_code == 500


if __name__ == "__main__":
    test_0_reset()
    test_1_create_new_character_and_get()
    test_2_create_already_exists()
    test_3_merge_type_fields()
    test_4_empty_fields()
    test_5_too_big_fields()
    test_6_create_fields_not_exist()