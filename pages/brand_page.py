from selenium.webdriver.common.by import By

from pages.products_page import ProductsPage


class BrandPage(ProductsPage):
    BRAND_BTN = By.XPATH, '//div[@class="list-group slimscroll"]/a[4]'
    brand_name = "baseus"
    BRAND_ITEMS = By.CSS_SELECTOR, "article"
    CORRECT_BRAND = By.XPATH, f'//div[@class="clearfix"]/div[contains(text(), {brand_name})]'

    def get_brand(self):
        self.click_button(self.BRAND_BTN)

    def brand_nr(self):
        brand_items = list(self.get_elements(*self.BRAND_ITEMS))
        correct_brand = list(self.get_elements(*self.CORRECT_BRAND))
        if len(correct_brand) == len(brand_items):
            print('Filtrarea a fost facuta corect')



