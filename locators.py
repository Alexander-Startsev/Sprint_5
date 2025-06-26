from selenium.webdriver.common.by import By

class Locators():
    PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')# Кнопка "Личный Кабинет"
    REGISTRATION_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')  # Кнопка "Зарегистрироваться"
    LOGIN_IN_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]')# Кнопка "Войти в аккаунт"
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@type='text']")  # Инпут для логина на странице входа
    LOGIN_PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")  # Инпут для пароля на странице входа
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')# Кнопка "Войти" на странице входа
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')# Кнопка "Выйти" в Личном Кабинете
    REGISTRATION_BUTTON_ON_LOGIN_PAGE = (By.XPATH, '//a[contains(text(), "Зарегистрироваться")]')# Кнопка "Зарегистрироваться" на странице входа
    RESTORE_PASSWORD_BUTTON = (By.XPATH, '//a[contains(text(), "Восстановить пароль")]')# Кнопка "Восстановить пароль" на странице входа
    LOGIN_BUTTON_ON_PAGES = (By.XPATH, '//a[contains(text(), "Войти")]')# Кнопка "Войти" на странице регистрации
    REGISTRATION_NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')# Поле для ввода имени
    REGISTRATION_EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')# Поле для ввода email
    REGISTRATION_PASSWORD_INPUT = (By.NAME, 'Пароль')# Поле для ввода пароля
    ERROR_MESSAGE = (By.XPATH, '//p[text()="Некорректный пароль"]')# Некорректный пароль
    LOGO_STELLAR_BURGERS = (By.XPATH, '//div/a[@href="/"]')# Лого сайта
    BULKI_BUTTON = (By.XPATH, '//span[text()="Булки"]/parent::div')# Кнопка "Булки"
    SAUCE_BUTTON = (By.XPATH, '//span[text()="Соусы"]/parent::div')# Кнопка "Соусы"
    FILLING_BUTTON = (By.XPATH, '//span[text()="Начинки"]/parent::div')# Кнопка "Начинка"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//li/a[@href="/"]')# Кнопка "Конструктор"
    CREATE_BURGER = (By.XPATH, '//h1[text()="Соберите бургер"]')# Элемент "Соберите Бургер"
