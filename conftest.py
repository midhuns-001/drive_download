import pytest, json, os

@pytest.fixture(scope="module", autouse=True)
def test_data_dict()->dict:
    with open('test_data/test_data.json', 'r') as f:
        test_data = json.load(f)
    if os.path.exists(test_data['VALID_DESTINATION']):
        os.remove(test_data['VALID_DESTINATION'])

    yield test_data

@pytest.fixture(scope="module", autouse=True)
def cred_file()->str:
    return os.path.join('config','cred.json')

@pytest.fixture(scope="module", autouse=True)
def invalid_cred_file()->str:
    return os.path.join('config','invalid_cred.json')