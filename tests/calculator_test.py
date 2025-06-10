from selenium.webdriver.common.by import By
import pytest

# DRY = don't repeat yourself
# Data driven testing


@pytest.mark.parametrize("a,b,expected", [(0, 0, 0), (5, 8, 13), (-5, 8, 3)])
def test_add(driver, a, b, expected):
    print("Test")
    driver.get("http://127.0.0.1:5501/pages/calculator/")
    input_field = driver.find_element(By.ID, "a-input")
    input_field.send_keys(str(a))

    input_field = driver.find_element(By.ID, "b-input")
    input_field.send_keys(str(b))
    # When
    button = driver.find_element(By.ID, "submit-button")
    button.click()
    # Then
    input_field = driver.find_element(By.ID, "result-input")
    result = input_field.get_attribute("value")
    print("Az eredmeny:", result)
    assert result == str(expected)
