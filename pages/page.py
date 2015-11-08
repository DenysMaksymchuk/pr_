import abc

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'dmakstc'


class Page:
    __metaclass__ = abc.ABCMeta

    def __init__(self, model):
        self.driver = model.driver
        self.wait = WebDriverWait(self.driver, 15)
        self.model = model

    # locators
    SPINNER_OFF = (By.XPATH, "//div[@id='spinnerDiv' and @style='display: none;']")
    ERROR_ALERT = (By.ID, "toast-container")

    # web elements
    @property
    def alert(self):
        return self.driver.find_element(*self.ERROR_ALERT)

    # page elem function
    def wait_until_page_generate(self):
        return self.wait.until(presence_of_element_located(self.SPINNER_OFF))

    # general function
    @abc.abstractmethod
    def get_unique(self):
        """

        :return: unique wed element on page else throw NoSuchElement exception
        """
        return

    def get_current_page(self):
        self.wait_until_page_generate()
        return self

    def is_alert_show(self):
        try:
            if self.alert:
                return True
        except NoSuchElementException:
            return False

    def is_current_page(self):
        try:
            self.get_unique()
            return True
        except NoSuchElementException:
            return False

    def __eq__(self, other):
        return isinstance(other, self.__class__)
