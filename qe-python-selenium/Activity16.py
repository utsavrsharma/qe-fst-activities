    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select

with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 20)
    driver.get("https://training-support.net/webelements/selects")
    dropdown_element = driver.find_element(By.TAG_NAME,"select")
    dropdown_object = Select(dropdown_element)
    options = dropdown_object.options

    dropdown_object.select_by_visible_text("Three")
    dropdown_object.select_by_index(3)
    dropdown_object.select_by_value("four")

    selected_options = dropdown_object.all_selected_options

    for option in options[1:]:
        print(option.text)
    


   