import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service(r"C:\Users\mateusz.iwanek\Desktop\New folder (2)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://the-internet.herokuapp.com/iframe')

driver.switch_to.frame('mce_0_ifr')
time.sleep(2)
driver.find_element(By.ID, 'tinymce').clear()
driver.find_element(By.ID, 'tinymce').send_keys('My name is Mateusz')
driver.switch_to.default_content()
print (driver.find_element(By.TAG_NAME, 'h3').text)

