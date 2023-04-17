import os

import allure
import pytest as pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from pages.auth_page import AuthPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    print("\nstart browser..")
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


@pytest.fixture()
def auth_page(driver):
    return AuthPage(driver)

