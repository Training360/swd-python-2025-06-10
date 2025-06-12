from selenium.webdriver.remote.webdriver import WebDriver
from employees_po import EmployeesPage
import uuid


def test_save(driver: WebDriver):
    ## DB törlés
    name = ("John Doe" + str(uuid.uuid4()))[:25]
    page = EmployeesPage(driver)
    page.go()
    page.set_name(name)
    page.save()
    page.wait_for_message()
    table = page.get_table()

    assert name in [row[1] for row in table]
