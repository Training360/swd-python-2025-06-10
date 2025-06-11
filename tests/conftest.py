from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    print("Before")
    options = Options()
    # options.add_argument("--headless")  # Run in headless mode
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    yield driver
    print("After")
    driver.quit()
