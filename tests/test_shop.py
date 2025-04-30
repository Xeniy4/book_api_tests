
import requests
from selene import browser, have
from urllib3 import request

base_url = "https://aromacode.ru/"
url_add_card = "https://aromacode.ru/product/attar-collection-sierra/"
body = {
    "sku_id": "87545",
    "product_id": "25045"
}

url_cart = "https://aromacode.ru/cart/"

def test_add_item_in_cart():
    response = requests.post(url=url_add_card, data=body)
    assert response.status_code == 200
    # cookies = response.cookies.get('PHPSESSID')
    # print(response.cookies)

    # browser.open(base_url)
    # browser.driver.add_cookie({"name": "PHPSESSID", "value": cookies})
    # browser.open(url_cart)
    # browser.element('.sku-code').should(have.text('арт.: 97545'))


def test_site():
    response = requests.post(
        url='https://www.holodilnik.ru/ajax/auth/login/',
        data= {"login": "testbk01@bk.ru", "password": "123456789-"}
    )
    assert response.status_code == 200
    print(response.text, response.status_code)