# -*- coding: utf-8 -*-
from PIL import ImageGrab
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def wait_short(self):
        return WebDriverWait(self.driver, 40)

    @property
    def wait(self):
        return self.driver.implicitly_wait(40)

    @staticmethod
    def is_element_present(element):
        """Проверка наличия элемента"""
        try:
            element
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def element_is_not_present(element):
        """Проверка отсутсвия элемента"""
        try:
            element
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def get_screenshot(name: str):
        filepath = f'my_image_{name}.png'
        screenshot = ImageGrab.grab()
        screenshot.save(filepath, 'PNG')