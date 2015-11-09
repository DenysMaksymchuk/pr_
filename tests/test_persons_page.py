import time

import pytest

__author__ = 'dmakstc'


@pytest.mark.usefixtures('load_model_for_persons_page')
class TestPersons(object):
    def test_1(self):
        time.sleep(1)
        assert self.model.persons_page == self.model.get_current_page()
        assert self.model.get_current_page().is_this_page_displayed()
        # self.model.get_current_page().check_all_gender()
        # self.model.get_current_page().check_all_type()
        # self.model.get_current_page().check_all_hostel()
        # self.model.get_current_page().check_all_military()
        # self.model.get_current_page().check_all_foreigner()
