import allure
import requests
from jsonschema.validators import validate

from helpers.api import base_url, CreateUpdateBook, booking_endpoint, GetBooks
from schemas import schema_get_book

create_book = CreateUpdateBook()
id_book = create_book.create_valid_booking()
id_book = str(id_book)
get_book = GetBooks()



@allure.epic("API тесты")
@allure.story('Проверка поиска ранее созданного нами заказа')
def test_get_booking_ids_from_create_book():
    create_book.create_valid_booking()
    response = requests.get(
        url=base_url+booking_endpoint+id_book
        # params=id_book
    )
    assert response.status_code == 200
    response_body = response.json()
    validate(response_body, schema_get_book)


@allure.epic("API тесты")
@allure.story('Проверка поиска существующего заказа, id = 1')
def test_get_random_booking_ids():
    response_get = get_book.get_book_with_id(1)
    assert response_get.status_code == 200
    response_body = response_get.json()
    validate(response_body, schema_get_book)


@allure.epic("API тесты")
@allure.story('Проверка поиска несуществующего заказа, id = 123456789123')
def test_gen_non_existent_id():
    response_get = get_book.get_book_with_id(123456789123)
    assert response_get.status_code == 404



