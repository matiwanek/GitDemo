import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service(r"C:\Users\mateusz.iwanek\Desktop\New folder (2)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://the-internet.herokuapp.com/windows')
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT, 'Click Here').click()
windowsopen= driver.window_handles
driver.switch_to.window(windowsopen[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.switch_to.window(windowsopen[0])
assert driver.find_element(By.TAG_NAME, "h3").text