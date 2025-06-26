from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestStellarBurgers:
    def test_transition_through_logo(self, driver, wait_for_element_located):
        wait_for_element_located(driver, time=5, locator=Locators.LOGO_STELLAR_BURGERS, condition=EC.visibility_of_element_located)
        driver.find_element(*Locators.LOGO_STELLAR_BURGERS).click()
        assert wait_for_element_located(driver, time=5, locator=Locators.CREATE_BURGER, condition=EC.visibility_of_element_located)

    def test_transition_through_constructor(self, driver, wait_for_element_located):
        wait_for_element_located(driver, time=5, locator=Locators.CONSTRUCTOR_BUTTON, condition=EC.visibility_of_element_located)
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert wait_for_element_located(driver, time=5, locator=Locators.CREATE_BURGER, condition=EC.visibility_of_element_located)