
import pytest

import pytest
from faker import Faker
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pageobjects.login_page import LoginPage


# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
USER_NAME = "Admin"
PASSWORD = "admin123"


@pytest.fixture(scope="session")
def web_driver(request):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    web_driver = webdriver.Chrome(
        service=Service(executable_path=ChromeDriverManager().install())
    )
    web_driver.maximize_window()

    web_driver.get(URL)
    LoginPage(web_driver).perform_login_action(USER_NAME, PASSWORD)
    yield web_driver
    web_driver.quit()


@pytest.fixture()
def generate_password() -> str:
    """ Fixture to generate 12 digits password with upper and lower letters, numbers and special characters"""
    faker = Faker()
    password = faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password
