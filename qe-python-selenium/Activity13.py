from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with webdriver.Firefox() as driver:
    actions = ActionChains(driver)
    wait = WebDriverWait(driver,20)
    driver .get("https://training-support.net/webelements/tables")
    print(driver.title)
    rows = driver.find_elements(By.TAG_NAME,"tr")
    print(f"number of rows: {len(rows)}")
    cols = driver.find_elements(By.TAG_NAME,"th")
    print(f"number of coloumns : {len(cols)}")


    third_row = driver.find_elements(By.XPATH,"//tr[3]/td")
    for cell in third_row:
        print(cell.text)
    second_row = driver.find_element(By.XPATH,"//tr[2]/td[2]").text    
    print(second_row)

    

   