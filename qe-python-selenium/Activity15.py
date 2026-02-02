    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 20)
    driver.get("https://training-support.net/webelements/dynamic-attributes")
    
    print(driver.title)

    name_field = driver.find_element(By.XPATH, "//input[@placeholder='Full name']")
    email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
    date_field = driver.find_element(By.XPATH, "//input[@type='date']")
    message_field = driver.find_element(By.XPATH, "//textarea")

    name_field.send_keys("Utsav Sharma")
    email_field.send_keys("abc.xyz@pqr.com")
    
    date_field.send_keys("2026-05-15")
    
    message_field.send_keys("thoota")

    submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_btn.click()

    confirmation = wait.until(EC.visibility_of_element_located((By.ID, "action-confirmation")))
    print(f"Confirmation Message: {confirmation.text}")
   