from pages.dictionaries.dictionaries_page import DictionariesPage
from pages.enrollments.enrollments_page import EnrollmentsPage
from pages.login.login_page import LoginPage
from pages.page import Page
from pages.persons.persons_page import PersonsPage

__author__ = 'dmakstc'


class Model:
    def __init__(self, driver):

        self.driver = driver
        self.login_page = LoginPage(self)
        self.persons_page = PersonsPage(self)
        self.dictionaries_page = DictionariesPage(self)
        self.enrollments_page = EnrollmentsPage(self)
        self.current_page = self.login_page

    def get_welcome_page(self):
        self.current_page = self.login_page
        self.current_page.wait_until_page_generate()
        return self.current_page

    def get_current_page(self):
        return self.current_page
