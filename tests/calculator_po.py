from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def go(self):
        """Navigate to the calculator page."""
        self.driver.get("http://127.0.0.1:5501/pages/calculator/")

    def set_operands(self, a: int = 0, b: int = 0):
        """Set the operands for the calculation."""
        input_field = self.driver.find_element(By.ID, "a-input")
        input_field.send_keys(str(a))

        input_field = self.driver.find_element(By.ID, "b-input")
        input_field.send_keys(str(b))

    def click_equal_button(self):
        """Click the button to perform the calculation."""
        self.driver.find_element(By.ID, "submit-button").click()

    def get_result(self) -> int:
        """Retrieve the result of the calculation."""
        input_field = self.driver.find_element(By.ID, "result-input")
        result = input_field.get_attribute("value")
        return int(result)
