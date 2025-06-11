from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_live_alert(driver: WebDriver):
    # Given
    driver.get("http://127.0.0.1:5501/pages/messages/")
    driver.find_element(By.ID, "liveAlertBtn").click()

    alert = driver.find_element(By.CLASS_NAME, "alert")
    assert alert.text.startswith("Nice")


def test_live_alert_with_timeout(driver: WebDriver):
    # Given
    driver.get("http://127.0.0.1:5501/pages/messages/")
    driver.find_element(By.ID, "liveAlertTimeoutBtn").click()

    alert = driver.find_element(By.CLASS_NAME, "alert")

    assert alert.text.startswith("Nice")
