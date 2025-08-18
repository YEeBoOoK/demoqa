import time
import pytest
from selenium.common import WebDriverException
from pages.modal_dialogs import ModalDialogs


def is_page_available(browser):
    try:
        modal_dialogs_page = ModalDialogs(browser)
        modal_dialogs_page.visit()
        time.sleep(2)
        if modal_dialogs_page.small_modal_btn.visible():
            return True
        return False
    except WebDriverException:
        return False

def test_check_modal(browser):
    if not is_page_available(browser):
        pytest.skip('Страница недоступна')

    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()

    modal_dialogs_page.small_modal_btn.click()
    time.sleep(1)
    assert modal_dialogs_page.modals.visible()
    modal_dialogs_page.close_small_modal.click()

    time.sleep(1)

    modal_dialogs_page.large_modal_btn.click()
    time.sleep(1)
    assert modal_dialogs_page.modals.visible()
    modal_dialogs_page.close_large_modal.click()