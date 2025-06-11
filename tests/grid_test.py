from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_relative_locators(driver: WebDriver):
    # Given
    driver.get("http://127.0.0.1:5501/pages/grid/")
    element5 = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) td:nth-child(2)")
    assert element5.text == "5"
    # When
    element2 = driver.find_element(
        locate_with(By.CSS_SELECTOR, "td").to_left_of(element5)
    )
    # Then
    assert element2.text == "4"
