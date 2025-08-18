from selenium.webdriver import Keys

from pages.slider_page import SliderPage

def test_slider(browser):
    slider_page = SliderPage(browser)

    slider_page.visit()
    slider_page.slider.exist()
    slider_page.slider_input_value.exist()

    assert slider_page.slider.get_dom_attribute('value') == '25'

    while not slider_page.slider_input_value.get_dom_attribute('value') == '50':
        slider_page.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider_page.slider_input_value.get_dom_attribute('value') == '50'