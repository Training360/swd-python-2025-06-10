from selenium.webdriver.remote.webdriver import WebDriver
from calculator_po import CalculatorPage


def test_calculate(driver: WebDriver):
    # Arrange, Act, Assert - AAA
    # Arrange = Given
    calculator_page = CalculatorPage(driver)
    calculator_page.go()
    calculator_page.set_operands(2, 3)
    # Act = When
    calculator_page.click_equal_button()
    # Assert = Then
    assert calculator_page.get_result() == 5
