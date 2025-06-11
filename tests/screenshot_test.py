from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_screenshot(driver: WebDriver):
    driver.get("http://127.0.0.1:5501/pages/grid/")

    driver.save_screenshot("screenshot.png")

    element = driver.find_element(
        By.CSS_SELECTOR, "body > table > tbody > tr:nth-child(2) > td:nth-child(2)"
    )

    element.screenshot("element_screenshot.png")
