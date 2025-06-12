from selenium.webdriver.remote.webdriver import WebDriver
from calculator_po import CalculatorPage
from calculator_workflow import CalculatorWorkflow


def test_calculate(driver: WebDriver):
    assert 5 == CalculatorWorkflow(CalculatorPage(driver)).calculate(2, 3)
