from selenium.webdriver.remote.webdriver import WebDriver
from employees_po import EmployeesPage
import uuid
import psycopg2 as psycopg


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


def test_save_db(driver: WebDriver):
    delete_employees()
    page = EmployeesPage(driver)
    page.go()
    page.set_name()
    page.save()
    page.wait_for_message()
    table = page.get_table()

    assert "John Doe" == table[0][1]


def delete_employees():
    with psycopg.connect(
        user="employees", password="employees", host="localhost", dbname="employees"
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM employees;")
            conn.commit()
