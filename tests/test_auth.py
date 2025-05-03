import json
from http.client import responses

import requests
from jsonschema.validators import validate
from pycparser.ply.yacc import token

from models.auth_model import AuthModel
from schemas import auth_user


def auth_book():
    response = requests.post(
        url="https://restful-booker.herokuapp.com/auth",
        data={
    "username" : "admin",
    "password" : "password123"
}
    )
    auth_response = AuthModel(**json.loads(response.text))
    return auth_response.token




tok = auth_book()


def test_book():
    response = requests.post(
        url="https://restful-booker.herokuapp.com/booking/2",
        headers= {
            'Cookie': f'token={tok}'
        },
        data={
    "firstname" : "James1",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    )
    assert response.status_code == 404
    print(response.headers)
