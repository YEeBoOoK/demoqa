import time
from selenium.webdriver.common.by import By
from pages.web_tables_page import WebTables

def test_add_edit_web_tables(browser):
    web_tables_page = WebTables(browser)
    web_tables_page.visit()

    # Проверка существования кнопки add и открытия модального окна по нажатию на кнопку
    assert web_tables_page.btn_add.visible()
    web_tables_page.btn_add.click()
    time.sleep(2)
    assert web_tables_page.modal_content.visible()

    # Проверка обязательности полей (отправка пустой формы)
    web_tables_page.submit.click()
    time.sleep(2)
    assert web_tables_page.modal_content.visible()

    # Заполнение всех полей и отправка формы
    web_tables_page.first_name.send_keys('Tester')
    web_tables_page.last_name.send_keys('Testtesteronchik')
    web_tables_page.email.send_keys('test@test.test')
    web_tables_page.age.send_keys('22')
    web_tables_page.salary.send_keys('9999999999')
    web_tables_page.department.send_keys('Cryptology')
    web_tables_page.submit.click()
    time.sleep(2)

    # Проверка, что окно закрылось и появилась новая строка в таблице
    assert not web_tables_page.modal_content.exist()
    # assert web_tables_page.new_row.visible()
    assert web_tables_page.get_row_by_email('test@test.test') is not None, 'Строка с таким email не найдена в таблице'

    # Проверка кнопки и окна редактирования
    web_tables_page.new_row_edit_btn.click()
    time.sleep(2)
    assert web_tables_page.modal_content.visible()
    assert web_tables_page.first_name.get_dom_attribute('value') == 'Tester'

    # Очистка поля имени в форме редактирования, ввод нового значения и отправка формы
    web_tables_page.first_name.clear()
    web_tables_page.first_name.send_keys('Tester2')
    web_tables_page.submit.click()
    time.sleep(2)

    # Проверка, что данные в таблице обновились, удаление записи
    assert web_tables_page.new_row_first_name.get_text() == 'Tester2'
    web_tables_page.new_row_delete_btn.click()
    time.sleep(2)

    # Проверка, что новая запись была удалена
    # assert web_tables_page.new_row.get_text().strip() == ''
    assert web_tables_page.get_row_by_email('test@test.test') is None, 'Строка не удалилась'



def test_previous_and_next(browser):
    web_tables_page = WebTables(browser)
    web_tables_page.visit()

    # Установка отображения 5 строк в таблице
    web_tables_page.select_count_of_rows.click()
    web_tables_page.count_of_rows_5.click()
    time.sleep(2)

    # Проверка, что кнопки заблокированы
    assert not web_tables_page.previous_btn.is_enabled(), 'Кнопка "Previous" должна быть отключена'
    assert not web_tables_page.next_btn.is_enabled(), 'Кнопка "Next" должна быть отключена'

    # Проверка, что клик не меняет страницу
    current_page = web_tables_page.page_number_input.get_dom_attribute('value')

    web_tables_page.previous_btn.click_force()
    assert web_tables_page.page_number_input.get_dom_attribute('value') == current_page

    web_tables_page.next_btn.click_force()
    assert web_tables_page.page_number_input.get_dom_attribute('value') == current_page

    # Заполнение всех полей и отправка формы 3 раза
    for i in range(3):
        web_tables_page.btn_add.click()
        time.sleep(1)
        web_tables_page.first_name.send_keys('Tester')
        web_tables_page.last_name.send_keys('Testtesteronchik')
        web_tables_page.email.send_keys('test@test.test')
        web_tables_page.age.send_keys('22')
        web_tables_page.salary.send_keys('9999999999')
        web_tables_page.department.send_keys('Cryptology')
        web_tables_page.submit.click()
        time.sleep(0.5)

    # Проверка пагинации
    assert web_tables_page.total_page.get_text() == '2', 'Должно быть 2 страницы'

    # Проверка перехода на вторую страницу
    assert web_tables_page.next_btn.is_enabled(), 'Кнопка "Next" должна быть активной'
    web_tables_page.next_btn.click()
    time.sleep(1)
    assert web_tables_page.page_number_input.get_dom_attribute('value') == '2'

    # Проверка перехода на первую страницу
    assert web_tables_page.previous_btn.is_enabled(), 'Кнопка "Previous" должна быть активной'
    web_tables_page.previous_btn.click()
    time.sleep(1)
    assert web_tables_page.page_number_input.get_dom_attribute('value') == '1'