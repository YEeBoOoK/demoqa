from pages.base_page import BasePage
from components.components import WebElement

class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.user_form = WebElement(driver, '#userForm')

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')

        self.hobbies = WebElement(driver, '#hobbies-checkbox-1')
        self.current_address = WebElement(driver, '#currentAddress')

        # Переменные для первого варианта решения
        self.state_field_btn = WebElement(driver, '#state > div > div.css-1wy0on6')
        self.city_field_btn = WebElement(driver, '#city > div > div.css-1wy0on6 > div')

        self.state_dropdown_item_1 = WebElement(driver, '#react-select-3-option-0')
        self.city_dropdown_item_1 = WebElement(driver, '#react-select-4-option-0')

        # Переменные для второго варианта решения
        self.select_state_field = WebElement(driver, '#state')
        self.select_city_field = WebElement(driver, '#city')

        self.state_input = WebElement(driver, '#react-select-3-input')
        self.city_input = WebElement(driver, '#react-select-4-input')