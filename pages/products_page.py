from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage


class ProductsPage(MainPage):
    ALL_PRODUCTS = By.XPATH, '//*[@class="h5 name"]/a[@data-ecproduct="true"]'
    CORRECT_PRODUCTS = By.XPATH, '//a[contains(text(), "Incarcator")]'

    def get_products(self, product_name):
        self.driver.get(self.MAIN_PAGE)
        search_box = self.driver.find_element(self.SEARCH_BOX)
        search_box = WebDriverWait(self.driver, 10).until((EC.presence_of_element_located(self.SEARCH_BOX)))
        search_box.send_keys(product_name)
        search_button = self.driver.find_element(self.SEARCH_BUTTON)
        search_button.click()

    def products_number(self):
        all_products_list = self.driver.find_elements(self.ALL_PRODUCTS)
        print(len(all_products_list))

    def products_type(self):
        all_products_list = self.driver.find_elements(self.ALL_PRODUCTS)
        correct_products_list = self.driver.find_elements(self.CORRECT_PRODUCTS)
        other_products = []
        for i in all_products_list:
            if i not in correct_products_list:
                other_products.append(i)
        for i in correct_products_list:
            if i not in all_products_list:
                other_products.append(i)
        print(f"Sunt {len(other_products)} produse in plus")
        return other_products
