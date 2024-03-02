import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class MainPage(BasePage):
    SEARCH_BOX = (By.XPATH, '//input[@id="search-box" and @spellcheck]')
    SEARCH_BUTTON = (By.XPATH, '//span[@class="input-group-btn"]/button[@type="submit"]')
    ARTICLES = (By.CSS_SELECTOR, 'article[data-sna-product="true"]')

    def enter_item(self, product_name):
        self.enter_text(self.SEARCH_BOX, product_name)

    def enter_product(self, product):
        self.enter_text(self.SEARCH_BOX, product)

    def click_search_button(self):
        self.click_button(self.SEARCH_BUTTON)

    def get_url_title(self):
        print(self.driver.title)
        # return self.driver.title()

    def get_articles(self):
        all_articles_list = self.get_elements(*self.ARTICLES)
        all_articles = []
        for article in all_articles_list:
            all_articles.append(article)
        assert len(all_articles) > 0, "No articles"

    # def get_articles(self):
    #     all_articles_list = self.get_elements(*self.ARTICLES)
    #     all_articles = []
    #     for article in all_articles_list:
    #         all_articles.append(article)
    #     if len(all_articles) > 0:
    #         print("Cautare efectuata cu succes")
    #     else:
    #         print("Produsul cautat nu exista")


