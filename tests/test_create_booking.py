import json

import allure
import requests
from jsonschema.validators import validate

from helpers.api import base_url, CreateUpdateBook, booking_endpoint
from models.create_models import BookingdatesModel, BookingModel
from schemas import schema_create_book

body_create = CreateUpdateBook()



@allure.epic("API тесты")
@allure.story('Проверка создания заказа с валидными значениями')
def test_create_valid_booking():
    response = requests.post(
        url=base_url + booking_endpoint,
        json=body_create.create_update_body_valid(
            first_name="Ivan",
            last_name="Ivanov",
            total_price="564",
            depositpaid_bool="True",
            checkin_yyyy_mm_dd="2025-07-01",
            checkout_yyyy_mm_dd="2025-07-01",
            additional_needs="dinner"
        )
    )
    # response_text = BookingdatesModel(**json.loads(response.text))
    assert response.status_code == 200
    # assert response_text.checkin == "2025-07-01" # или today через импорт даты
    response_body = response.json()
    validate(response_body, schema_create_book)
    id_book = response.json()["bookingid"]
    return id_book

@allure.epic("API тесты")
@allure.story('Проверка создания заказа без обязательного поля  first_name')
def test_create_no_valid_booking():
    response = requests.post(
        url=base_url + booking_endpoint,
        json=body_create.create_body_no_firstname(
            last_name="Ivanov",
            total_price="564",
            depositpaid_bool="True",
            checkin_yyyy_mm_dd="2025-06-01",
            checkout_yyyy_mm_dd="2025-07-01",
            additional_needs="dinner"
        )
    )
    assert response.status_code == 500
