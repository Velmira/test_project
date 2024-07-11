# -*- encoding=utf8 -*-
import allure

from UI.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SignupPage(BasePage):
    TITLE = "Create New Customer Account"
    SIGNUP_BUTTON_WITH_EMAIL = By.XPATH, "//span[@class='my-btn-span' and text()='Sign up with email']"
    FIRST_NAME = By.CSS_SELECTOR, 'input[name="first_name"]'
    LAST_NAME = By.CSS_SELECTOR, 'input[name="last_name"]'
    USERNAME = By.CSS_SELECTOR, 'input[name="username"]'

    @allure.step("Отображение страницы регистрации")
    def main_title(self):
        self.get_title(self.TITLE)

    @allure.step("Нажатие на кнопку Регистрации")
    def click_signup_button_email(self):
        self.click(self.SIGNUP_BUTTON_WITH_EMAIL)

    @allure.step("Наличие поля Имя")
    def first_name(self):
        self.get_element(self.FIRST_NAME)

    @allure.step("Наличие поля Фамилия")
    def last_name(self):
        self.get_element(self.LAST_NAME)

    @allure.step("Наличие поля Username")
    def username(self):
        self.get_element(self.USERNAME)
