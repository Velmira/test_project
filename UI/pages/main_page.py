# -*- encoding=utf8 -*-
import allure

from UI.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    TITLE = "Leading Cryptocurrency and Bitcoin Exchange | Crypto Exchange"
    LOGIN_BUTTON = By.LINK_TEXT, "Login"
    SIGN_UP_FIELD = By.XPATH, "//input[@id='quick_signup' and @type='email']"
    SUBMIT_EMAIL_TO_SIGNUP_BUTTON = By.XPATH, "//button[@type='submit' and text()='Sign Up']"
    MARKETPLACE_TAB = By.XPATH, "//*[@id='header']/div[2]/div/div[2]/div[3]/a"
    ESCROW_TAB = By.XPATH, "//*[@id='header']/div[2]/div/div[2]/div[2]/a"
    EXCHANGE_TAB = By.XPATH, '//*[@id="header"]/div[2]/div/div[2]/div[1]/a'
    START_NEW_TRANSACTION_BTN = By.LINK_TEXT, "Start a New Transaction"
    TITLE_START_NEW_TRX = "Start New Transaction"
    CURRENCY_PAIRS_BTN = By.XPATH, '//i[@class="icon angle-right-icon"]'
    BNB_USD = By.XPATH, '//span[text()="BNB / USD"]'
    TRX_USD = By.XPATH, '//span[text()="TRX / USD"]'

    EMAIL_TO_SIGN_UP = "test123456789@gmail.com"

    def main_title(self):
        self.get_title(self.TITLE)

    @allure.step("Страница новой транзакции")
    def start_trx_title(self):
        self.get_title(self.TITLE_START_NEW_TRX)

    @allure.step("Нажатие на кнопку логина")
    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step("Ввод email для регистрации")
    def sign_up_field(self):
        self.click(self.SIGN_UP_FIELD)
        self.input_value(self.SIGN_UP_FIELD, text=MainPage.EMAIL_TO_SIGN_UP)

    @allure.step("Нажатие на кнопку регистрации")
    def click_signup_button(self):
        self.click(self.SUBMIT_EMAIL_TO_SIGNUP_BUTTON)

    def click_marketplace_tab(self):
        self.click(self.MARKETPLACE_TAB)

    @allure.step("Переход на вкладку Escrow")
    def click_escrow_tab(self):
        self.click(self.ESCROW_TAB)

    @allure.step("Клик по кнопке старта новой транзакции")
    def start_new_transaction(self):
        self.click(self.START_NEW_TRANSACTION_BTN)

    @allure.step("Валютные пары для обмена")
    def currency_pairs_btn(self):
        self.click(self.CURRENCY_PAIRS_BTN)

    @allure.step("Выбор криптовалютного курса BNB/USD")
    def bnb_usd(self):
        self.click(self.BNB_USD)

    @allure.step("Выбор криптовалютного курса TRX/USD")
    def trx_usd(self):
        self.click(self.TRX_USD)

    @allure.step("Переход на вкладку Exchange")
    def exchange_tab(self):
        self.click(self.EXCHANGE_TAB)
