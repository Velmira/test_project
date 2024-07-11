# -*- encoding=utf8 -*-
import time

import allure

from UI.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    MENU_BUTTON = By.CSS_SELECTOR, "div.my-header_customer_btn-title"
    LOGOUT_BUTTON = By.XPATH, "//span[@class='my-header_customer_drop_link' and text()='Sign out']"
    PROFILE_BTN = By.XPATH, "//*[@id='header']/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/a[1]"
    PROFILE_SETTINGS = By.XPATH, '//img[@src="/images/icons/more-actions.svg"]'
    EDIT_PROFILE = (By.XPATH,
                    '//*[@id="app"]/main/div/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]')
    USERNAME_FIELD = By.XPATH, "//input[@placeholder='Username']"
    USERNAME = "test123123zz"
    UPDATE_ACCOUNT_BTN = By.XPATH, ('//*[@id="app"]'
                                    '/main/div/div/div/div/div/div/div/div/div[2]/div[1]/div[3]/form/div[5]/button[2]')
    CARD_BUTTON = By.CLASS_NAME, "my-header_cart_icon-prod"
    DELETE_ITEM_BTN = By.XPATH, "//div[@class='cart-multi-content_select-action']//span[contains(., 'Delete (1)')]"
    EMPTY_CARD_TEXT = By.XPATH, "//p[contains(text(), 'Your shopping cart is empty')]"

    def menu_button(self):
        self.click(self.MENU_BUTTON)

    def logout_button(self):
        self.click(self.LOGOUT_BUTTON)

    @allure.step("Клик по кнопке Профиль")
    def profile_button(self):
        self.click(self.PROFILE_BTN)

    @allure.step("Клик по кнопке Настройки профиля")
    def profile_settings(self):
        self.click(self.PROFILE_SETTINGS)

    @allure.step("Клик по кнопке редактирования профиля")
    def edit_profile(self):
        self.click(self.EDIT_PROFILE)

    @allure.step("Ввод USERNAME")
    def username_enter(self):
        self.click(self.USERNAME_FIELD)
        time.sleep(3)
        self.input_value(self.USERNAME_FIELD, self.USERNAME)

    @allure.step("Обновление данных профиля")
    def update_account_btn(self):
        self.click(self.UPDATE_ACCOUNT_BTN)

    @allure.step("Клик по кнопке Корзина")
    def card_btn(self):
        self.click(self.CARD_BUTTON)

    @allure.step("Клик по кнопке Удалить товар")
    def delete_btn(self):
        self.click(self.DELETE_ITEM_BTN)

    @allure.step("Проверка того, что корзина пустая")
    def empty_card(self):
        self.get_element(self.EMPTY_CARD_TEXT)
