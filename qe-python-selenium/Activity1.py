from selenium import webdriver

with webdriver.Firefox() as driver:
     driver .get("https://training-support.net")

     print(driver.title)
     about_us_link = driver.find_element(By.LINK_TEXT, "About Us")
     about_us_link.click()
     print(driver.title)
     driver.quit()