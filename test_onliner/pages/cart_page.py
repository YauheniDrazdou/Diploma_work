from test_onliner.pages.base_page import BasePage
from selenium.webdriver.common.by import By


TX_ITEM_IN_CART = By.XPATH, "//*[@class='cart-form__link cart-form__link_primary cart-form__link_base-alter' and @href]"


class CartPage(BasePage):

    def cart_content(self):
        cart_item = self.driver.find_element(*TX_ITEM_IN_CART)
        return cart_item.text
