import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service(r"C:\Users\mateusz.iwanek\Desktop\New folder (2)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')

driver.find_element(By.CSS_SELECTOR, 'th:nth-child(1) span:nth-child(1)').click()
driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
veggienames = [a.text for a in driver.find_elements(By.XPATH, '//tbody/tr/td[1]')]
assert veggienames == sorted(veggienames)
