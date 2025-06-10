from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.selenium.dev/")

search_box = driver.find_element(By.CLASS_NAME, "DocSearch-Button-Placeholder")
print(type(search_box))

search_box.click()
