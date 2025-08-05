# 2 задание
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_text_in_footer(browser):
    # a. перейти на страницу 'https://demoqa.com/'
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    # b. проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’
    assert demo_qa_page.text_in_footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.', f'Текст в подвале: {demo_qa_page.text_in_footer.get_text()}'


# 3 задание
def test_text_to_the_center(browser):
    # a. перейти на страницу 'https://demoqa.com/'
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.get_url() == 'https://demoqa.com/'

    # b. через кнопку перейти на страницу 'https://demoqa.com/elements'
    demo_qa_page.btn_elements.click()

    elements_page = ElementsPage(browser)
    assert  demo_qa_page.get_url() == 'https://demoqa.com/elements'

    # c. проверить что текст по центру == 'Please select an item from left to start practice.'
    expected_text = 'Please select an item from left to start practice.'
    actual_text = elements_page.text_on_page_elements.get_text()
    assert actual_text == expected_text, f"Ожидаемый текст: '{expected_text}', полученный: '{actual_text}'"

    text_align = elements_page.text_on_page_elements.get_css_value('text-align')
    print(f'Выравнивание текста: {text_align}')
    assert text_align == 'center', f"Текст не по центру! Выравнивание: {text_align}"