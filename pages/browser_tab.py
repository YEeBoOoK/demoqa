from pages.base_page import BasePage
from components.components import WebElement

class BrowserWinPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/browser-windows'
        super().__init__(driver, self.base_url)

        self.new_tab_btn = WebElement(driver, '#tabButton')
        self.new_window_btn = WebElement(driver, '#windowButton')
        self.new_window_message_btn = WebElement(driver, '#messageWindowButton')