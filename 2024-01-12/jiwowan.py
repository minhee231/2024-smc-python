from selenium import webdriver
import re
from selenium.webdriver.common.by import By
import time
import pyperclip
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver2.get('https://time.navyism.com/?host=https%3A%2F%2Fwww.nextedition.co.kr%2Fshops%2FNextedition%2520Sinlim')
driver.get('https://www.nextedition.co.kr/shops/Nextedition%20Sinlim')
print(driver2.find_element(By.ID, 'time_area').text)##잘되는지 확인

while True:                                                           #00초마다 #동작 실행함
    ttt = driver2.find_element(By.ID, 'time_area').text
    time_list= re.findall('[0-9]+',ttt)
    if time_list[5]=='00':
        resv_button = driver.find_element(By.ID,'round812')
        resv_button.click()

        name = driver.find_element(By.ID, 'name')
        pn = driver.find_element(By.ID, 'phoneNumber')
        memo = driver.find_element(By.ID,'memo')
        name.click()
        pyperclip.copy('양지환')       # 파이퍼클립은 안쓰고 send_keys 사용시 한글사용이 안될 수 있음.
        name.send_keys(Keys.CONTROL,'v')
        pn.click()
        pyperclip.copy('010-2916-3553')
        pn.send_keys(Keys.CONTROL,'v')
        memo.click()
        pyperclip.copy('가나다라마바사')
        memo.send_keys(Keys.CONTROL,'v')
        exit_button = driver.find_element(By.XPATH,'/html/body/div[7]/div/div/div[3]/button[2]')
        exit_button.click()
        break