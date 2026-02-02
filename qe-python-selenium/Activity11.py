from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with webdriver.Firefox() as driver:
    actions = ActionChains(driver)
    wait = WebDriverWait(driver,10)
    driver .get("https://training-support.net/webelements/dynamic-controls")
    checkbox = driver.find_element(By.ID,"checkbox")
    checkbox_button = driver.find_element(By.XPATH,"//button[text()='Toggle Checkbox']")
    actions.click(checkbox_button).perform()
    wait.until(EC.invisibility_of_element_located(checkbox))
    print("checkbox is gone")
    actions.click(checkbox_button).perform()
    wait.until(EC.visibility_of_element_located(checkbox))
    print("checkbox is visible")
    driver.quit()