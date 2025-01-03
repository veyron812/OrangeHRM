import os

import pytest
import requests
from dotenv import load_dotenv
from faker import Faker
import sqlite3

from pageobjects.login_page import LoginPage


load_dotenv()

user = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
demo_url = f"{os.getenv('BASE_URL')}/web/index.php/admin/viewSystemUsers"


@pytest.fixture(scope="session")
def web_driver(request):
    """ Fixture to select webdriver. Go through login process """
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    web_driver = webdriver.Chrome(
        service=Service(executable_path=ChromeDriverManager().install())
    )
    web_driver.maximize_window()

    web_driver.get(demo_url)
    LoginPage(web_driver).perform_login_action(user, password)
    yield web_driver
    web_driver.quit()


@pytest.fixture()
def generate_password() -> str:
    """ Fixture to generate 12 digits password with upper and lower letters, numbers and special characters"""
    faker = Faker()
    password_12 = faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password_12


@pytest.fixture(scope='session')
def db_connection():
    """ Fixture to connect to database """
    connection = sqlite3.connect(":memory:")  # In-memory SQLite DB for the test
    cursor = connection.cursor()

    yield connection  # Provide the connection to tests

    connection.close()


@pytest.fixture()
def get_all_users():
    """ Fixture to make GET API call for all users """
    url = f"{os.getenv('BASE_URL')}/users"
    response = requests.get(url)
    if response.status_code == "200":
        data = response.json()
        return data
