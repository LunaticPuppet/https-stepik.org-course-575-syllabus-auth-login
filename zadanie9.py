import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID,'input_value')
x = x_element.text
y = calc(int(x))

browser.execute_script("window.scrollBy(0, 200);")

element1 = browser.find_element(By.ID,'answer')
element1.send_keys(y)

option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
option1.click()
option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
option2.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(30)
browser.quit()
