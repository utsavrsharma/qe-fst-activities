from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with webdriver.Firefox() as driver:
    driver.get("https://training-support.net/webelements/drag-drop")
    title = driver.title
    wait = WebDriverWait(driver, 10)
    actions  = ActionChains(driver)
    ball = driver.find_element(By.ID, "ball")
    dp1 = driver.find_element(By.ID,"dropzone1")
    dp2 = driver.find_element(By.ID,"dropzone2")
    actions.click_and_hold(ball).move_to_element(dp1).perform()
    wait.until(EC.text_to_be_present_in_element((By.XPATH,"//div[@id='dropzone1']/span"),"Dropped!"))
    print("Action confirmed")

    
    print()

