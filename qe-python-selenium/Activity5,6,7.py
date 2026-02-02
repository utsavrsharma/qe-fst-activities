from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Firefox() as driver:
    driver .get("https://training-support.net/webelements/dynamic-controls")
    print(driver.title)
# Activity 7  
    # checkbox = driver.find_element(By.ID, "checkbox")
    # print(checkbox.is_displayed())
    # enable_button = driver.find_element(By.XPATH,"//button[text()='Enable Input']")
    # print(enable_button.click())
    # text_field = driver.find_element(By.ID,"textInput")
    # print(text_field.is_enabled())

 # Activity 5 
    # checkbox = driver.find_element(By.ID, "checkbox")
    # print(checkbox.is_displayed())
    # Remove_checkbox_button = driver.find_element(By.XPATH,"//button[text()='Toggle Checkbox']")
    # print(Remove_checkbox_button.click())
    # print(checkbox.is_displayed())

    
# Activity 6
    checkbox = driver.find_element(By.ID, "checkbox")
    print(checkbox.is_displayed())
    checkbox.click()
    print(checkbox.is_displayed())
    driver.quit()