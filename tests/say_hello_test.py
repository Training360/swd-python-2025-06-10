from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_say_hello():
    # Given
    name = "John Doe"
    # When
    message = f"Hello, {name}!"
    # Then
    assert message == "Hello, John Doe!"


def test_say_hello_selenium():
    # Given
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://127.0.0.1:5501/pages/welcome/")
    input_field = driver.find_element(By.ID, "name-input")
    input_field.send_keys("John Doe")
    # When
    button = driver.find_element(By.ID, "welcome-button")
    button.click()
    # Then
    message_div = driver.find_element(By.ID, "welcome-div")
    message = message_div.text
    assert message == "Hello John Doe!"
