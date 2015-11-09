from selenium.webdriver.common.by import By

from pages.page import Page
from web_elements_util.utils import input_text_in_field, checkbox_set_state

__author__ = 'dmakstc'


class LoginPage(Page):
    # locators
    USERNAME_FIELD = (By.ID, "inputLogin")
    PASSWORD_FIELD = (By.ID, "inputPassword")
    LOGIN_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    # web elements
    @property
    def username_field(self):
        return self.driver.find_element(*self.USERNAME_FIELD)

    @property
    def password_field(self):
        return self.driver.find_element(*self.PASSWORD_FIELD)

    @property
    def login_checkbox(self):
        return self.driver.find_element(*self.LOGIN_CHECKBOX)

    @property
    def submit_button(self):
        return self.driver.find_element(*self.SUBMIT_BUTTON)

    # page elem function

    def input_in_username_field(self, login):
        input_text_in_field(self.username_field, login, True)

    def input_in_password_field(self, password):
        input_text_in_field(self.password_field, password, True)

    def submit_button_click(self):
        self.submit_button.click()
        self.model.current_page = self.model.persons_page
        self.wait_until_page_generate()
        return self.model.get_current_page()

    def set_remind_me_checkbox_state(self, is_should_check):
        checkbox_set_state(self.login_checkbox, is_should_check)

    # general function
    def get_unique(self):
        return self.username_field

    def login(self):
        """
        function for quick login
        :return:
        """
        input_text_in_field(self.username_field, 'admin', False)
        input_text_in_field(self.password_field, 'nimda', False)
        return self.submit_button_click()
