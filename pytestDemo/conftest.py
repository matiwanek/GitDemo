import pytest


@pytest.fixture()
def setup():
    print("i will be executing first")
    yield
    print('I will be executed last')
@pytest.fixture()
def dataLoad():
    print('user profile data is being created')
    return ["Mateusz", 'Iwanek', 'mateusziwanek.com']

@pytest.fixture(params=[("chrome","Mateusz"),("firefox","Iwanek"),("IE","Akademia")])
def crossBrowser(request):
    return request.param