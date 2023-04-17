import allure
import parametrize_from_file
import pysnooper


@parametrize_from_file
@pysnooper.snoop()
def test_correct_login_and_password(auth_page, login, password):
    with allure.step('Шаг 1.Перейти на страницу авторизации'):
        auth_page.open_auth_page()
    with allure.step('Шаг 2.Клик по кнопке почта'):
        auth_page.click_mail_button()
    with allure.step('Шаг 3. Ввести логин'):
        auth_page.enter_login(login)
    with allure.step('Шаг 4. Нажать кнопку "Войти"'):
        auth_page.click_button_enter()
    with allure.step('Шаг 5. Ввести пароль'):
        auth_page.enter_password(password)
    with allure.step('Шаг 6. Нажать кнопку "Войти"'):
        auth_page.click_button_enter()
    with allure.step('Шаг 7. Кликнуть по аватару почты'):
        auth_page.click_avatar()
    with allure.step('Шаг 8. Информация в аватаре совпадает с введённым логином'):
        assert auth_page.login_mail() in login
    with allure.step('Шаг 9. Сделать скриншот'):
        auth_page.get_screenshot(login)


@parametrize_from_file
@pysnooper.snoop()
def test_correct_phone(auth_page, phone, phone_title):
    with allure.step('Шаг 1.Перейти на страницу авторизации'):
        auth_page.open_auth_page()
    with allure.step('Шаг 2.Клик по кнопке телефон'):
        auth_page.click_button_phone()
    with allure.step('Шаг 3. Ввести логин'):
        auth_page.enter_phone(phone)
    with allure.step('Шаг 4. Нажать кнопку "Войти"'):
        auth_page.click_button_enter()
    with allure.step('Шаг 5. Проверка тайтла '):
        assert phone_title in auth_page.text_from_title_enter_code_from_sms()
    with allure.step('Шаг 6. Сделать скриншот'):
        auth_page.get_screenshot(phone)


@parametrize_from_file
@pysnooper.snoop()
def test_incorrect_login(auth_page, login):
    with allure.step('Шаг 1.Перейти на страницу авторизации'):
        auth_page.open_auth_page()
    with allure.step('Шаг 2.Клик по кнопке почта'):
        auth_page.click_mail_button()
    with allure.step('Шаг 3. Ввести логин'):
        auth_page.enter_login(login)
    with allure.step('Шаг 4. Нажать кнопку "Войти"'):
        auth_page.click_button_enter()
    with allure.step('Шаг 5. Информация в аватаре совпадает с введённым логином'):
        assert "Такой логин" in auth_page.text_from_title_login_field()
    with allure.step('Шаг 6. Сделать скриншот'):
        auth_page.get_screenshot(login)


@parametrize_from_file
@pysnooper.snoop()
def test_incorrect_password(auth_page, login, password):
    with allure.step('Шаг 1.Перейти на страницу авторизации'):
        auth_page.open_auth_page()
    with allure.step('Шаг 2.Клик по кнопке почта'):
        auth_page.click_mail_button()
    with allure.step('Шаг 3. Ввести логин'):
        auth_page.enter_login(login)
    with allure.step('Шаг 4. Нажать кнопку "Войти"'):
        auth_page.click_button_enter()
    with allure.step('Шаг 5. Ввести пароль'):
        auth_page.enter_password(password)
    with allure.step('Шаг 6. Нажать кнопку "Войти"'):
        auth_page.click_button_enter()
    with allure.step('Шаг 8. Информация в аватаре совпадает с введённым логином'):
        assert 'Неверный пароль' == auth_page.text_from_title_password_field()
    with allure.step('Шаг 9. Сделать скриншот'):
        auth_page.get_screenshot(login)


@parametrize_from_file
@pysnooper.snoop()
def test_incorrect_phone(auth_page, phone):
    with allure.step('Шаг 1.Перейти на страницу авторизации'):
        auth_page.open_auth_page()
    with allure.step('Шаг 2.Клик по кнопке телефон'):
        auth_page.click_button_phone()
    with allure.step('Шаг 3. Ввести логин'):
        auth_page.enter_phone(phone)
    with allure.step('Шаг 4. Нажать кнопку "Войти"'):
        auth_page.click_button_enter()
    with allure.step('Шаг 5. Проверка тайтла '):
        assert 'Недопустимый формат номера' == auth_page.text_from_title_phone_field()
    with allure.step('Шаг 6. Сделать скриншот'):
        auth_page.get_screenshot(phone)
