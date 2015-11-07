from selenium.webdriver.common.by import By
from pages.internal_page import InternalPage

__author__ = 'dmakstc'


class PersonsPage(InternalPage):

    # locators
    PERSONS_PAGE_ID = (By.CSS_SELECTOR, ".fa.fa-user.text-danger")

    # web elements

    # page elem function

    # general function
    def get_unique(self):
        return self.driver.find_element(*self.PERSONS_PAGE_ID)
