import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from locators import Locators


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen")
    browser = webdriver.Chrome(options=chrome_options)
    browser = webdriver.Chrome()
    browser.get(constants.MAIN_URL)
    yield browser
    browser.quit()

@pytest.fixture
def logged_user(driver):
    driver.get(constants.LOGIN_PAGE)
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locators.LOGIN_EMAIL_INPUT)))
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.EMAIL_FOR_LOGIN)
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.PASSWORD_FOR_LOGIN)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((Locators.PERSONAL_ACCOUNT)))
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    return driver


def wait_for_element_located(driver, locator, time, condition):
        return WebDriverWait(driver, time).until(condition(locator))