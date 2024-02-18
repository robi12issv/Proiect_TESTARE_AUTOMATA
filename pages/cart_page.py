import time
from selenium.webdriver.common.by import By

from pages.products_page import ProductsPage


class CartPage(ProductsPage):

    def choose_product(self):
        wanted_product = self.driver.find_element(By.XPATH, '//*[@class="h5 name"]/a[@title="Incarcator de retea UGREEN UGREEN CD289 Power Charger, 2x USB-C, 1x USB-A, GaN, 140W, 2m Cable (Silver)"]')
        wanted_product.click()
        time.sleep(2)

    def add_to_cart(self):
        cart_button = self.driver.find_element(By.ID, "add_to_cart_button")
        cart_button.click()
        time.sleep(3)

    def add_2_to_cart(self):
        cart_button = self.driver.find_element(By.XPATH, '//*[@href=" /adaugaincos-2038239"]')
        cart_button.click()
        time.sleep(3)

    # def cart_title(self):
    #     if self.driver.title != 'Adaugaincos':
    #         print(self.driver.title)

    def cart_title(self):
        assert self.driver.title == 'Nu uita sa trimiti comanda', 'Nu am ajuns pe pagina cosului'
