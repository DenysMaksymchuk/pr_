import pytest
from selenium import webdriver
from site_model.model import Model

__author__ = 'dmakstc'


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--base_url", action="store", default="http://192.168.96.134:9000/")


@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture(scope="function")
def load_model_auth_check(request, browser_type, base_url):
    """
    Fixture is used to perform all tests, use it in your tests like >>>  def test_method(app)
    It performs all tests in one browser, because of (scope="session")
    If it needs to perform tests in another browser,
    you can write in the console something like >>> py.test --browser "chrome"
    :return: new Application with chosen or default params
    """
    if browser_type == "firefox":
        driver = webdriver.Firefox()
        driver.get(base_url)
    request.addfinalizer(driver.quit)
    request.cls.model = Model(driver)
