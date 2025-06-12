from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class EmployeesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def go(self):
        """Navigate to the calculator page."""
        url = os.getenv("EMPLOYEES_URL", "http://localhost:5025")
        self.driver.get(url)

    def set_name(self, name: str = "John Doe"):
        """Set the name of the employee."""
        input_field = self.driver.find_element(By.ID, "name")
        input_field.send_keys(name)

    def save(self):
        self.driver.find_element(By.ID, "submit-input").click()

    def wait_for_message(self):
        wait = WebDriverWait(self.driver, timeout=3)
        wait.until(EC.presence_of_element_located((By.ID, "message-paragraph")))

    def get_table(self):
        tr_elements = self.driver.find_elements(By.CSS_SELECTOR, "tbody > tr")

        rows = []
        for tr_element in tr_elements:
            td_elements = tr_element.find_elements(By.CSS_SELECTOR, "td")
            row = [element.text for element in td_elements]
            rows.append(row)
        return rows
