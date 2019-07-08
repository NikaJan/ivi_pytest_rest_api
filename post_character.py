from pack.IviServerRequests import *
from pack.Character import *
from pack.Characters import *


def test_0_reset():
    res = requests.post('http://rest.test.ivi.ru/reset', auth=HTTPBasicAuth('v.milchakova9887@gmail.com', 'hgJH768Cv23'))
    assert res.status_code == 200


#POST
def test_1_create_new_character():
    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    some = Character(iviReq)

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
    assert res.data.get("name") == 'Ivanov'
    assert res.data.get('education') == 'High School'
    assert res.data.get('height') == 150
    assert res.data.get('weight') == 100
    assert res.data.get('identity') == 'Publicly'
    assert res.data.get('other_aliases') == 'None'
    assert res.data.get('universe') == 'Marvel'



#POST
def test_2_create_already_exists():
    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    some = Character(iviReq)

    some.name = 'Ivanov'
    some.education = 'High School'
    some.universe = 'Marvel'
    some.identity = 'Publicly'
    some.height = 150
    some.weight = 100
    some.other_aliases = 'None'
    res = some.create()
    code = res.code
    message = res.msg

    assert code == 200
    assert message == "Ivanov is already exists"


#POST
def test_3_merge_type_fields():
    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    some = Character(iviReq)

    some.name = 123
    some.education = 456
    some.universe = 678
    some.identity = 890
    some.height = 'to big'
    some.weight = 'to fat'
    some.other_aliases = 1
    res = some.create()
    code = res.code

    assert code == 200
    assert res.data.get("name") == 123
    assert res.data.get('education') == 456
    assert res.data.get('height') == 'to big'
    assert res.data.get('weight') == 'to fat'
    assert res.data.get('identity') == 890
    assert res.data.get('other_aliases') == 1
    assert res.data.get('universe') == 678


#POST
def test_4_empty_fields():
    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    some = Character(iviReq)

    some.name = ''
    some.education = ''
    some.universe = ''
    some.identity = ''
    some.height = 0
    some.weight = 0
    some.other_aliases = ''
    res = some.create()
    code = res.code
    message = res.msg

    assert code == 200


# POST
def test_5_too_big_fields():
    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    some = Character(iviReq)

    with open('lorem', 'r') as file:
        data = file.read().replace('\n', '')

    with open('ints', 'r') as file:
        ints = file.read().replace('\n', '')

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


#POST
def test_6_create_characte_and_check_get():
    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    some = Character(iviReq)

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


if __name__ == "__main__":
    test_0_reset()
    # test_1_create_new_character()
    # test_2_create_already_exists()
    # test_3_merge_type_fields()
    test_4_empty_fields()
    # test_5_too_big_fields()
