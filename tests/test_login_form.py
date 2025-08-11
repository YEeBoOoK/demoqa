import time

from selenium.webdriver import Keys

from pages.form_page import FormPage

def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert not form_page.modal_dialog.exist()
    time.sleep(2)

    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    form_page.hobbies.click_force()
    form_page.current_address.send_keys('testtown')
    time.sleep(2)

    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()



# Первый вариант решения
def test_filling_in_fields_state_and_city(browser):
    form_page = FormPage(browser)
    form_page.visit()

    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    time.sleep(2)

    form_page.state_field_btn.click()
    assert form_page.state_dropdown_item_1.visible()
    form_page.state_dropdown_item_1.click()
    time.sleep(2)

    form_page.city_field_btn.click()
    assert form_page.city_dropdown_item_1.visible()
    form_page.city_dropdown_item_1.click()
    time.sleep(2)



# Второй вариант решения
def test_filling_in_fields_state_and_city_2(browser):
    form_page = FormPage(browser)
    form_page.visit()

    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    time.sleep(2)

    form_page.select_state_field.click_force()
    form_page.state_input.send_keys('NCR')
    form_page.state_input.send_keys(Keys.ENTER)
    time.sleep(2)

    form_page.select_city_field.click_force()
    form_page.city_input.send_keys('Delhi')
    form_page.city_input.send_keys(Keys.ENTER)
    time.sleep(2)

    form_page.btn_submit.click_force()
    time.sleep(2)