from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome(r"C:\chromedriver\chromedriver.exe")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)

    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element(By.CSS_SELECTOR, '#book')
    button.click()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x_element.text)

    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, '#solve')
    button.click()



finally:
    time.sleep(5)
    browser.quit()
    

