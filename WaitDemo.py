import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj= Service(r"C:\Users\mateusz.iwanek\Desktop\New folder (2)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/seleniumPractise/')

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys('ber')
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
resultslist = []
time.sleep(2)
for result in results:
    resultslist.append(result.find_element(By.CSS_SELECTOR, ".product-name").text)
print(resultslist)
for result in results:
    result.find_element(By.XPATH, "div/button").click()
driver.find_element(By.XPATH, "//div[@class='cart']/a[4]").click()
driver.find_element(By.XPATH, "//div[@class='cart']/div[2]/div[2]/button").click()
driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo')))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
products = driver.find_elements(By.XPATH, "//td[5]/p")

suma = 0
for product in products:
    suma = suma + int(product.text)
print(suma)
assert str(suma) == driver.find_element(By.CSS_SELECTOR, ".totAmt").text
assert float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text) > float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)