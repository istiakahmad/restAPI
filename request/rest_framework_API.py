import requests

ENDPOINT = "http://127.0.0.1:8000/api/status/"


def do(method='get', data={}, id=4):
    r = requests.request(method, ENDPOINT + "?id=" + str(id), data=data)
    print(r.text)
    return r
