import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from envars import BASE_URL_YANDEX_PASSPORT
from pages.base_page import BasePage


class AuthPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

        # Поле логин
        self.field_login = lambda: self.driver.find_element(By.ID, 'passp-field-login')
        # Поле пароль
        self.field_password = lambda: self.driver.find_element(By.ID, 'passp-field-passwd')
        # Кнопка 'Войти'
        self.button_enter = lambda: self.driver.find_element(By.ID, 'passp:sign-in')
        # Лоудер
        self.pop_up = lambda: self.driver.find_element(By.CLASS_NAME,'.passp-page-overlay_showed')
        # Кнопка 'Создать id'
        self.button_create_id = lambda: self.driver.find_element(By.ID, 'passp:exp-register')
        # Кнопка 'Войти по qr коду'
        self.enter_by_qr = lambda: self.driver.find_element(By.CLASS_NAME, '.AuthPasswordForm-qr-button')
        # Кнопка 'Войти с помощью пароля'
        self.enter_by_password = lambda: self.driver.find_element(By.CLASS_NAME, '.MagicPromoPage-controls')
        # Аватар
        self.avatar_email = lambda: self.driver.find_element(By.CSS_SELECTOR, 'button.zen-ui-avatar')
        # Логин в аватаре
        self.login_in_avatar = lambda: self.driver.find_element(By.CSS_SELECTOR, 'li.Menu-Item_type_info')
        # Кнопка почта
        self.mail_button = lambda: self.driver.find_element(By.XPATH, ("//button[contains(@data-type, 'login')]"))
        # Кнопка телефон
        self.phone_button = lambda: self.driver.find_element(By.XPATH, ("//button[contains(@data-type, 'phone')]"))
        # Поле телефон
        self.field_phone = lambda: self.driver.find_element(By.ID, 'passp-field-phone')
        # Логин в аватаре
        self.title_enter_code_from_sms = lambda: self.driver.find_element(By.CSS_SELECTOR, '.Title_align_center')
        # Поле код из смс
        self.field_phone_code_sms = lambda: self.driver.find_element(By.ID, 'passp-field-phoneCode')
        # Логин не подходит
        self.title_login_field = lambda: self.driver.find_element(By.ID, 'field:input-login:hint')
        # Неверный пароль
        self.title_password_field = lambda: self.driver.find_element(By.ID, 'field:input-passwd:hint')
        # Неверный номер телефона
        self.title_phone_field = lambda: self.driver.find_element(By.ID, 'field:input-phone:hint')





    @allure.step('Открытие страницы авторизации')
    def open_auth_page(self):
        self.driver.get(BASE_URL_YANDEX_PASSPORT)

    @allure.step('Нажать кнопку "Войти"')
    def click_button_enter(self):
        self.wait_short.until(EC.element_to_be_clickable((By.ID, 'passp:sign-in')))
        self.button_enter().click()
        return self

    @allure.step('Нажать кнопку "Телефон"')
    def click_button_phone(self):
        self.wait_short.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@data-type, "phone")]')))
        self.phone_button().click()
        return self

    @allure.step('Нажать кнопку "Создать ID"')
    def click_button_create_id(self):
        self.wait_short.until(EC.element_to_be_clickable((By.ID, 'passp:exp-register')))
        self.button_create_id().click()
        return self

    @allure.step('Нажать кнопку "Войти по qr коду"')
    def click_enter_by_qr(self):
        self.wait_short.until(EC.element_to_be_clickable((By.CLASS_NAME, '.AuthPasswordForm-qr-button')))
        self.enter_by_qr().click()
        return self

    @allure.step('Нажать кнопку "Войти с помощью пароля"')
    def click_enter_by_password(self):
        self.wait_short.until(EC.element_to_be_clickable((By.CLASS_NAME, '.MagicPromoPage-controls')))
        self.enter_by_password().click()
        return self

    @allure.step('Нажать кнопку Аватара почты')
    def click_avatar(self):
        self.wait_short.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.zen-ui-avatar')))
        self.avatar_email().click()
        return self

    @allure.step('Ввод логина')
    def enter_login(self, login: str):
        self.field_login().send_keys(login)
        return self

    @allure.step('Клик по кнопке Почта')
    def click_mail_button(self):
        self.wait_short.until(EC.element_to_be_clickable((By.XPATH, ("//button[contains(@data-type, 'login')]"))))
        self.mail_button().click()
        return self

    @allure.step('Ввод пароля')
    def enter_password(self, password: str):
        self.wait_short.until(EC.element_to_be_clickable((By.ID, 'passp-field-passwd')))
        self.field_password().send_keys(password)
        return self

    @allure.step('Ввод телефона')
    def enter_phone(self, number_phone: str):
        self.wait_short.until(EC.element_to_be_clickable((By.ID, 'passp-field-phone')))
        self.field_phone().send_keys(number_phone)
        return self

    @allure.step('Получить логин')
    def login_mail(self):
        self.wait_short.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.Menu-Item_type_info')))
        text = self.login_in_avatar().get_attribute('textContent')
        return text

    @allure.step('Тайтл получить код из смс')
    def text_from_title_enter_code_from_sms(self):
        self.wait_short.until(EC.element_to_be_clickable((By.ID, 'passp-field-phoneCode')))
        text = self.title_enter_code_from_sms().get_attribute('textContent')
        return text

    @allure.step('Тайтл неверный логин')
    def text_from_title_login_field(self):
        self.wait_short.until(EC.element_to_be_clickable((By.ID, 'field:input-login:hint')))
        text = self.title_login_field().get_attribute('textContent')
        return text

    @allure.step('Тайтл неверный пароль')
    def text_from_title_password_field(self):
        self.wait_short.until(EC.element_to_be_clickable((By.ID, 'field:input-passwd:hint')))
        text = self.title_password_field().get_attribute('textContent')
        return text

    @allure.step('Тайтл неверный пароль')
    def text_from_title_phone_field(self):
        self.wait_short.until(EC.element_to_be_clickable((By.ID, 'field:input-phone:hint')))
        text = self.title_phone_field().get_attribute('textContent')
        return text