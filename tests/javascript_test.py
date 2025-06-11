from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_javascript(driver: WebDriver):
    driver.get("http://127.0.0.1:5501/pages/grid/")

    javascript = """
        var element = document.querySelector("body > table > tbody > tr:nth-child(2) > td:nth-child(2)");
        element.style.border = 'thin solid red';
    """

    driver.execute_script(javascript)
    driver.save_screenshot("javascript_screenshot.png")


def test_javascript_pin(driver: WebDriver):
    driver.get("http://127.0.0.1:5501/pages/grid/")

    javascript = """
        var element = document.querySelector("body > table > tbody > tr:nth-child(2) > td:nth-child(2)");
        element.style.border = 'thin solid red';
    """

    script_key = driver.pin_script(javascript)
    driver.execute_script(script_key)
    driver.save_screenshot("javascript_screenshot.png")
