from selenium.webdriver.common.by import By
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

        self.modal_content = WebElement(driver, 'div.modal-content')
        self.submit = WebElement(driver, '#submit')

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')

        self.new_row = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div')
        self.new_row_edit_btn = WebElement(driver, '#edit-record-4')
        self.new_row_delete_btn = WebElement(driver, '#delete-record-4')
        self.new_row_first_name = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')


        self.select_count_of_rows = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select')
        self.count_of_rows_5 = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select > option:nth-child(1)')

        self.previous_btn = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button')
        self.next_btn = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')

        self.page_number_input = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > div > input[type=number]')
        self.total_page = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > span')

    def get_row_by_email(self, email):
        rows = self.driver.find_elements(By.CSS_SELECTOR, 'div.rt-tbody > div.rt-tr-group')
        for row in rows:
            if email in row.text:
                return WebElement(self.driver, f'//div[@class="rt-tbody"]//div[contains(text(), "{email}")]/ancestor::div[@role="row"]', 'xpath')
        return None