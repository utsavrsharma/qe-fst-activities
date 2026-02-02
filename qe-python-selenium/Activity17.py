    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select

with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 20)
    driver.get("https://training-support.net/webelements/selects")
    dropdown_element = driver.find_element(By.CSS_SELECTOR,"select[multiple]")
    dropddown_options = Select(dropdown_element)
    dropddown_options.select_by_visible_text("HTML")
    dropddown_options.select_by_index(4)
    dropddown_options.select_by_index(5)
    dropddown_options.select_by_index(6)
    dropddown_options.deselect_by_index(6)
    selected_options = dropddown_options.all_selected_options
    
    for option in selected_options:
        print(option.text)
    
   

   