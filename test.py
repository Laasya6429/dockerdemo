import app 
def test_hello():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Hello Devops'}

def test_about():
    client = app.app.test_client()
    response = client.get('/about')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'This is about page'}