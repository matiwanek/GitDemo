from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = 'Mateusz'
service_obj= Service(r"C:\Users\mateusz.iwanek\Desktop\New folder (2)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element(By.CSS_SELECTOR, '#name').send_keys(name)
driver.find_element(By.CSS_SELECTOR, '#alertbtn').click()
alert = driver.switch_to.alert
alertText = alert.text
assert name in alertText
alert.accept()
print(alertText)