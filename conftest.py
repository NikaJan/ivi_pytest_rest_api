import pytest
from pack import IviServerRequests
from pack import Character


@pytest.fixture(scope='function')
def case_data():
    url = 'http://rest.test.ivi.ru'
    iviReq = IviServerRequests.IviServerRequests(url, 'v.milchakova9887@gmail.com', 'hgJH768Cv23')
    some = Character.Character(iviReq)
    yield some