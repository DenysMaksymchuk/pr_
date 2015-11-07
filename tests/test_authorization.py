import allure
from allure.constants import AttachmentType
import pytest
import time

__author__ = 'dmakstc'


@pytest.mark.usefixtures('load_model_auth_check')
class TestLogin:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_correct_auth(self):
        try:
            with pytest.allure.step('Valid login test'):
                current_page = self.model.get_welcome_page()
                current_page.input_in_username_field('admin')
                current_page.input_in_password_field('nimda')
                current_page = current_page.submit_button_click()
                assert current_page == self.model.persons_page
        except Exception:
            allure.attach('screenshot', self.model.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_incorrect_auth(self):
        try:
            with pytest.allure.step('Invalid login test'):
                current_page = self.model.get_welcome_page()
                current_page.input_in_username_field('incorrect')
                current_page.input_in_password_field('incorrect')
                current_page = current_page.submit_button_click()
                assert current_page.is_alert_show()
        except Exception:
            allure.attach('screenshot', self.model.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    def test_quick_auth(self):
        try:
            with pytest.allure.step('test general function login()'):
                current_page = self.model.get_welcome_page()
                current_page.login()
                assert self.model.persons_page.is_current_page()
        except Exception:
            allure.attach('screenshot', self.model.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    def test_checkbox_remind_me_auth(self):
        try:
            with pytest.allure.step('test checkbox remind me'):
                current_page = self.model.get_welcome_page()
                current_page.set_remind_me_checkbox_state(True)
                current_page = current_page.login()
                current_page = current_page.logout()
                current_page = current_page.submit_button_click()
                assert self.model.persons_page == current_page
        except Exception:
            allure.attach('screenshot', self.model.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise
