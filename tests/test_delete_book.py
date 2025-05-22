import logging

import allure
from allure_commons.types import Severity

from api_methods.api import DeleteBooks, response_logging

del_book = DeleteBooks()


@allure.severity(Severity.NORMAL)
@allure.tag("API")
@allure.label("owner", "Xeniy4")
@allure.suite("API-Тесты")
@allure.title('Проверка удаления существующего заказа, id=7')
def test_delete_book():
    response = del_book.delete_booking('7')
    assert response.status_code == 201
    response_logging(response=response)


@allure.severity(Severity.NORMAL)
@allure.tag("API")
@allure.label("owner", "Xeniy4")
@allure.suite("API-Тесты")
@allure.title('Проверка удаления несуществующего заказа, id=1234567891234598')
def test_delete_non_existent_book():
    response = del_book.delete_booking("1234567891234598")
    assert response.status_code == 405
    response_logging(response=response)
