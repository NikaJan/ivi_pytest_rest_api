from requests.auth import HTTPBasicAuth
from pack import config
from pack.config import ivi_user
import requests


def test_0_reset():
    res = requests.post('http://rest.test.ivi.ru/reset', auth=HTTPBasicAuth('v.milchakova9887@gmail.com', 'hgJH768Cv23'))
    assert res.status_code == 200


def test_1_delete_existing_character(case_data):
    """Тест удаляет существующий обьект на сервере
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

    some.name = ivi_user
    res = some.delete()
    code = res.code
    assert code == 200

    some.name = ivi_user
    res = some.read()
    code = res.code
    assert code == 200
    assert res.msg == 'No such name'


def test_2_delete_not_exist_character(case_data):
    """Тест удаляет не существующий обьект на сервере
    """

    some = case_data
    some.name = '{}{}'.format(ivi_user, 2)
    res = some.update()
    code = res.code
    assert code == 500


if __name__ == "__main__":
    test_0_reset()
    test_1_delete_existing_character()
    test_2_delete_not_exist_character()