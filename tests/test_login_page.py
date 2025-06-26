from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
import constants


class TestStellarBurgers:
    def test_login_personal_account_button(self, driver, wait_for_element_located):
        wait_for_element_located(driver, time=7, locator=Locators.LOGIN_IN_ACCOUNT, condition=EC.element_to_be_clickable)
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        wait_for_element_located(driver, time=7, locator=Locators.LOGIN_BUTTON, condition=EC.visibility_of_element_located)
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.EMAIL_FOR_LOGIN)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.PASSWORD_FOR_LOGIN)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait_for_element_located(driver, time=10, locator=Locators.PERSONAL_ACCOUNT, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert wait_for_element_located(driver, time=17, locator=Locators.LOGOUT_BUTTON, condition=EC.visibility_of_element_located)
    def test_login_in_account_button(self, driver, wait_for_element_located):
        wait_for_element_located(driver, time=7, locator=Locators.LOGIN_IN_ACCOUNT, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        wait_for_element_located(driver, time=7, locator=Locators.LOGIN_EMAIL_INPUT, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.EMAIL_FOR_LOGIN)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.PASSWORD_FOR_LOGIN)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait_for_element_located(driver, time=10, locator=Locators.PERSONAL_ACCOUNT, condition=EC.visibility_of_element_located)
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert wait_for_element_located(driver, time=17, locator=Locators.LOGOUT_BUTTON, condition=EC.visibility_of_element_located)

    def test_login_button_on_registration_page(self, driver, wait_for_element_located):
        wait_for_element_located(driver, time=7, locator=Locators.LOGIN_IN_ACCOUNT, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        wait_for_element_located(driver, time=7, locator=Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()
        wait_for_element_located(driver, time=7, locator=Locators.LOGIN_BUTTON_ON_PAGES, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.LOGIN_BUTTON_ON_PAGES).click()
        wait_for_element_located(driver, time=7, locator=Locators.LOGIN_BUTTON, condition=EC.visibility_of_element_located)
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.EMAIL_FOR_LOGIN)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.PASSWORD_FOR_LOGIN)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait_for_element_located(driver, time=3, locator=Locators.PERSONAL_ACCOUNT, condition=EC.visibility_of_element_located)
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert wait_for_element_located(driver, time=17, locator=Locators.LOGOUT_BUTTON, condition=EC.visibility_of_element_located)
    def test_login_restore_password_page(self, driver, wait_for_element_located):
        wait_for_element_located(driver, time=3, locator=Locators.LOGIN_IN_ACCOUNT, condition=EC.visibility_of_element_located)
        driver.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        wait_for_element_located(driver, time=5, locator=Locators.RESTORE_PASSWORD_BUTTON, condition=EC.visibility_of_element_located)
        driver.find_element(*Locators.RESTORE_PASSWORD_BUTTON).click()
        wait_for_element_located(driver, time=5, locator=Locators.LOGIN_BUTTON_ON_PAGES, condition=EC.visibility_of_element_located)
        driver.find_element(*Locators.LOGIN_BUTTON_ON_PAGES).click()
        wait_for_element_located(driver, time=5, locator=Locators.LOGIN_EMAIL_INPUT, condition=EC.visibility_of_element_located)
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.EMAIL_FOR_LOGIN)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.PASSWORD_FOR_LOGIN)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait_for_element_located(driver, time=10, locator=Locators.PERSONAL_ACCOUNT, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert wait_for_element_located(driver, time=10, locator=Locators.LOGOUT_BUTTON, condition=EC.visibility_of_element_located)