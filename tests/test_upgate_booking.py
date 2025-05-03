import allure
import requests

from helpers.api import base_url



@allure.epic("API тесты")
@allure.story('Проверка редактирования собственного заказа')
# def test_update_self_book():
#     response = requests.put(
#         url=base_url,
#         json=
#     )

@allure.epic("API тесты")
@allure.story('Проверка редактирования несуществующего заказа')
def test_update_non_existent_book():
    pass




@allure.epic("API тесты")
@allure.story('Проверка редактирования с невалидными данными')
def test_update_non_existent_book():
    pass