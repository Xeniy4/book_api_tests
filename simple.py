from datetime import date

import requests

from helpers.api import base_url, booking_endpoint

json_body = {
    "bookingid": 701,
    "booking": {
        "firstname": "arbuz",
        "lastname": "zeleniy",
        "totalprice": 3000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2019-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
}


filtered_campaigns = [['checkin'] for x in json_body["booking"]['bookingdates']]

print(filtered_campaigns)



def get_book_with_id(id):
    response_get = requests.get(
        url=base_url+booking_endpoint+f'/{id}'
    )
    print(response_get.text)

get_book_with_id(1)


