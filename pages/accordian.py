from pages.base_page import BasePage
from components.components import WebElement

class AccordianPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.heading = WebElement(driver, '#accordianContainer > h1')

        self.heading_section1 = WebElement(driver, '#section1Heading')
        self.content_section1 = WebElement(driver, '#section1Content > p')

        self.heading_section2 = WebElement(driver, '#section2Heading')
        self.content1_section2 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.content2_section2 = WebElement(driver, '#section2Content > p:nth-child(2)')

        self.heading_section3 = WebElement(driver, '#section3Heading')
        self.content_section3 = WebElement(driver, '#section3Content > p')