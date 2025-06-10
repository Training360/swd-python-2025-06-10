from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
# options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
# driver.maximize_window()
driver.get("http://127.0.0.1:5501/pages/welcome/")

input_field = driver.find_element(By.ID, "name-input")
input_field.send_keys("John Doe")

button = driver.find_element(By.ID, "welcome-button")
button.click()
