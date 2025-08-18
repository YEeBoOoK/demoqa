import pytest
from pages.radio_button_page import RadioButtonPage

# @pytest.mark.skipif(True, reason='просто пропуск')
def test_decor_2(browser):
    radio_button_page = RadioButtonPage(browser)
    radio_button_page.visit()

    radio_button_page.yes_btn.click_force()
    assert radio_button_page.text.get_text() == 'You have selected Yes'

    radio_button_page.impressive_btn.click_force()
    assert radio_button_page.text.get_text() == 'You have selected Impressive'

    assert 'disabled' in radio_button_page.no_btn.get_dom_attribute('class')