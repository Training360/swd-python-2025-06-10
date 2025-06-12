from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
import os


@pytest.fixture
def driver():
    print("Before")

    driver_type = os.getenv("SELENIUM_DRIVER", "ChromeDriver")
    if driver_type == "ChromeDriver":
        options = Options()
        # options.add_argument("--headless")  # Run in headless mode
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    elif driver_type == "RemoteWebDriver":
        command_executor = os.getenv("SELENIUM_HUB_URL", "http://localhost:4444/wd/hub")
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote(command_executor=command_executor, options=options)
    else:
        raise ValueError(f"Invalid driver: {driver_type}")

    yield driver
    print("After")
    driver.quit()
