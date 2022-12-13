from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome(r"C:\chromedriver\chromedriver.exe")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)
    # time.sleep(3)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x_element.text)

    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    # button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()
    browser.execute_script("window.scrollBy(0, 100);")
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option1.click()

    # button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()


finally:
    time.sleep(15)
    browser.quit()