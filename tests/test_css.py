from pages.textbox_page import TextBox

def test_text_box_submit(browser):
    textbox_page = TextBox(browser)
    textbox_page.visit()

    assert textbox_page.submit.check_css('color', 'rgba(255, 255, 255, 1)')

    assert textbox_page.submit.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert textbox_page.submit.check_css('borderColor', 'rgb(0, 123, 255)')