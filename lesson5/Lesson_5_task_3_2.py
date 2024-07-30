from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driverFf = webdriver.Firefox()

try:
    count = 0
    driver.get("http://uitestingplayground.com/dynamicid")
    driverFf.get("http://uitestingplayground.com/dynamicid")
    # Наживаем на синию кнопку
    blue_batton = driver.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
    blue_batton = driverFf.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
    #Кликаем на синюю кнопку 3 раза
    for _ in range(3):
        blue_batton = driver.find_element(
            "xpath", '//button[text()="Button with Dynamic ID"]').click()
        count = count + 1
        sleep(2)
        print(count)
        blue_batton = driverFf.find_element(
            "xpath", '//button[text()="Button with Dynamic ID"]').click()
        count = count + 1
        sleep(2)
        print(count)
except Exception as ex:
        print(ex)
finally:
        driver.quit()
        driverFf.quit()
        