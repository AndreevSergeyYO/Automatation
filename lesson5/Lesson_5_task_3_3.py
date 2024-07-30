from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driverFf = webdriver.Firefox()

try:
    driver.get("http://uitestingplayground.com/classattr")
    driverFf.get("http://uitestingplayground.com/classattr")
    # Запускаем скрипт 3 раза
    for _ in range(3):
        blue_batton = driver.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_batton.click()
        blue_batton = driverFf.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_batton.click()
        sleep(2)
        #Кликаем на ок в модальном окне
        driver.switch_to.alert.accept()
        driverFf.switch_to.alert.accept()
except Exception as ex:
        print(ex)
finally:
        driver.quit()
        driverFf.quit()
        