from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome(r"C:\chromedriver\chromedriver.exe")

try:
    browser.get(link)
    time.sleep(3)
    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')

    x = x_element.get_attribute("valuex")

    
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option1.click()

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    time.sleep(15)
    browser.quit()