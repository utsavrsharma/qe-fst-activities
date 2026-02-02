from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with webdriver.Firefox() as driver:
    actions = ActionChains(driver)
    wait = WebDriverWait(driver,20)
    driver .get("https://training-support.net/webelements/dynamic-content")
    button = driver.find_element(By.ID,"genButton")
    actions.click(button).perform()
    wait.until(EC.text_to_be_present_in_element((By.ID, "word"), "release"))
    word_header = driver.find_element(By.ID, "word")
    print(word_header.text)
   