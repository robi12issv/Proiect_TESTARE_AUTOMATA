import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.webdriver import WebDriver


class ProductsPage(WebDriver):

    def get_products(self, product_name):
        self.driver.get("https://www.vexio.ro/")
        time.sleep(2)
        search_box = self.driver.find_element(By.XPATH, '//input[@id="search-box" and @spellcheck]')
        search_box = WebDriverWait(self.driver, 10).until((
            EC.presence_of_element_located((By.XPATH, '//input[@id="search-box" and @spellcheck]'))
        ))
        time.sleep(3)
        search_box.send_keys(product_name)
        search_button = self.driver.find_element(By.XPATH, '//span[@class="input-group-btn"]/button[@type="submit"]')
        search_button.click()

    def products_number(self):
        all_products_list = self.driver.find_elements(By.XPATH, '//*[@class="h5 name"]/a[@data-ecproduct="true"]')
        print(len(all_products_list))

    def products_type(self):
        all_products_list = self.driver.find_elements(By.XPATH, '//*[@class="h5 name"]/a[@data-ecproduct="true"]')
        correct_products_list = self.driver.find_elements(By.XPATH, '//a[contains(text(), "Incarcator")]')
        other_products = []
        for i in all_products_list:
            if i not in correct_products_list:
                other_products.append(i)
        for i in correct_products_list:
            if i not in all_products_list:
                other_products.append(i)
        print(f"Sunt {len(other_products)} produse in plus")
        return other_products
