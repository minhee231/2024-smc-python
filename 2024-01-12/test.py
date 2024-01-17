from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

driver = webdriver.Chrome()
my_time = '05'

driver.get('https://time.navyism.com/?host=https%3A%2F%2Fwww.nextedition.co.kr%2Fshops%2FNextedition%2520Sinlim')


while True:
    ttt = driver.find_element(By.ID, 'time_area').text
    times = re.findall('[0-9]+',ttt)
    if times[5]==my_time:
        print(times[0],times[1],times[2],times[3],times[4],times[5])
        break

driver.get('https://www.nextedition.co.kr/shops/Nextedition%20Sinlim')
driver.implicitly_wait(6000)

for i in range(1000):
    try:
        dPdir = driver.find_element(By.ID,'round813')
        dPdir.click()

        name_element = driver.find_element(By.ID,'name')
        phoneNumber_element = driver.find_element(By.ID,'phoneNumber')
        cl = driver.find_element(By.XPATH,'/html/body/div[7]/div/div/div[3]/button[2]')

        name_element.send_keys('양지환')
        time.sleep(2)
        phoneNumber_element.send_keys('010-1234-1234')
        time.sleep(2)
        cl.click()
    except: continue