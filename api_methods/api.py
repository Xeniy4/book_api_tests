import json
import logging
import os

import pytest
import requests
from dotenv import load_dotenv

from models.auth_models import AuthModel
from models.create_models import CreateModel

load_dotenv()

username = os.getenv("BOOKER_USERNAME")
password = os.getenv("BOOKER_PASSWORD")

base_url = "https://restful-booker.herokuapp.com"
booking_endpoint = "/booking/"


def auth_booking():
    response = requests.post(
        url=base_url + "/auth",
        data={
        "username": username,
        "password": password
    }
    )
    auth_response = AuthModel(**json.loads(response.text))
    return auth_response.token


response_token = auth_booking()


class CreateUpdateBook:
    def create_update_body_valid(self, first_name, last_name, total_price, depositpaid_bool, checkin_yyyy_mm_dd,
                                 checkout_yyyy_mm_dd, additional_needs):
        boby_create_update = {
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
        return boby_create_update

    def create_update_body_no_firstname(self, last_name, total_price, depositpaid_bool, checkin_yyyy_mm_dd,
                                        checkout_yyyy_mm_dd, additional_needs):
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

    def create_valid_booking(self):
        response = requests.post(
            url=base_url + booking_endpoint,
            json=self.create_update_body_valid(
                first_name="Ivan",
                last_name="Ivanov",
                total_price="564",
                depositpaid_bool="True",
                checkin_yyyy_mm_dd="2025-07-01",
                checkout_yyyy_mm_dd="2025-07-01",
                additional_needs="dinner"
            )
        )
        id_book = CreateModel(**json.loads(response.text))
        return id_book.bookingid


class GetBooks:
    def get_booking_with_id(self, ids):
        response_get = requests.get(
            url=base_url + booking_endpoint + str(ids)
        )
        return response_get


class DeleteBooks:
    def delete_booking(self, ids):
        response = requests.delete(
            url=base_url + booking_endpoint + str(ids),
            headers={
                'Cookie': f'token={response_token}'
            }
        )
        return response

#
# class ResponseLogging:
#     @pytest.mark.parametrize("response", ["text", "status_code", "url"])
#     def response_logging(self, **kwargs):
#         logging.info(kwargs.text)
#         return logging