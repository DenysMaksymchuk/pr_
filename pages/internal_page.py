import abc

from selenium.webdriver.common.by import By

from pages.page import Page

__author__ = 'dmakstc'


class InternalPage(Page):
    __metaclass__ = abc.ABCMeta
    # locators
    INTERNAL_PAGE_ID = (By.CSS_SELECTOR, "nav")
    USER_DROPDOWN = (By.XPATH, "//i[@class='fa fa-user fa-fw']")
    LOGOUT_BUTTON = (By.XPATH, "//li[@class='dropdown open']//a[@ng-click='header.logout()']")
    PERSON_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.person.list']")
    ENROLLMENTS_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.enrolment.list']")
    DICTIONARIES_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.dictionaries']")

    # web elements

    @property
    def user_dropdown(self):
        return self.driver.find_element(*self.USER_DROPDOWN)

    @property
    def logout_button(self):
        return self.driver.find_element(*self.LOGOUT_BUTTON)

    @property
    def persons_page_link(self):
        return self.driver.find_element(*self.PERSON_PAGE_LINK)

    @property
    def enrollments_page_link(self):
        return self.driver.find_element(*self.ENROLLMENTS_PAGE_LINK)

    @property
    def dictionaries_page_link(self):
        return self.driver.find_element(*self.DICTIONARIES_PAGE_LINK)

    # page elem function

    def user_dropdown_ref_click(self):
        self.user_dropdown.click()

    def logout_button_click(self):
        self.logout_button.click()
        self.wait_until_page_generate()
        self.model.current_page = self.model.login_page
        return self.model.get_current_page()

    def persons_page_link_click(self):
        self.persons_page_link.click()
        self.wait_until_page_generate()
        self.model.current_page = self.model.persons_page
        return self.model.get_current_page()

    def enrollments_page_link_click(self):
        self.enrollments_page_link.click()
        self.wait_until_page_generate()
        self.model.current_page = self.model.enrollments_page
        return self.model.get_current_page()

    # general function

    def logout(self):
        self.user_dropdown_ref_click()
        return self.logout_button_click()
