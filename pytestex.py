from selenium import webdriver
import time 
import math 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import os



link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # x = browser.find_element(By.ID, "num1").text
    # y = browser.find_element(By.ID, "num2").text
    # z = int(x) + int(y)
    # print(z)
    # select = Select(browser.find_element(By.TAG_NAME, "select"))
    # select.select_by_value(f"{z}") # ищем элемент с текстом "Python"
    
    
    # input2 = browser.find_element_by_name("lastname")
    # input2.send_keys("Hypcuk")
    # input3 = browser.find_element_by_name("email")
    # input3.send_keys("Hypcuk")
    # input4 = browser.find_element_by_id("file")
    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = os.path.join(current_dir, "sav.py")
    # input4.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    def calc(x):
         return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


  
