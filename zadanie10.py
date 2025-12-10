import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter first name"]')
input1.send_keys("Ivan")
input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]')
input2.send_keys("Petrov")
input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter email"]')
input3.send_keys("test@.ru")

element4 = browser.find_element(By.ID,"file")
current_dir = r"C:\Users\Rina\Desktop"
file_path = os.path.join(current_dir, 'py sel.txt')
element4.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(300)
browser.quit()