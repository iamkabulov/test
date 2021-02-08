import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")      
def browser(request):
    language = request.config.getoption("language")
    if  language == "es":
        lang = "es"
        browser = webdriver.Chrome()
        browser.get(f"http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    elif language == "fr":
        lang = "fr"
        browser = webdriver.Chrome()
        browser.get(f"http://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/")
        yield browser
        browser.quit()
    else:
        raise pytest.UsageError("--language should be selected")

