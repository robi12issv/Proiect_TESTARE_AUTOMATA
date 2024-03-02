from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.webdriver import WebDriver


class BasePage(WebDriver):
    MAIN_PAGE = 'https://www.vexio.ro/'

    def load(self):
        self.driver.get(self.MAIN_PAGE)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def click_button(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)

    def get_elements(self, *locator):
        elements = self.driver.find_elements(*locator)
        return elements
