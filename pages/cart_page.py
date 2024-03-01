from selenium.webdriver.common.by import By

from pages.products_page import ProductsPage


class CartPage(ProductsPage):
    WANTED_PRODUCT = By.XPATH, '//*[@class="h5 name"]/a[@title="Incarcator de retea UGREEN UGREEN CD289 Power Charger, 2x USB-C, 1x USB-A, GaN, 140W, 2m Cable (Silver)"]'
    CART_BUTTON1 = By.ID, "add_to_cart_button"
    CART_BUTTON2 = By.XPATH, '//*[@href=" /adaugaincos-2038239"]'

    def choose_product(self):
        wanted_product = self.driver.find_element(self.WANTED_PRODUCT)
        wanted_product.click()

    def add_to_cart(self):
        cart_button = self.driver.find_element(self.CART_BUTTON1)
        cart_button.click()

    def add_2_to_cart(self):
        cart_button = self.driver.find_element(self.CART_BUTTON2)
        cart_button.click()

    def cart_title(self):
        if self.driver.title != 'Adaugaincos':
            print(self.driver.title)

    # def cart_title(self):
    #     assert self.driver.title == 'Nu uita sa trimiti comanda', 'Nu am ajuns pe pagina cosului'
