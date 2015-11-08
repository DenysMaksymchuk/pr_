from selenium.webdriver.common.by import By
from pages.internal_page import InternalPage

__author__ = 'max'


class DictionariesPage(InternalPage):
    # locators
    DICTIONARIES_PAGE_ID = (By.XPATH, "//i[@class ='fa fa-book text-danger']")
    DICTIONARIES_DROPDOWN = (By.XPATH, "//select[@ng-click ='pickDictionary()']")
    DICTIONARIES_PAGE_TABLE = (By.XPATH, "//table")
    BUTTON_DISPLAY_BY_10 = (By.XPATH, "//div[contains(@class,'ng-table-counts')]/button[1]")
    BUTTON_DISPLAY_BY_25 = (By.XPATH, "//div[contains(@class,'ng-table-counts')]/button[2]")
    BUTTON_DISPLAY_BY_50 = (By.XPATH, "//div[contains(@class,'ng-table-counts')]/button[3]")
    BUTTON_DISPLAY_BY_100 = (By.XPATH, "//div[contains(@class,'ng-table-counts')]/button[4]")
    PAGE_BUTTON_NEXT = (By.XPATH, "//ul[@class='pagination ng-table-pagination']/li/a[@ng-switch-when='next']")
    PAGE_BUTTON_PREV = (By.XPATH, "//ul[@class='pagination ng-table-pagination']/li/a[@ng-switch-when='prev']")

    # web elements
    @property
    def dictionaries_dropdown(self):
        return self.driver.find_element(*self.DICTIONARIES_DROPDOWN)

    @property
    def current_table(self):
        return self.driver.find_element(*self.DICTIONARIES_PAGE_TABLE)

    @property
    def button_display_by_10(self):
        return self.driver.find_element(*self.BUTTON_DISPLAY_BY_10)

    @property
    def button_display_by_25(self):
        return self.driver.find_element(*self.BUTTON_DISPLAY_BY_25)

    @property
    def button_display_by_50(self):
        return self.driver.find_element(*self.BUTTON_DISPLAY_BY_50)

    @property
    def button_display_by_100(self):
        return self.driver.find_element(*self.BUTTON_DISPLAY_BY_100)

    @property
    def button_next(self):
        return self.driver.find_element(*self.PAGE_BUTTON_NEXT)
    @property
    def button_prev(self):
        return self.driver.find_element(*self.PAGE_BUTTON_PREV)

    # page elem function

    # general function
    def get_unique(self):
        pass
