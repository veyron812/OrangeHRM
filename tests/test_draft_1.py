import time

import pytest
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageobjects.admin_page import AdminPage


@pytest.mark.demo
class TestDemo:

    user_name_1 = f"Test_User_{time.time()}"
    user_role_1 = "Admin"
    user_status_1 = "Enabled"

    user_name_2 = f"Test_User_{time.time()}"
    user_role_2 = "ESS"
    user_status_2 = "Disabled"

    current_user = ''

    # def test_create_2_users(self, web_driver, generate_password):
    #     admin_page = AdminPage(web_driver)
    #     self.current_user = admin_page.get_current_user()
    #     admin_page.create_user(user_name=self.user_name_1, emp_name=self.current_user,
    #                            user_role=self.user_role_1, status=self.user_status_1, password=generate_password)
    #     admin_page.create_user(user_name=self.user_name_2, emp_name=self.current_user,
    #                            user_role=self.user_role_2, status=self.user_status_2, password=generate_password)
    #
    # def test_users_search(self, web_driver):
    #     admin_page = AdminPage(web_driver)
    #     admin_page.search_user_by_username(user_name=self.user_name_1)
    #     # assert table values
    #     admin_page.search_user_by_username(user_name=self.user_name_2)

    def test_reset_button(self, web_driver):
        admin_page = AdminPage(web_driver)
        admin_page.select_dropdown('User Role', 'Admin')
        # admin_page.get_dropdown_value('User Role')


    # def test_delete_user(self, web_driver):
    #     admin_page = AdminPage(web_driver)
    #     admin_page.delete_user(self.user_name_2)
    #     time.sleep(4)
        # assert was deleted from the table
        # assert was deleted with SQL query

    def test_get_api(self):
        pass
        # assert GET request and UI table has the same results


    # ADD README
    # REFACTOR ALL