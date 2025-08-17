from pages.base_page import BasePage
from components.components import WebElement

class LinksPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/links'
        super().__init__(driver, self.base_url)

        self.home_link = WebElement(driver, '#simpleLink')
        self.home93il8_link = WebElement(driver, '#dynamicLink')
        self.created_link = WebElement(driver, '#created')
        self.no_content_link = WebElement(driver, '#no-content')
        self.moved_link = WebElement(driver, '#moved')
        self.bad_request_link = WebElement(driver, '#bad-request')
        self.unauthorized_link = WebElement(driver, '#unauthorized')
        self.forbidden_link = WebElement(driver, '#forbidden')
        self.not_found_link = WebElement(driver, '#invalid-url')