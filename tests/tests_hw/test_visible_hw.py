import time
from pages.accordian import AccordianPage

def test_visible_accordian(browser):
    accordian_page = AccordianPage(browser)
    accordian_page.visit()

    assert accordian_page.content_section1.visible()

    accordian_page.heading_section1.click()
    time.sleep(2)
    assert not accordian_page.content_section1.visible()

def test_visible_accordian_default(browser):
    accordian_page = AccordianPage(browser)
    accordian_page.visit()

    assert not accordian_page.content1_section2.visible()
    assert not accordian_page.content2_section2.visible()
    assert not accordian_page.content_section3.visible()