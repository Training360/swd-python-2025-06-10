from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_add():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    driver.get("http://127.0.0.1:5501/pages/calculator/")
    input_field = driver.find_element(By.ID, "a-input")
    input_field.send_keys("5")

    input_field = driver.find_element(By.ID, "b-input")
    input_field.send_keys("8")
    # When
    button = driver.find_element(By.ID, "submit-button")
    button.click()
    # Then
    input_field = driver.find_element(By.ID, "result-input")
    result = input_field.get_attribute("value")
    print("Az eredmeny:", result)
    assert result == "13"
