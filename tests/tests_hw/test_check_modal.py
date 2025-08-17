import time
from pages.modal_dialogs import ModalDialogs

def test_check_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()

    modal_dialogs_page.small_modal_btn.click()
    time.sleep(2)
    modal_dialogs_page.alert()
    modal_dialogs_page.close_small_modal.click()

    modal_dialogs_page.large_modal_btn.click()
    time.sleep(2)
    modal_dialogs_page.alert()
    modal_dialogs_page.close_large_modal.click()