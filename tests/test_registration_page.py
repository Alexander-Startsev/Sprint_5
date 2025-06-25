from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conftest
import constants
from locators import Locators
from faker import Faker


class TestStellarBurgers:
    fake = Faker()
    def fake_email(self):
        return self.fake.email()

    def test_registration_new_user(self, driver):
        email = self.fake_email()
        password = "123456"
        conftest.wait_for_element_located(driver, time=3, locator=Locators.LOGIN_IN_ACCOUNT, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        conftest.wait_for_element_located(driver, time=3, locator=Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()
        driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(email+password)
        driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        conftest.wait_for_element_located(driver,time=5, locator=Locators.LOGIN_EMAIL_INPUT, condition=EC.visibility_of_element_located)
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.PERSONAL_ACCOUNT, condition=EC.element_to_be_clickable)
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert conftest.wait_for_element_located(driver, time=10, locator=Locators.LOGOUT_BUTTON, condition=EC.visibility_of_element_located)



    def test_registration_invalid_password(self, driver):
        conftest.wait_for_element_located(driver, time=3, locator=Locators.LOGIN_IN_ACCOUNT, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        conftest.wait_for_element_located(driver, time=3, locator=Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()
        driver.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(constants.NAME_FOR_REGISTRATION)
        driver.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(constants.EMAIL_FOR_LOGIN)
        driver.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys('12345')
        conftest.wait_for_element_located(driver, time=3, locator=Locators.REGISTRATION_BUTTON, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        assert conftest.wait_for_element_located(driver, time=17, locator=Locators.ERROR_MESSAGE, condition=EC.visibility_of_element_located)