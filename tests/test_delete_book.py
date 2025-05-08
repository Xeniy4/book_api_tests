import allure
from requests import delete

from helpers.api import DeleteBooks

del_book = DeleteBooks()

"""Сюда нужна авторизация, чтобы был ответ 200, а не 403
И schema"""
@allure.epic("API тесты")
@allure.story('Проверка удаления существующего заказа, id=4')
def test_delete_book():
    response = del_book.delete_book('4')
    assert response.status_code == 201


@allure.epic("API тесты")
@allure.story('Проверка удаления несуществующего заказа, id=1234567891234598')
def test_delete_non_existent_book():
    response = del_book.delete_book("1234567891234598")
    assert response.status_code == 405