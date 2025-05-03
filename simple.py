from datetime import date

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