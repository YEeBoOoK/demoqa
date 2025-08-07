from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class WebElement:
    def __init__(self, driver, locator = ''):
        self.driver = driver
        self.locator = locator

    def _get_by(self):
        if self.locator.startswith('//') or self.locator.startswith('.//'):
            return By.XPATH
        return By.CSS_SELECTOR

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(self._get_by(), self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

# 1. в классе компонентов создайте метод для получения текста с элементов get_text(self).
#  текст из элемента считывайте так str(self.find_element().text)

    def get_text(self):
        return str(self.find_element().text)

    def get_css_value(self, property_name):
        return self.find_element().value_of_css_property(property_name)

    def visible(self):
        return self.find_element().is_displayed()