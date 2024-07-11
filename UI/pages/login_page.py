# -*- encoding=utf8 -*-
import allure
from UI.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    TITLE = "Login to cryptoexchange.com"
    EMAIL_FIELD = By.XPATH, "//input[@name='email']"
    PASSWORD_FIELD = By.XPATH, "//input[@name='password']"
    AGREE_BOX = By.CLASS_NAME, "agree-box"
    LOGIN_BUTTON = By.XPATH, "//span[text()='Secure Log In']"
    EMAIL_TO_INFORM = By.ID, "email"
    LET_ME_KNOW_BTN = By.XPATH, '//button[@class="marketplace-empty__btn" and text()="Let me know once it launches"]'

    EMAIL = "test123123zz@mail.ru"
    PASSWORD = "crypto123456!"

    def main_title(self):
        self.get_title(self.TITLE)

    def input_email(self):
        self.click(self.EMAIL_FIELD)
        self.input_value(self.EMAIL_FIELD, text=LoginPage.EMAIL)

    def input_password(self):
        self.click(self.PASSWORD_FIELD)
        self.input_value(self.PASSWORD_FIELD, text=LoginPage.PASSWORD)

    def agree_box(self):
        self.click(self.AGREE_BOX)

    def login_button(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step("Ввод email для новостной рассылки")
    def email_to_inform(self):
        self.input_value(self.EMAIL_TO_INFORM, self.EMAIL)

    @allure.step("Клик по кнопке информирования")
    def let_me_know_click(self):
        self.click(self.LET_ME_KNOW_BTN)
