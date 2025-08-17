import time
from pages.web_tables_page import WebTables

def test_sort(browser):
    web_tables_page = WebTables(browser)
    web_tables_page.visit()

    columns_names = [
        web_tables_page.first_name_row,
        web_tables_page.last_name_row,
        web_tables_page.email_row,
        web_tables_page.age_row,
        web_tables_page.salary_row,
        web_tables_page.department_row
    ]

    for column_name in columns_names:
        column_name.click()
        time.sleep(1)
        assert '-sort-asc' in column_name.get_dom_attribute('class')
        time.sleep(0.5)