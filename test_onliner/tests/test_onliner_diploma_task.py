import allure
import pytest
from test_onliner.pages.main_page import MainPage
from test_onliner.pages.catalog_page import CatalogPage
from test_onliner.pages.item_page import ItemPage
from test_onliner.pages.cart_page import CartPage


@allure.title("Nokia item search")
@pytest.mark.smoke
def test_button_phones(driver):

    main_page = MainPage(driver)
    main_page.catalog_link()

    catalog_page = CatalogPage(driver)
    catalog_page.electronics_link()

    driver.implicitly_wait(2)
    catalog_page.mobile_devises()
    catalog_page.button_phones()
    catalog_page.manufactor_list()
    catalog_page.nokia_phone()
    driver.implicitly_wait(5)
    catalog_page.nokia_model()
    catalog_page.nokia_click()

    item_page = ItemPage(driver)
    item_title = item_page.get_item_title()
    item_page.add_to_cart()
    driver.implicitly_wait(2)
    item_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.cart_content()
    assert cart_page.cart_content() == item_title