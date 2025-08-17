import time
from pages.links_page import LinksPage

def test_window_tab(browser):
    links_page = LinksPage(browser)
    links_page.visit()
    links_page.home_link.exist()
    assert links_page.home_link.get_text() == 'Home'
    assert links_page.home_link.get_dom_attribute('href') == 'https://demoqa.com'
    links_page.home_link.click()
    time.sleep(1)
    assert len(browser.window_handles) == 2
    time.sleep(1)