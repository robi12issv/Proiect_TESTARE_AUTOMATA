import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.webdriver import WebDriver


class MainPage(WebDriver):

    def load(self):
        self.driver.get('https://www.vexio.ro/')

    def search_item(self, product_name):
        search_box = self.driver.find_element(By.XPATH, '//input[@id="search-box" and @spellcheck]')
        search_box = WebDriverWait(self.driver, 10).until((
            EC.presence_of_element_located((By.XPATH, '//input[@id="search-box" and @spellcheck]'))
        ))
        search_box.send_keys(product_name)

    def search_button(self):
        search_button = self.driver.find_element(By.XPATH, '//span[@class="input-group-btn"]/button[@type="submit"]')
        search_button.click()
        time.sleep(5)

    def get_url_title(self):
        print(self.driver.title)
        # return self.driver.title()

