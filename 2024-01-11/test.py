from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('http://localhost:8080/')
driver.implicitly_wait(6000)
count = 1

while True:
    box = driver.find_element(By.ID,f'Box{count}')
    box.click()
    count += 1
    # time.sleep(0.1)

