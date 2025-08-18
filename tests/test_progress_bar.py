import time
from pages.progress_bar_page import ProgressBar

def test_progress_bar(browser):
    progress_bar_page = ProgressBar(browser)
    progress_bar_page.visit()
    time.sleep(2)

    progress_bar_page.start_stop_btn.click()

    # while not progress_bar_page.progress.get_dom_attribute('aria-valuenow') == '51':
    #     time.sleep(0.1)
    #
    # progress_bar_page.start_stop_btn.click()

    while True:
        if progress_bar_page.progress.get_dom_attribute('aria-valuenow') == '51':
            progress_bar_page.start_stop_btn.click()
            break

    time.sleep(2)