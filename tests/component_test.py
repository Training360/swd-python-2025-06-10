from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_find_by_natural_id(driver: WebDriver):
    # Given
    driver.get("http://127.0.0.1:5501/pages/components/")
    tr_elements = driver.find_elements(By.CSS_SELECTOR, "tbody > tr")
    for tr_element in tr_elements:
        td_elements = tr_element.find_elements(By.CSS_SELECTOR, "td")
        id = td_elements[0].text
        name = td_elements[1].text
        print("Row:", id, name)
        if id == "2":
            assert name == "Jack Doe"
            # name_found = name
    # assert name_found == "Jack Doe"


def test_table(driver: WebDriver):
    driver.get("http://127.0.0.1:5501/pages/components/")
    tr_elements = driver.find_elements(By.CSS_SELECTOR, "tbody > tr")
    rows = []
    for tr_element in tr_elements:
        td_elements = tr_element.find_elements(By.CSS_SELECTOR, "td")
        row = [element.text for element in td_elements]
        rows.append(row)
    print(rows)


def test_table_dictionary(driver: WebDriver):
    driver.get("http://127.0.0.1:5501/pages/components/")
    tr_elements = driver.find_elements(By.CSS_SELECTOR, "tbody > tr")
    rows = []
    for tr_element in tr_elements:
        td_elements = tr_element.find_elements(By.CSS_SELECTOR, "td")
        row = [element.text for element in td_elements]
        headers = ["id", "name"]
        row_dict = dict(zip(headers, row))
        rows.append(row_dict)
    print(rows)

    assert "Jack Doe" == [row["name"] for row in rows if row["id"] == "2"][0]
