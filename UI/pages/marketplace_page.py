# -*- encoding=utf8 -*-
import allure

from UI.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MarketplacePage(BasePage):
    TITLE_MARKETPLACE = "Buy & Sell Items In Our Marketplace with Bitcoin and Cryptocurrency"
    TITLE_MARKETPLACE_CARS = "Buy Exotic Cars with Bitcoin In our Cryptocurrency Marketplace"
    TITLE_GIFT_CARDS = "Buy Gift Cards with Crypto & Bitcoin | Crypto Exchange"
    TITLE_DOMAINS = "Buy Premium Domains with Bitcoin in our Cryptocurrency Marketplace"
    TITLE_WATCHES = "Buy Luxury Watches with Bitcoin in Our Cryptocurrency Marketplace"
    TITLE_USERNAMES = "Buy Social Media Account Usernames with Crypto"
    TITLE_ESTATE = "Buy a House with Bitcoin in our Cryptocurrency Real Estate Marketplace"
    GIFT_CARDS = By.XPATH, "//span[text()='Gift Cards']"
    DOMAINS = By.XPATH, "//span[text()='Domains']"
    CARS = By.XPATH, "//span[text()='Cars']"
    WATCHES = By.XPATH, "//span[text()='Watches']"
    USERNAMES = By.XPATH, "//span[text()='Usernames']"
    REAL_ESTATE = By.XPATH, "//span[text()='Real Estate']"
    LAMBORGHINI = By.XPATH, "//a[@class='car-brands__item' and .//div[@class='car-brands__item-bg lamborghini']]"
    CHOOSE_ITEM = By.CLASS_NAME, "marketplace-product__image"
    ADD_TO_CART_BTN = By.CSS_SELECTOR, ".button.addtocart[type='submit']"
    CARD = By.XPATH, "//*[@class='my-header_cart-prod']//span[@class='notify-count prod-true']"

    def main_title(self):
        self.get_title(self.TITLE_MARKETPLACE)

    @allure.step("Отображение вкладки Cars")
    def title_cars(self):
        self.get_title(self.TITLE_MARKETPLACE_CARS)

    @allure.step("Отображение вкладки Giftcards")
    def title_gift_cards(self):
        self.get_title(self.TITLE_GIFT_CARDS)

    @allure.step("Отображение вкладки Domains")
    def title_domains(self):
        self.get_title(self.TITLE_DOMAINS)

    @allure.step("Отображение вкладки Watches")
    def title_watches(self):
        self.get_title(self.TITLE_WATCHES)

    @allure.step("Отображение вкладки Usernames")
    def title_usernames(self):
        self.get_title(self.TITLE_USERNAMES)

    @allure.step("Отображение вкладки Real Estate")
    def title_real_estate(self):
        self.get_title(self.TITLE_ESTATE)

    @allure.step("Клик по вкладке Giftcards")
    def giftcards(self):
        self.click(self.GIFT_CARDS)

    @allure.step("Клик по вкладке Domains")
    def domains(self):
        self.click(self.DOMAINS)

    @allure.step("Клик по вкладке Cars")
    def cars(self):
        self.click(self.CARS)

    @allure.step("Клик по вкладке Watches")
    def watches(self):
        self.click(self.WATCHES)

    @allure.step("Клик по вкладке Usernames")
    def usernames(self):
        self.click(self.USERNAMES)

    @allure.step("Отображение категории Real Estate")
    def realestate(self):
        self.click(self.REAL_ESTATE)

    @allure.step("Выбор категории авто LAMBORGHINI")
    def click_lamborghini(self):
        self.get_element(self.LAMBORGHINI)

    @allure.step("Выбор товара")
    def choose_item(self):
        a = self.get_elements(self.CHOOSE_ITEM)[0]
        a.click()

    @allure.step("Добавление товара в корзину")
    def click_add_to_card(self):
        self.click(self.ADD_TO_CART_BTN)

    @allure.step("Проверка корзины")
    def get_card(self):
        card = self.get_element(self.CARD)
        return card
