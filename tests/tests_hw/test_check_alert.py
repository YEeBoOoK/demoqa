import time
from pages.alerts import AlertsPage

def test_check_alert(browser):
    alerts_page = AlertsPage(browser)
    alerts_page.visit()

    assert alerts_page.timer_alert_btn.exist()

    alerts_page.timer_alert_btn.click()
    time.sleep(5.1)
    assert alerts_page.alert()