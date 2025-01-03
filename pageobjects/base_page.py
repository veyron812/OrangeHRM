import time
from typing import Literal

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_current_user(self) -> str:
        """ Function to get current username """
        curr_user_sel = (By.XPATH, "//p[@class = 'oxd-userdropdown-name']")
        field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(curr_user_sel),
            f"Element not visible\nSelector used: \n{curr_user_sel}")
        curr_user = field.text
        return curr_user


    def enter_text(self, field_label: str, text: str) -> None:
        """ Function to enter text in UI text field (without hint) """

        field_sel = (By.XPATH, f"//label[text() = '{field_label}']//following::input[1]")
        field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(field_sel),
            f"Element not visible\nSelector used: \n{field_sel}")
        field.send_keys(text)
        time.sleep(2)

    def enter_text_in_name_field(self, field_label: str, name: str) -> None:
        """ Function to enter text in name field with hint. Will search for the last name in the hint """

        self.enter_text(field_label, name)
        last_name = name.split()[-1]
        hint_sel = (By.XPATH, f"//div[@class = 'oxd-autocomplete-option']//span[contains(text(), '{last_name}')]")
        hint = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(hint_sel),
            f"Element not visible\nSelector used: \n{hint_sel}")
        hint.click()


    def btn_action(self, btn_name: str) -> None:
        """ Function to click button """

        btn_sel = (By.XPATH, f"//button[text() = ' {btn_name} ']")
        btn = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(btn_sel),
            f"Button not visible\nSelector used: \n{btn_sel}")
        btn.click()

    def get_dropdown_value(self, dropdown_label: str) -> str:
        drdwn_field_sel = (
        By.XPATH, f"//label[text() = '{dropdown_label}']//following::div[@class = 'oxd-select-wrapper'][1]")
        drdwn_field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(drdwn_field_sel),
            f"Button not visible\nSelector used: \n{drdwn_field_sel}")
        dropdown_value = drdwn_field.get_attribute('value')
        print(f"Value: {dropdown_value}")


    def select_dropdown(self, dropdown_label: str, dropdown_value: str):

        # drdwn_field_sel = (By.XPATH, f"//label[text() = '{dropdown_label}']//following::div[@class = 'oxd-select-wrapper'][1]")
        drdwn_field_sel = (By.XPATH, f"//label[text() = '{dropdown_label}']//following::div[@class = 'oxd-select-text-input'][1]")
        drdwn_field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(drdwn_field_sel),
            f"Button not visible\nSelector used: \n{drdwn_field_sel}")
        drdwn_field.click()

        drdwn_value_sel = (By.XPATH, f"//div[@role = 'option']//span[text() = '{dropdown_value}']")
        drdwn_value = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(drdwn_value_sel),
            f"Button not visible\nSelector used: \n{drdwn_value_sel}")
        drdwn_value.click()
        time.sleep(2)

    def verify_popup_msg(self, popup_title: str, popup_text: str) -> None:
        popup_title_sel = (By.XPATH, f"//p[contains(@class, 'title')][text() = '{popup_title}']")
        popup_msg_sel = (By.XPATH, f"//p[contains(@class, 'message')][text() = '{popup_text}']")
        popup_title = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(popup_title_sel),
            f"Button not visible\nSelector used: \n{popup_title_sel}")
        popup_msg = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(popup_msg_sel),
            f"Button not visible\nSelector used: \n{popup_msg_sel}")

    def get_table_checkbox_status(self, row_value: str) -> bool:
        """
        Function to get checkbox status.
        Will find checkbox in the table by provided value.
        Always expect checkbox to be the first left column un the table.
        Return True if checked, False if not checked"""
        checkbox_sel = (By.XPATH, f"//div[text() = '{row_value}']//preceding::div[contains(@class, 'checkbox')][1]//span")
        checkbox = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(checkbox_sel),
            f"Element not visible\nSelector used: \n{checkbox_sel}")
        checkbox_class = checkbox.get_attribute('class')
        if "oxd-checkbox-input--active" in checkbox_class:
            return False  # checkbox not checked
        elif "oxd-checkbox-input--focus" in checkbox_class:
            return True  # checkbox is checked


    def change_table_checkbox(self, row_value: str, desired_status: Literal['check', 'uncheck']) -> None:
        """ Function to change checkbox status in the table """
        checkbox_sel = (By.XPATH, f"//div[text() = '{row_value}']//preceding::div[contains(@class, 'checkbox')][1]//span")
        checkbox = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(checkbox_sel),
            f"Element not visible\nSelector used: \n{checkbox_sel}")
        curr_status = self.get_table_checkbox_status(row_value)
        if (curr_status is False and desired_status == "check") or (curr_status is True and desired_status == "uncheck"):
            checkbox.click()


    def get_text_field_value(self, field_label: str, attribute: Literal['value', 'placeholder'] = 'value') -> str:
        field_sel = (By.XPATH, f"//label[text() = '{field_label}']//following::input[1]")
        field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(field_sel),
            f"Element not visible\nSelector used: \n{field_sel}")
        field_value = field.get_attribute(attribute)
        return field_value


