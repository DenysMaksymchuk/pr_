import time

from selenium.webdriver.common.by import By

from pages.internal_page import InternalPage
from web_elements_util.utils import checkbox_set_state

__author__ = 'dmakstc'


class PersonsPage(InternalPage):
    # locators
    PERSONS_PAGE_ID = (By.CSS_SELECTOR, ".fa.fa-user.text-danger")

    ###
    #  TO FILTER
    ###
    # button
    REFRESH_UPPER_BUTTON = (By.XPATH, "//p[1]/*[contains(@class, 'personFilterUpdateButton')]")
    REFRESH_BOTTOM_BUTTON = (By.XPATH, "//p[2]/*[contains(@class, 'personFilterUpdateButton')]")
    # check box
    GENDER_MALE_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[1]/div[2]/div[@class='panel-body']/div[1]/label/input")
    GENDER_FEMALE_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[1]/div[2]/div[@class='panel-body']/div[2]/label/input")
    GENDER_NOT_DEFINED_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[1]/div[2]/div[@class='panel-body']/div[3]/label/input")
    TYPE_APPLICANT_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[1]/label/input")
    TYPE_STUDENT_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[2]/label/input")
    TYPE_SCIENTIST_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[3]/label/input")
    TYPE_EMPLOYEE_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[4]/label/input")
    TYPE_GRADUATE_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[5]/label/input")
    TYPE_OUTSIDER_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[6]/label/input")
    NEED_HOSTEL_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[3]/div[2]/div[@class='panel-body']/div[1]/label/input")
    DO_NOT_NEED_HOSTEL_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[3]/div[2]/div[@class='panel-body']/div[2]/label/input")
    BOUND_TO_MILITARY_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[4]/div[2]/div[@class='panel-body']/div[1]/label/input")
    NOT_BOUND_TO_MILITARY_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[4]/div[2]/div[@class='panel-body']/div[2]/label/input")
    RESIDENT_FOREIGNER_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[5]/div[2]/div[@class='panel-body']/div[1]/label/input")
    RESIDENT_NOT_FOREIGNER_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[5]/div[2]/div[@class='panel-body']/div[2]/label/input")

    # web elements
    @property
    def refresh_upper_button(self):
        return self.driver.find_element(*self.REFRESH_UPPER_BUTTON)

    @property
    def refresh_bottom_button(self):
        return self.driver.find_element(*self.REFRESH_BOTTOM_BUTTONN)

    @property
    def gender_male_checkbox(self):
        return self.driver.find_element(*self.GENDER_MALE_CHECKBOX)

    @property
    def gender_female_checkbox(self):
        return self.driver.find_element(*self.GENDER_FEMALE_CHECKBOX)

    @property
    def gender_not_defined_checkbox(self):
        return self.driver.find_element(*self.GENDER_NOT_DEFINED_CHECKBOX)

    @property
    def type_applicant_checkbox(self):
        return self.driver.find_element(*self.TYPE_APPLICANT_CHECKBOX)

    @property
    def type_student_checkbox(self):
        return self.driver.find_element(*self.TYPE_STUDENT_CHECKBOX)

    @property
    def type_scientist_checkbox(self):
        return self.driver.find_element(*self.TYPE_SCIENTIST_CHECKBOX)

    @property
    def type_employee_checkbox(self):
        return self.driver.find_element(*self.TYPE_EMPLOYEE_CHECKBOX)

    @property
    def type_graduate_checkbox(self):
        return self.driver.find_element(*self.TYPE_GRADUATE_CHECKBOX)

    @property
    def type_outsider_checkbox(self):
        return self.driver.find_element(*self.TYPE_OUTSIDER_CHECKBOX)

    @property
    def need_hostel_checkbox(self):
        return self.driver.find_element(*self.NEED_HOSTEL_CHECKBOX)

    @property
    def do_not_need_hostel_checkbox(self):
        return self.driver.find_element(*self.DO_NOT_NEED_HOSTEL_CHECKBOX)

    @property
    def bound_to_military_checkbox(self):
        return self.driver.find_element(*self.BOUND_TO_MILITARY_CHECKBOX)

    @property
    def not_bound_to_military_checkbox(self):
        return self.driver.find_element(*self.NOT_BOUND_TO_MILITARY_CHECKBOX)

    @property
    def resident_foreigner_checkbox(self):
        return self.driver.find_element(*self.RESIDENT_FOREIGNER_CHECKBOX)

    @property
    def resident_not_foreigner_checkbox(self):
        return self.driver.find_element(*self.RESIDENT_NOT_FOREIGNER_CHECKBOX)

    # page elem function

    # general function
    def get_unique(self):
        return self.driver.find_element(*self.PERSONS_PAGE_ID)

    # def check_all_gender(self):
    #     checkbox_set_state(self.gender_male_checkbox, True)
    #     time.sleep(1)
    #     checkbox_set_state(self.gender_female_checkbox, True)
    #     time.sleep(1)
    #     checkbox_set_state(self.gender_not_defined_checkbox, True)
    #     time.sleep(1)
    #
    # def check_all_type(self):
    #     checkbox_set_state(self.type_applicant_checkbox, True)
    #     time.sleep(1)
    #     checkbox_set_state(self.type_student_checkbox, True)
    #     time.sleep(1)
    #     checkbox_set_state(self.type_scientist_checkbox, True)
    #     time.sleep(1)
    #     checkbox_set_state(self.type_employee_checkbox, True)
    #     time.sleep(1)
    #     checkbox_set_state(self.type_graduate_checkbox, True)
    #     time.sleep(1)
    #     checkbox_set_state(self.type_outsider_checkbox, True)
    #     time.sleep(1)
    #
    # def check_all_hostel(self):
    #     checkbox_set_state(self.need_hostel_checkbox, True)
    #     time.sleep(1)
    #     checkbox_set_state(self.do_not_need_hostel_checkbox, True)
    #     time.sleep(1)
    #
    # def check_all_military(self):
    #     checkbox_set_state(self.bound_to_military_checkbox, True)
    #     time.sleep(1)
    #     checkbox_set_state(self.not_bound_to_military_checkbox, True)
    #     time.sleep(1)
    #
    # def check_all_foreigner(self):
    #     checkbox_set_state(self.resident_foreigner_checkbox, True)
    #     time.sleep(1)
    #     checkbox_set_state(self.resident_not_foreigner_checkbox, True)
    #     time.sleep(1)
