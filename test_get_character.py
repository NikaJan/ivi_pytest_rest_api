from requests.auth import HTTPBasicAuth
from pack import IviServerRequests
from pack import Character
import requests
from pack.config import ivi_user


url = 'http://rest.test.ivi.ru'
iviReq = IviServerRequests.IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
some = Character.Character(iviReq)


def test_0_reset():
    res = requests.post('http://rest.test.ivi.ru/reset', auth=HTTPBasicAuth('v.milchakova9887@gmail.com', 'hgJH768Cv23'))
    assert res.status_code == 200


def test_1_get_existing_character_check_all_fields():
    """Тест получает персонажа по имени и проверяет его поля
    """

    some.name = '3-D Man'
    res = some.read()
    code = res.code

    assert code == 200
    assert res.data[0].get('education') == 'High school graduate; military training (Chuck Chandler only)'
    assert res.data[0].get('height') == 187
    assert res.data[0].get('identity') == 'Secret'
    assert res.data[0].get('other_aliases') == 'None'
    assert res.data[0].get('universe') == 'Marvel Universe'
    assert res.data[0].get('weight') == 90.0


def test_2_no_such_name():
    """Тест получает персонажа, которого нет на сервере и проверяет ответ
    """

    some.name = '{}{}'.format(ivi_user, 2)
    res = some.read()
    code = res.code
    message = res.msg
    assert code == 200
    assert message == 'No such name'


def test_3_no_such_name_special_characters():
    """Тест Тест получает персонажа с именем спецсимволами
    """

    some.name = '%!!@#$%'
    res = some.read()
    code = res.code
    assert code == 200


def test_4_no_name():
    """Тест получает персонажа с пустым именем
    """

    some.name = ''
    res = some.read()
    code = res.code
    message = res.msg
    assert code == 404
    assert message is None


if __name__ == "__main__":
    test_0_reset()
    test_1_get_existing_character_check_all_fields()
    test_2_no_such_name()
    test_3_no_such_name_special_characters()
    test_4_no_name()
