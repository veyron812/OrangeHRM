import time
from typing import Literal

from pandas import DataFrame
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import pandas as pd

curr_user_sel = (By.XPATH, "//p[@class = 'oxd-userdropdown-name']")

def input_text_sel(field_label): return By.XPATH, f"//label[text() = '{field_label}']//following::input[1]"
def hint_sel(last_name): return By.XPATH, f"//div[@class = 'oxd-autocomplete-option']//span[contains(text(), '{last_name}')]"
def btn_sel(btn_name): return By.XPATH, f"//button[text() = ' {btn_name} ']"
def drdwn_field_sel(dropdown_label): return By.XPATH, f"//label[text() = '{dropdown_label}']//following::div[@class = 'oxd-select-text-input'][1]"
def drdwn_value_sel(dropdown_value): return By.XPATH, f"//div[@role = 'option']//span[text() = '{dropdown_value}']"
def popup_title_sel(popup_title): return By.XPATH, f"//p[contains(@class, 'title')][text() = '{popup_title}']"
def popup_msg_sel(popup_text): return By.XPATH, f"//p[contains(@class, 'message')][text() = '{popup_text}']"
def checkbox_sel(row_value): return By.XPATH, f"//div[text() = '{row_value}']//preceding::div[contains(@class, 'checkbox')][1]//span"


class BasePage:


    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def wait_elem(self, elem, wait_time: int = 15, wait_for: str = "Visibility"):
        """ Wait UI element status: Visibility, Presence, Clickable, Invisibility """
        wait = WebDriverWait(self.driver, wait_time)

        ui_element = None
        if wait_for == "Visibility":
            ui_element = wait.until(
                EC.visibility_of_element_located(elem),
                f"Element not visible\nSelector used: \n{elem}")
        return ui_element

    def get_current_user(self) -> str:
        """ Function to get current username """
        curr_user = self.wait_elem(curr_user_sel).text
        return curr_user


    def enter_text(self, field_label: str, text: str) -> None:
        """ Function to enter text in UI text field (without hint) """
        field = self.wait_elem(input_text_sel(field_label))
        self.actions.click(field)
        field.clear()
        self.actions.pause(1).send_keys(text).pause(1).perform()


    def enter_text_in_name_field(self, field_label: str, name: str) -> None:
        """ Function to enter text in name field with hint. Will search for the last name in the hint """
        self.enter_text(field_label, name)
        last_name = name.split()[-1]
        self.wait_elem(hint_sel(last_name)).click()
        time.sleep(2)


    def btn_action(self, btn_name: str) -> None:
        """ Function to click button """
        btn = self.wait_elem(btn_sel(btn_name))
        self.actions.pause(1).move_to_element(btn).pause(1).click(btn).pause(1).perform()

    def get_dropdown_value(self, dropdown_label: str) -> str:
        """ Function to get current dropdown value """
        dropdown_value = self.wait_elem(drdwn_field_sel(dropdown_label)).text
        return dropdown_value

    def select_dropdown(self, dropdown_label: str, dropdown_value: str) -> None:
        """ Function to select value in the dropdown"""
        self.wait_elem(drdwn_field_sel(dropdown_label)).click()
        self.wait_elem(drdwn_value_sel(dropdown_value)).click()
        time.sleep(2)

    def verify_popup_msg(self, popup_title: str, popup_text: str) -> None:
        self.wait_elem(popup_title_sel(popup_title))
        self.wait_elem(popup_msg_sel(popup_text))


    def get_table_checkbox_status(self, row_value: str) -> bool:
        """
        Function to get checkbox status.
        Will find checkbox in the table by provided value.
        Always expect checkbox to be the first left column un the table.
        Return True if checked, False if not checked"""

        checkbox_class = self.wait_elem(checkbox_sel(row_value)).get_attribute('class')
        if "oxd-checkbox-input--active" in checkbox_class:
            return False  # checkbox not checked
        elif "oxd-checkbox-input--focus" in checkbox_class:
            return True  # checkbox is checked


    def change_table_checkbox(self, row_value: str, desired_status: Literal['check', 'uncheck']) -> None:
        """ Function to change checkbox status in the table """
        checkbox = self.wait_elem(checkbox_sel(row_value), wait_time=5)
        curr_status = self.get_table_checkbox_status(row_value)

        if (curr_status is False and desired_status == "check") or (curr_status is True and desired_status == "uncheck"):
            checkbox.click()
        time.sleep(2)

    def get_text_field_value(self, field_label: str, attribute: Literal['value', 'placeholder'] = 'value') -> str:
        field_value = self.wait_elem(input_text_sel(field_label)).get_attribute(attribute)
        return field_value

    def parse_table(self) -> DataFrame:
        """ Function to parse table from UI. Returns pandas DataFrame
            Read column names without Ascending-Descending arrows """

        # Read table with BeautifulSoup
        html_content = self.driver.page_source
        soup = BeautifulSoup(html_content, "html.parser")
        table_div = soup.find("div", role="table")

        # Extract headers
        header_row = table_div.find("div", class_="oxd-table-header")
        headers = [cell.text.strip() for cell in header_row.find_all("div", role="columnheader")]
        headers = [header.replace('AscendingDescending', '') for header in headers]

        # Extract data rows
        data_rows = []
        for row in table_div.find_all("div", class_="oxd-table-card"):
            cells = [cell.text.strip() for cell in row.find_all("div", role="cell")]
            data_rows.append(cells)

        # Convert to a pandas DataFrame
        df = pd.DataFrame(data_rows, columns=headers)

        # Display the DataFrame
        print(df)

        return df
