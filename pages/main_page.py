from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.webdriver import WebDriver


class MainPage(WebDriver):
    MAIN_PAGE = 'https://www.vexio.ro/'
    SEARCH_BOX = By.XPATH, '//input[@id="search-box" and @spellcheck]'
    SEARCH_BUTTON = By.XPATH, '//span[@class="input-group-btn"]/button[@type="submit"]'

    def load(self):
        self.driver.get(self.MAIN_PAGE)

    def search_item(self, product_name):
        search_box = self.driver.find_element(self.SEARCH_BOX)
        search_box = WebDriverWait(self.driver, 10).until((EC.presence_of_element_located(self.SEARCH_BOX)))
        search_box.send_keys(product_name)

    def search_button(self):
        search_button = self.driver.find_element(self.SEARCH_BUTTON)
        search_button.click()

    def get_url_title(self):
        print(self.driver.title)
        # return self.driver.title()

