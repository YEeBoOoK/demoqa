import time
from pages.textbox_page import TextBox


def test_text_box(browser):
    textbox_page = TextBox(browser)
    textbox_page.visit()

    expected_name = 'Meow Meow Meow'
    expected_address = 'TestTown'

    textbox_page.full_name.send_keys(expected_name)
    textbox_page.current_address.send_keys(expected_address)
    textbox_page.submit.click()

    time.sleep(2)

    assert expected_name in textbox_page.name_output.get_text()
    assert expected_address in textbox_page.current_address_output.get_text()