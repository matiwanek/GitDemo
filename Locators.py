from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj= Service(r"C:\Users\mateusz.iwanek\Desktop\New folder (2)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('Mateusz')
driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click
driver.find_element(By.NAME, 'email').send_keys('m.iwanek714@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456')
dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_index(0)
dropdown.select_by_visible_text('Female')
driver.find_element(By.ID, 'exampleCheck1').click()
driver.find_element(By.XPATH, '//input[@type="submit"]').click()
message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)
assert 'Success' in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys('Hello!')
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
