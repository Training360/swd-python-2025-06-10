from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_navigation(driver: WebDriver):
    driver.get("http://127.0.0.1:5501/pages/wizard/")
    driver.find_element(By.LINK_TEXT, "Next").click()
    driver.find_element(By.LINK_TEXT, "Next").click()
    driver.back()
    title = driver.find_element(By.TAG_NAME, "h1").text
    assert title == "Wizard1"


def test_resfresh(driver: WebDriver):
    driver.get("http://127.0.0.1:5501/pages/wizard/wizard2.html")
    driver.refresh()
    driver.refresh()
    driver.refresh()
    assert driver.find_element(By.ID, "counter-div").text == "4"
