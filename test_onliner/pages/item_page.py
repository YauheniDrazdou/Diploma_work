from test_onliner.pages.base_page import BasePage
from selenium.webdriver.common.by import By


TX_ITEM_TITLE = By.XPATH, "//*[@class='catalog-masthead__title js-nav-header']"
BN_ADD_TO_CART = By.PARTIAL_LINK_TEXT, 'В корзину'
BN_GO_TO_CART = By.XPATH, "//*[contains(text(), 'Перейти в корзину')]"


class ItemPage(BasePage):

    def get_item_title(self):
        return self.driver.find_element(*TX_ITEM_TITLE).text


    def add_to_cart(self):
        return self.driver.find_element(*BN_ADD_TO_CART).click()

    def go_to_cart(self):
        return self.driver.find_element(*BN_GO_TO_CART).click()