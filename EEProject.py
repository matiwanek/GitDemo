
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')

service_obj= Service(r"C:\Users\mateusz.iwanek\Desktop\New folder (2)\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.close()

driver.find_element(By.LINK_TEXT, 'Shop').click()
elements = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for el in elements:
    productName = el.find_element(By.XPATH, "div/h4/a").text
    if productName == 'Samsung Note 8':
        el.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
driver.find_element(By.ID, 'country').send_keys('Pol')
driver.find_element(By.XPATH, "//div[@class='suggestions']/ul/li/a").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, ".btn-lg").click()
check = driver.find_element(By.CSS_SELECTOR, '.alert-dismissible').text
assert 'Success!' in check