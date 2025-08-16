import time
from pages.browser_tab import BrowserWinPage

def test_browser_tab(browser):
    browser_win_page = BrowserWinPage(browser)
    browser_win_page.visit()

    assert len(browser.window_handles) == 1

    browser_win_page.new_tab_btn.click()
    time.sleep(2)

    assert len(browser.window_handles) == 2

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)