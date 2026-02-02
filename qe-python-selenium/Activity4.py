from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Firefox() as driver:
    driver.maximize_window()
    driver .get("https://training-support.net/webelements/target-practice") 
    print(driver.title)
    print(driver.find_element('xpath',"//h3").text)
    print(driver.find_element('xpath',"//h5").value_of_css_property("color"))
    print(driver.find_element(By.CLASS_NAME,"purple").get_attribute("class"))
    
    driver.quit()