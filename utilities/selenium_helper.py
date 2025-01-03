from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_elem(driver, elem, time: int = 15, wait_for: str = "Visibility") -> None:
    """ Wait UI element status: Visibility, Presence, Clickable, Invisibility """
    wait = WebDriverWait(driver, time)

    ui_element = None
    if wait_for == "Visibility":
        ui_element = wait.until(
            EC.visibility_of_element_located(elem),
            f"Element not visible\nSelector used: \n{elem}")
    return ui_element
