from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

# DRY = don't repeat yourself
# Data driven testing


def read_file():
    data = []
    with open("tests/calculator.csv") as f:
        for line in f:
            parts = line.split(",")
            data.append((int(parts[0]), int(parts[1]), int(parts[2])))
    return data


# @pytest.mark.parametrize("a,b,expected", [(0, 0, 0), (5, 8, 13), (-5, 8, 3)])
@pytest.mark.parametrize("a,b,expected", read_file())
def test_add(driver: WebDriver, a: int, b: int, expected: int):
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
