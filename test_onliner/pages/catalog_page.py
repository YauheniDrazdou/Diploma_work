from test_onliner.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LI_ELECTRONICS = By.XPATH, "//span[contains(text(), 'Электроника')]"
LI_MOBILE_DEVISES = By.XPATH, "//div[contains(text(), 'Мобильные телефоны и аксессуары')]"
LI_BUTTON_PHONES = By.XPATH, "//span[contains(text(), 'Кнопочные телефоны')]"
FD_MANUFACTORS = By.XPATH, "//div[@class='catalog-form__field']//div[@class='input-style__real']"
FD_NOKIA_PHONE = By.XPATH, "//div[contains(text(), 'Nokia')]"
LI_NOKIA_MODEL = By.XPATH, "//*[contains(text(), 'Кнопочный телефон Nokia 3310')]"



class CatalogPage(BasePage):

    def electronics_link(self):
        return self.driver.find_element(*LI_ELECTRONICS).click()


    def mobile_devises(self):
        return self.driver.find_element(*LI_MOBILE_DEVISES).click()

    def button_phones(self):
        return self.driver.find_element(*LI_BUTTON_PHONES).click()

    def manufactor_list(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*FD_MANUFACTORS)
        action.move_to_element(element).click().perform()

    def nokia_phone(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*FD_NOKIA_PHONE)
        action.scroll_to_element(element).click().perform()

    def nokia_model(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*LI_NOKIA_MODEL)
        action.scroll_to_element(element).perform()

    def nokia_click(self):
        return self.driver.find_element(*LI_NOKIA_MODEL).click()








