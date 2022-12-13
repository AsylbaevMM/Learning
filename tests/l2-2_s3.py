from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome(r"C:\chromedriver\chromedriver.exe")

try:
    browser.get(link)
    # time.sleep(3)
    x_element = browser.find_element(By.CSS_SELECTOR, '#num1')
    x = int(x_element.text)

    y_element = browser.find_element(By.CSS_SELECTOR, '#num2')
    y = int(y_element.text)
    print(x, y)

    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{x +y}']").click()

    
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()


finally:
    time.sleep(15)
    browser.quit()
