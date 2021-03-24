import requests

data = {
    'id': 6,
    'name': 'OPPO',
    'description': 'OPPO',
    'price': 70
}


def test_create_phone():
    url = 'http://localhost:8000/create_phone/'
    response = requests.post(url, json=data)
    print(response.text)
    print(response.ok)


if __name__ == '__main__':
    test_create_phone()
