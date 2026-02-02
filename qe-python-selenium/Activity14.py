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
    initial_book_name = driver.find_element(By.XPATH,"//tr[5]/td[2]").text
    print(initial_book_name)
    price_header_button = driver.find_element(By.XPATH,"//th[text()='Price']")
    actions.click(price_header_button).perform()
    # wait.until(lambda d: d.find_element(By.XPATH, "//table/tbody/tr[5]/td[2]").text != initial_book_name)
    final_book_name = driver.find_element(By.XPATH,"//tr[5]/td[2]").text
    print( final_book_name)


    

   