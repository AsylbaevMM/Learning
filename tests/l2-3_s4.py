from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome(r"C:\chromedriver\chromedriver.exe")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x_element.text)

    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()