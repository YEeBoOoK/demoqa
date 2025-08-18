import pytest
from pages.demoqa import DemoQa

@pytest.mark.skip
def test_decor(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.h5.check_count_elements(6)

    for element in demo_qa_page.h5.find_elements():
        assert element.text != ''