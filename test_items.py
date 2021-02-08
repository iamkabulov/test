from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

def test_items(browser):
    try:
        WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")))
    except NoSuchElementException:
        return False
    return True   