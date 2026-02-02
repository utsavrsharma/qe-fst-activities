from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
actions = ActionChains(driver)
wait = WebDriverWait(driver,10)
try:
    driver.get("https://training-support.net/webelements/mouse-events")
    
    print("Page title is:", driver.title)

   
    cargo_lock = driver.find_element(By.CSS_SELECTOR, ".file:nth-child(1)")
    cargo_toml = driver.find_element(By.CSS_SELECTOR, ".file:nth-child(2)")
    
    actions.click(cargo_lock).move_to_element(cargo_toml).click().perform()
    
    action_text1 = driver.find_element(By.ID, "result").text
    print("Sequence 1 Result:", action_text1)

    
    src_button = driver.find_element(By.CSS_SELECTOR, ".file:nth-child(3)")
    target_button = driver.find_element(By.CSS_SELECTOR, ".file:nth-child(4)")
    
    open_button = driver.find_element(By.CSS_SELECTOR,".li:nth-child(1)")
    actions.double_click(src_button).context_click(target_button).click(open_button).perform()
    
    action_text2 = driver.find_element(By.ID, "result").text
    print("Sequence 2 Result:", action_text2)

finally:
    driver.quit()