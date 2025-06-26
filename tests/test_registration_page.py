from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import constants
import pytest

class TestStellarBurgers:
    @pytest.mark.parametrize("name,email,password", [("Тестовый Пользователь", "SashaStartsev25001@ya.ru", "123456")])
    def test_registration_new_user(self, driver, wait_for_element_located, name, email, password):
        wait_for_element_located(driver, 3, Locators.LOGIN_IN_ACCOUNT, EC.presence_of_element_located)
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()

        wait_for_element_located(driver, 3, Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE, EC.presence_of_element_located)
        driver.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()

        driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        wait_for_element_located(driver, 5, Locators.LOGIN_EMAIL_INPUT, EC.visibility_of_element_located)
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        wait_for_element_located(driver, 10, Locators.PERSONAL_ACCOUNT, EC.element_to_be_clickable)
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        assert wait_for_element_located(driver, 10, Locators.LOGOUT_BUTTON, EC.visibility_of_element_located)

    @pytest.mark.parametrize("name,email,password", [(constants.NAME_FOR_REGISTRATION, constants.EMAIL_FOR_LOGIN, "12345")])
    def test_registration_invalid_password(self, driver, wait_for_element_located, name, email, password):
        wait_for_element_located(driver, 3, Locators.LOGIN_IN_ACCOUNT, EC.presence_of_element_located)
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()

        wait_for_element_located(driver, 3, Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE, EC.presence_of_element_located)
        driver.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()

        driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys(password)

        wait_for_element_located(driver, 3, Locators.REGISTRATION_BUTTON, EC.presence_of_element_located)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        assert wait_for_element_located(driver, 17, Locators.ERROR_MESSAGE, EC.visibility_of_element_located)