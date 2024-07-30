from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driverFf = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")
    driverFf.get("http://the-internet.herokuapp.com/login")
    input_name = driver.find_element(By.ID, "username").send_keys("tomsmith")
    input_name = driverFf.find_element(By.ID, "username").send_keys("tomsmith")
    sleep(1)
    input_pass = driver.find_element(
           By.ID, "password").send_keys("SuperSecretPassword!")
    input_pass = driverFf.find_element(
           By.ID, "password").send_keys("SuperSecretPassword!")
    sleep(1)
    button = driver.find_element(By.TAG_NAME, "button").click()
    button = driverFf.find_element(By.TAG_NAME, "button").click()
    sleep(2)
except Exception as ex:
        print(ex)
finally:
        driver.quit()
        driverFf.quit()