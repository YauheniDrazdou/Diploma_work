from test_onliner.pages.base_page import BasePage
from selenium.webdriver.common.by import By

LI_CATALOG = By.XPATH, "//span[@class='b-main-navigation__text'][contains(text(), 'Каталог')]"


class MainPage(BasePage):
    def catalog_link(self):
        return self.driver.find_element(*LI_CATALOG).click()

