import datetime
import json
import logging

import allure
import requests
from allure_commons.types import Severity
from jsonschema.validators import validate

from api_methods.api import base_url, CreateUpdateBook, booking_endpoint
from schemas import schema_create_book

body_create = CreateUpdateBook()
today = str(datetime.date.today())


@allure.severity(Severity.NORMAL)
@allure.tag("API")
@allure.label("owner", "Xeniy4")
@allure.suite("API-Тесты")
@allure.title("Проверка создания заказа с валидными значениями")
def test_create_valid_booking():
    response = requests.post(
        url=base_url + booking_endpoint,
        json=body_create.create_update_body_valid(
            first_name="Ivan",
            last_name="Ivanov",
            total_price="564",
            depositpaid_bool="True",
            checkin_yyyy_mm_dd=f'"{today}"',
            checkout_yyyy_mm_dd="2025-07-01",
            additional_needs="dinner"
        )
    )
    assert response.status_code == 200
    assert json.loads(response.text)['booking']['bookingdates']['checkin'] == today
    assert json.loads(response.text)['booking']['additionalneeds'] == "dinner"
    response_body = response.json()
    validate(response_body, schema_create_book)
    id_book = response.json()["bookingid"]
    logging.info(response.text)
    logging.info(response.status_code)
    logging.info(response.url)
    logging.info(response.headers)
    return id_book


@allure.severity(Severity.NORMAL)
@allure.tag("API")
@allure.label("owner", "Xeniy4")
@allure.suite("API-Тесты")
@allure.title('Проверка создания заказа без обязательного поля  first_name')
def test_create_no_valid_booking():
    response = requests.post(
        url=base_url + booking_endpoint,
        json=body_create.create_update_body_no_firstname(
            last_name="Ivanov",
            total_price="564",
            depositpaid_bool="True",
            checkin_yyyy_mm_dd="2025-06-01",
            checkout_yyyy_mm_dd="2025-07-01",
            additional_needs="dinner"
        )
    )
    assert response.status_code == 500
    logging.info(response.text)
    logging.info(response.status_code)
    logging.info(response.url)
