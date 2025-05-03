import json
import requests
from jsonschema.validators import validate

from helpers.api import auth_book
from schemas import schema_auth_user
from models.auth_models import AuthModel


response_token = auth_book()

def test_book():
    response = requests.post(
        url="https://restful-booker.herokuapp.com/booking/2",
        headers= {
            'Cookie': f'token={response_token}'
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
