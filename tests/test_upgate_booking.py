import allure
import requests

from helpers.api import base_url, booking_endpoint, CreateUpdateBook
from tests.test_get_bookings import id_book

update_body = CreateUpdateBook()


"""Сюда нужна авторизация, чтобы был ответ 200, а не 403
И schema"""
@allure.epic("API тесты")
@allure.story('Проверка редактирования собственного заказа')
def test_update_self_book():
    response = requests.put(
        url=base_url+booking_endpoint+"21",
        json=update_body.create_update_body_valid(
            first_name="Petr",
            last_name="Petrov",
            total_price="900",
            depositpaid_bool="True",
            checkin_yyyy_mm_dd="2025-07-05",
            checkout_yyyy_mm_dd="2025-07-10",
            additional_needs="breakfast+dinner"
        )
    )
    assert response.status_code == 403


"""Сюда нужна авторизация, чтобы был ответ 200, а не 403
И schema"""
@allure.epic("API тесты")
@allure.story('Проверка редактирования несуществующего заказа')
def test_update_non_existent_book():
    response = requests.put(
        url=base_url + booking_endpoint + "21454618416846165",
        json=update_body.create_update_body_valid(
            first_name="Petr123",
            last_name="Petrov123",
            total_price="900123",
            depositpaid_bool="True",
            checkin_yyyy_mm_dd="2025-07-05",
            checkout_yyyy_mm_dd="2025-07-10",
            additional_needs="breakfast+dinner"
        )
    )
    assert response.status_code == 403



"""Сюда нужна авторизация, чтобы был ответ 200, а не 403
И schema"""
@allure.epic("API тесты")
@allure.story('Проверка редактирования с невалидными данными, например, без поля firstname')
def test_update_non_existent_book():
    response = requests.put(
        url=base_url + booking_endpoint + "21454618416846165",
        json=update_body.create_update_body_valid(
            first_name="Petr321",
            last_name="Petrov321",
            total_price="900321",
            depositpaid_bool="True",
            checkin_yyyy_mm_dd="2025-07-05",
            checkout_yyyy_mm_dd="2025-07-10",
            additional_needs="breakfast+dinner"
        )
    )
    assert response.status_code == 403