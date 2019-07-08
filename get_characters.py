from pack.IviServerRequests import *
from pack.Character import *
from pack.Characters import *


def test_0_reset():
    res = requests.post('http://rest.test.ivi.ru/reset', auth=HTTPBasicAuth('v.milchakova9887@gmail.com', 'hgJH768Cv23'))
    assert res.status_code == 200


# GET
def test_1_get_all_characters():
    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    chars = Characters(iviReq)
    res = chars.get()
    code = res.code
    message = res.msg
    data = res.data
    if code == 200:
        print(chars.arr)
    assert code == 200

if __name__ == "__main__":
    test_0_reset()
    test_1_get_all_characters()
