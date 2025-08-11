import time
from pages.textbox_page import TextBox

def test_clear(browser):
    textbox_page = TextBox(browser)
    textbox_page.visit()

    textbox_page.full_name.send_keys('meow')
    time.sleep(2)
    textbox_page.full_name.clear()
    time.sleep(2)
    assert textbox_page.full_name.get_text() == ''