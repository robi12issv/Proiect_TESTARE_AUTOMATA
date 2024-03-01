from selenium.webdriver.common.by import By

from pages.brand_page import BrandPage


class TestPage(BrandPage):

    def choose_product(self):
        wanted_product = self.driver.find_element(By.XPATH, '//*[@class="h5 name"]/a[@title="Incarcator de retea Baseus GaN5 Pro, 2 porturi USB C si 1 port USB, Cablu USB C la USB C, 140W, Negru"]')
        wanted_product.click()

    def add_to_cart(self):
        cart_button = self.driver.find_element(By.ID, "add_to_cart_button")
        cart_button.click()

    def add_2_to_cart(self):
        cart_button = self.driver.find_element(By.XPATH, '//*[@href=" /adaugaincos-1949700"]')
        cart_button.click()

    # def cart_title(self):
    #     if self.driver.title != 'Adaugaincos':
    #         print(self.driver.title)

    def cart_title(self):
        assert self.driver.title == 'Nu uita sa trimiti comanda', 'Nu am ajuns pe pagina cosului'
