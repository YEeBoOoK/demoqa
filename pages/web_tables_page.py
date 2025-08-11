from pages.base_page import BasePage
from components.components import WebElement

class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.title = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > h1')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.search_input = WebElement(driver, '#searchBox')
        self.btn_delete_row = WebElement(driver, '[id^="delete-record-"]')
        self.no_data = WebElement(driver, 'div.rt-noData')