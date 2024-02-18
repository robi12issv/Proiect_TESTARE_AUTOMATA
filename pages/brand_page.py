from selenium.webdriver.common.by import By

from pages.products_page import ProductsPage


class BrandPage(ProductsPage):

    def get_brand(self):
        brand_btn = self.driver.find_element(By.XPATH, '//div[@class="list-group slimscroll"]/a[4]')
        brand_btn.click()

    def brand_nr(self):
        brand_name = "baseus"
        brand_items = list(self.driver.find_elements(By.CSS_SELECTOR, "article"))
        correct_brand = list(self.driver.find_elements(By.XPATH, f'//div[@class="clearfix"]/div[contains(text(), {brand_name})]'))
        if len(correct_brand) == len(brand_items):
            print('Filtrarea a fost facuta corect')



