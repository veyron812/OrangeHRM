import time

from selenium.webdriver.common.by import By

from pageobjects.base_page import BasePage

TABLE_SEL = (By.XPATH, "//div[@role = 'table']")


class AdminPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_elem(TABLE_SEL)
        time.sleep(2)

    def create_user(self, user_name: str, emp_name: str, user_role: str, status: str, password: str) -> None:
        """ Function to create new user in UI """
        self.btn_action('Add')
        self.select_dropdown('User Role', user_role)
        self.select_dropdown('Status', status)
        self.enter_text_in_name_field('Employee Name', emp_name)
        self.enter_text('Username', user_name)
        self.enter_text('Password', password)
        self.enter_text('Confirm Password', password)
        self.btn_action('Save')
        self.verify_popup_msg('Success', 'Successfully Saved')

    def system_users_search(self, user_name: str, user_role: str, emp_name: str, status: str) -> None:
        """ Function to make 'System Users' search """
        self.enter_text('Username', user_name)
        self.select_dropdown('User Role', user_role)
        self.enter_text_in_name_field('Employee Name', emp_name)
        self.select_dropdown('Status', status)
        self.btn_action('Search')

    def search_user_by_username(self, user_name: str) -> None:
        """ Function to search user by username """
        self.btn_action('Reset')
        self.enter_text('Username', user_name)
        self.btn_action('Search')

    def delete_user(self, user_name: str) -> None:
        """ Function to delete user by username"""
        self.change_table_checkbox(user_name, 'check')
        self.btn_action('Delete Selected')
        self.btn_action('Yes, Delete')
        self.verify_popup_msg('Success', 'Successfully Deleted')

    def verify_search_cleared(self):
        """ Function verify 'System Users' search is cleared:
        4 values (Username, User Role, Employee Name, Status) has default values """
        assert self.get_text_field_value('Username') == ''
        assert self.get_text_field_value('Employee Name', 'placeholder') == 'Type for hints...'
        assert self.get_dropdown_value('User Role') == "-- Select --"
        assert self.get_dropdown_value('Status') == "-- Select --"