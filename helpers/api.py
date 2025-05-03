import json
import requests
from models.auth_models import AuthModel
from dotenv import load_dotenv
import os
load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

base_url = "https://restful-booker.herokuapp.com"
auth_endpoint = "/auth"
create_endpoint = "/booking"
body_auth = {
    "username" : username,
    "password" : password
}

def auth_book():
    response = requests.post(
        url=base_url+auth_endpoint,
        data=body_auth
    )
    auth_response = AuthModel(**json.loads(response.text))
    return auth_response.token



class CreateBook:
    def create_body_valid(self, first_name, last_name, total_price, depositpaid_bool, checkin_yyyy_mm_dd, checkout_yyyy_mm_dd, additional_needs):
        boby_create = {
            "firstname": first_name,
            "lastname": last_name,
            "totalprice": total_price,
            "depositpaid": depositpaid_bool,
            "bookingdates": {
                "checkin": checkin_yyyy_mm_dd,
                "checkout": checkout_yyyy_mm_dd
            },
            "additionalneeds": additional_needs
        }
        return boby_create

    def create_body_no_valid(self, last_name, total_price, depositpaid_bool, checkin_yyyy_mm_dd, checkout_yyyy_mm_dd, additional_needs):
        boby_create = {
            "lastname": last_name,
            "totalprice": total_price,
            "depositpaid": depositpaid_bool,
            "bookingdates": {
                "checkin": checkin_yyyy_mm_dd,
                "checkout": checkout_yyyy_mm_dd
            },
            "additionalneeds": additional_needs
        }
        return boby_create


