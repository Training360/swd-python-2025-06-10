from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_link(driver: WebDriver):
    # Given
    driver.get(
        "https://www.training360.com/tesztautomatizalas-selenium-webdriverrel-pythonban-tanfolyam-swd-python"
    )
    # When
    link = driver.find_element(By.PARTIAL_LINK_TEXT, "itt olvashat")
    # Then
    assert "/egyedi-oktatasi-szolgaltatasok" in link.get_attribute("href")


def test_price_by_class_name(driver: WebDriver):
    # Given
    driver.get(
        "https://www.training360.com/tesztautomatizalas-selenium-webdriverrel-pythonban-tanfolyam-swd-python"
    )
    # When
    price = driver.find_element(By.CLASS_NAME, "selected-course__amount")
    # Then
    assert price.text == "377 520 Ft"


def test_price_by_css_selector(driver: WebDriver):
    # Given
    driver.get(
        "https://www.training360.com/tesztautomatizalas-selenium-webdriverrel-pythonban-tanfolyam-swd-python"
    )
    # When
    price = driver.find_element(By.CSS_SELECTOR, ".selected-course__amount")
    # Then
    assert price.text == "377 520 Ft"


def test_outline_items(driver: WebDriver):
    # Given
    driver.get(
        "https://www.training360.com/tesztautomatizalas-selenium-webdriverrel-pythonban-tanfolyam-swd-python"
    )
    # When
    webelements = driver.find_elements(By.CSS_SELECTOR, "#Outline li")
    items = [element.text for element in webelements]
    # Then
    print(items)
    assert len(items) > 10
    assert items[0] == "Webes alkalmazások felépítése"


def test_outline_items_xpath(driver: WebDriver):
    # Given
    driver.get(
        "https://www.training360.com/tesztautomatizalas-selenium-webdriverrel-pythonban-tanfolyam-swd-python"
    )
    # When
    webelements = driver.find_elements(By.XPATH, '//*[@id="C_Outline"]/ul/li')
    items = [element.text for element in webelements]
    # Then
    print(items)
    assert len(items) > 10
    assert items[0] == "Webes alkalmazások felépítése"
