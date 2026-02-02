import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC


with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/alerts")
    wait = WebDriverWait(driver,10)
    action = ActionChains(driver)
    alert = Alert(driver)
    print(driver.title)
    driver.find_element(By.ID,"prompt").click()
    wait.until(EC.alert_is_present())
    print(alert.text)
    alert.send_keys("Awesome")
    alert.accept()

