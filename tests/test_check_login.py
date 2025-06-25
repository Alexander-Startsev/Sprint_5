from selenium.webdriver.support import expected_conditions as EC

import conftest
from locators import Locators
from constants import PROFILE_CABINET

class TestStellarBurgers:
    def test_login(self, driver, logged_user):
        conftest.wait_for_element_located(driver, time=17, locator=Locators.PERSONAL_ACCOUNT, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        conftest.wait_for_element_located(driver, time=17, locator=Locators.LOGOUT_BUTTON, condition=EC.presence_of_element_located)
        assert PROFILE_CABINET == driver.current_url