import logging

import allure
from helpers.api import DeleteBooks

del_book = DeleteBooks()


@allure.epic("API тесты")
@allure.story('Проверка удаления существующего заказа, id=4')
def test_delete_book():
    response = del_book.delete_book('4')
    assert response.status_code == 201
    logging.info(response.text)
    logging.info(response.status_code)
    logging.info(response.url)


@allure.epic("API тесты")
@allure.story('Проверка удаления несуществующего заказа, id=1234567891234598')
def test_delete_non_existent_book():
    response = del_book.delete_book("1234567891234598")
    assert response.status_code == 405
    logging.info(response.text)
    logging.info(response.status_code)
    logging.info(response.url)