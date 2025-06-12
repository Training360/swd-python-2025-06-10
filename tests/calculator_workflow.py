from calculator_po import CalculatorPage


class CalculatorWorkflow:
    def __init__(self, calculator_page: CalculatorPage):
        self.calculator_page = calculator_page

    def calculate(self, a: int = 0, b: int = 0) -> int:
        """Perform a calculation with the given operands."""
        self.calculator_page.go()
        self.calculator_page.set_operands(a, b)
        self.calculator_page.click_equal_button()
        return self.calculator_page.get_result()
