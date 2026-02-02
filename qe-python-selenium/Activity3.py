from selenium import webdriver

with webdriver.Firefox() as driver:
    driver.maximize_window()
    driver .get("https://training-support.net/webelements/login-form/") 
    driver.find_element("xpath","//input[contains(@id,'username')]").send_keys("admin")
    driver.find_element("xpath","//input[contains(@placeholder,'Pass')]").send_keys("password")
    driver.find_element("xpath", "//button[text()='Submit']").click()
    driver.quit()