import time

import pytest
import sqlite3

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

    @pytest.mark.dependency(name="create_users")
    def test_create_2_users(self, web_driver, generate_password):
        admin_page = AdminPage(web_driver)
        self.current_user = admin_page.get_current_user()
        admin_page.create_user(user_name=self.user_name_1, emp_name=self.current_user,
                               user_role=self.user_role_1, status=self.user_status_1, password=generate_password)
        admin_page.create_user(user_name=self.user_name_2, emp_name=self.current_user,
                               user_role=self.user_role_2, status=self.user_status_2, password=generate_password)

    @pytest.mark.dependency(name="search", depends=["create_users"])
    def test_users_search(self, web_driver):
        admin_page = AdminPage(web_driver)
        admin_page.search_user_by_username(user_name=self.user_name_1)
        df = admin_page.parse_table()
        assert self.user_name_1 in df["Username"].values, f"Username {self.user_name_1} is not in the table"
        assert len(df) == 1, f"Number of table columns more than 1"

        admin_page.search_user_by_username(user_name=self.user_name_2)
        df = admin_page.parse_table()
        assert self.user_name_2 in df["Username"].values, f"Username {self.user_name_2} is not in the table"
        assert len(df) == 1, f"Number of table columns more than 1"

    @pytest.mark.dependency(name="reset_button", depends=["search"])
    def test_reset_button(self, web_driver):
        admin_page = AdminPage(web_driver)
        admin_page.btn_action('Reset')
        admin_page.verify_search_cleared()

    @pytest.mark.dependency(name="delete_user", depends=["reset_button"])
    def test_delete_user(self, web_driver, db_connection):
        admin_page = AdminPage(web_driver)
        admin_page.delete_user(self.user_name_2)

        # assert User was deleted from UI
        admin_page = AdminPage(web_driver)
        df = admin_page.parse_table()
        assert self.user_name_2 not in df["Username"].values, f"Username {self.user_name_2} is in the table"

        # assert User was deleted from database
        with pytest.raises(sqlite3.OperationalError):  # for Demo purposes
            cursor = db_connection.cursor()
            cursor.execute(f"SELECT * FROM users WHERE username = '{self.user_name_2}'")
            result = cursor.fetchone()
            assert result is None, f"User {self.user_name_2} was not deleted from the database"

    @pytest.mark.dependency(name="get_api", depends=["delete_user"])
    def test_get_api(self, web_driver, get_all_users):
        users = get_all_users
        admin_page = AdminPage(web_driver)
        df = admin_page.parse_table()

        # assert GET response and UI table has the same length
        with pytest.raises(TypeError):
            assert len(df) == len(users), f"GET response and UI table has different length"
