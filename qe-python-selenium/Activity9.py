from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/keyboard-events")
    title = driver.title
    print(title)
    actions = ActionChains(driver)
    actions.send_keys("Utsav Sharma").perform()
    result = driver.find_element(By.XPATH, "/html/body/div/main/div/div/div/div/div[2]/h1")
    print(result.text)
    driver.quit