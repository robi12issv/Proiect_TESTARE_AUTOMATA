from selenium.webdriver.common.by import By

from pages.brand_page import BrandPage


class CartPage(BrandPage):
    WANTED_PRODUCT = (By.XPATH, '//*[@class="h5 name"]/a[@title="Incarcator de retea Baseus GaN5 Pro, 2 porturi USB C si 1 port USB, Cablu USB C la USB C, 140W, Negru"]')
    CART_BUTTON1 = (By.ID, "add_to_cart_button")
    CART_BUTTON2 = (By.XPATH, '//*[@href=" /adaugaincos-1949700"]')
    TITLE = 'Incarcator de retea Baseus GaN5 Pro, 2 porturi USB C si 1 port USB, Cablu USB C la USB C, 140W, Negru Pret: 289,99 lei - Vexio'

    def choose_product(self):
        self.click_button(self.WANTED_PRODUCT)

    def add_to_cart(self):
        self.click_button(self.CART_BUTTON1)

    def add_2_to_cart(self):
        self.click_button(self.CART_BUTTON2)

    def page_title(self, pg_title):
        if self.driver.title == pg_title == 'Nu uita sa trimiti comanda':
            print('Produsul a fost adaugat in cos')
        else:
            print('Produsul nu a fost adaugat in cos')
        print(self.driver.title)

    def cart_title(self):
        assert self.driver.title == 'Nu uita sa trimiti comanda', 'Produsul nu a fost adaugat in cos'

    # def product_page(self):
    #     assert self.driver.title == 'Just a moment...', 'A aparut pagina de verificare, testul nu mai poate continua.'

    def product_page(self):
        assert self.driver.title == self.TITLE, 'A aparut pagina de verificare, testul nu mai poate continua.'

