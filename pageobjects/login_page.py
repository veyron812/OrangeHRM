from pageobjects.base_page import BasePage


class LoginPage(BasePage):

    def perform_login_action(self, user_name, password):
        self.enter_text('Username', user_name)
        self.enter_text('Password', password)
        self.btn_action('Login')
