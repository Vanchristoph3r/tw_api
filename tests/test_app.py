import falcon
from server.app import api
from falcon import testing
import pytest

@pytest.fixture
def client():
    return testing.TestClient(api)

def test_get_tweets(client):
    response = client.simulate_get('/users/lacasadepapel')
    result_doc = response.json

    assert type(result_doc) == list
    assert response.status == falcon.HTTP_OK

def test_get_tweets(client):
    response = client.simulate_get('/users/lacasadepapel?limit=10')
    result_doc = response.json

    assert type(result_doc) == list
    assert response.status == falcon.HTTP_OK

def test_fail_get_tweets(client):
    doc = {'title': 'Invalid parameter in endpoint'}
    response = client.simulate_get('/users/lacasadepapel?limit=jsjs')
    result_doc = response.json
    print(falcon.HTTP_OK)

    assert result_doc == doc
    assert response.status == falcon.HTTP_BAD_REQUEST


def test_get_hashtag(client):
    response = client.simulate_get('/hashtags/dogs')
    result_doc = response.json

    assert type(result_doc) == list
    assert response.status == falcon.HTTP_OK

def test_fail_get_hashtag(client):
    doc = {'title': 'Invalid parameter in endpoint'}
    response = client.simulate_get('/hashtags/dogs?limit=jsjs')
    result_doc = response.json
    print(falcon.HTTP_OK)

    assert result_doc == doc
    assert response.status == falcon.HTTP_BAD_REQUEST