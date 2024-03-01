from selenium.webdriver.common.by import By


from pages.products_page import ProductsPage


class PricePage(ProductsPage):
    LOW_PRICE = By.XPATH, '//input[@placeholder="199"]'
    HIGH_PRICE = By.XPATH, '//input[@placeholder="943"]'
    PRICE_BUTTON = By.XPATH, '//button[@type="submit" and contains(text(), "filtru")]'
    ELEMENTS_LIST = By.XPATH, '//strong[contains(text(), "lei")]'

    def lower_price(self, lower_price):
        low_price_box = self.driver.find_element(self.LOW_PRICE)
        low_price_box.send_keys(lower_price)

    def upper_price(self, upper_price):
        high_price_box = self.driver.find_element(self.HIGH_PRICE)
        high_price_box.send_keys(upper_price)

    def price_box(self):
        price_submit = self.driver.find_element(self.PRICE_BUTTON)
        price_submit.click()

    def get_product_prices(self):
        element_list = self.driver.find_elements(self.ELEMENTS_LIST)
        price_list_text = list()
        for element in element_list:
            price_list_text.append(element.text)
        price_list = list()
        for price in price_list_text:
            number, moneda = price.split(" ")
            if "." in number:
                first, second = number.split(".")
                number = first + second
            number = number.replace(",", ".")
            price_list.append(float(number))
        print(f'Sunt {len(price_list)} elemente filtrate de pagina')
        price_list_final = list()
        for price in price_list:
            if 200 < price < 500:
                price_list_final.append(price)
        print(f'Sunt {len(price_list_final)} elemente filtrate manual')
        if price_list_final == price_list:
            print('Filtrarea a fost efectuata corect')
        else:
            print('Filtrarea nu a fost efectuata corect')
