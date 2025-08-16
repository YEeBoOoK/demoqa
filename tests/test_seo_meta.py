import time
from pages.accordian import AccordianPage
from pages.alerts import AlertsPage
from pages.browser_tab import BrowserWinPage
from pages.demoqa import DemoQa
import pytest

@pytest.mark.parametrize('pages', [AccordianPage, AlertsPage, BrowserWinPage, DemoQa])

def test_check_title_all_page(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'