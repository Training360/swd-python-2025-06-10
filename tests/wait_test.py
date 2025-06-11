from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    wait = WebDriverWait(driver, timeout=3, poll_frequency=0.2)

    # Polling
    # wait.until(lambda d: d.find_element(By.CLASS_NAME, "alert").is_displayed())

    # alert = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert")))

    # alert = driver.find_element(By.CLASS_NAME, "alert")

    alert = wait.until(presence_of_element_text_starts_with("Nice"))

    assert alert.text == ("Nice, you triggered this alert message!")


def presence_of_element_text_starts_with(prefix: str):
    def _predicate(driver: WebDriver):
        alert = driver.find_element(By.CLASS_NAME, "alert")
        text = alert.text
        if text.startswith(prefix):
            return alert
        else:
            return False

    return _predicate
