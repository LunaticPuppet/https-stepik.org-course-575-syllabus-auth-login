import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element(By.ID,'input_value').text
y = calc(int(x))

answer = browser.find_element(By.ID,'answer')
answer.send_keys(y)

button2 = browser.find_element(By.CLASS_NAME, "btn-primary")
button2.click()




time.sleep(30)
browser.quit()
