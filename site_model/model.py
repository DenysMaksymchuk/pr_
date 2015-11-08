from pages.login_page import LoginPage
from pages.persons_page import PersonsPage

__author__ = 'dmakstc'


class Model:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self)
        self.persons_page = PersonsPage(self)

    def get_welcome_page(self):
        return self.login_page
