# -*- encoding=utf8 -*-
import os
import sys
import time
import pytest
import allure

from UI.steps.steps import Steps
from UI.pages.main_page import MainPage
from UI.pages.sign_up_page import SignupPage
from UI.pages.marketplace_page import MarketplacePage
from UI.pages.profile_page import ProfilePage
from UI.pages.login_page import LoginPage

sys.path.append(os.getcwd())


# pytest -v UI/tests/test_ui.py::TestUI --browser firefox

@allure.epic('UI Tests')
class TestUI:

    @allure.story('Проверка авторизации в профиле и выхода из профиля')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Проверка авторизации существующего пользователя и выход из профиля')
    @allure.title('Логин/логаут пользователя')
    def test_login_logout(self, browser):
        with allure.step("Переход по базовой ссылке"):
            browser.get(browser.base_url)
        MainPage(browser).click_login_button()
        Steps.login(browser)
        time.sleep(0.5)
        Steps.logout(browser)

    @allure.story('Проверка обновления данных профиля')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Проверка обновления данных пользователя')
    @allure.title('Обновление данных профиля пользователя')
    def test_update_account(self, browser):
        with allure.step("Переход по базовой ссылке"):
            browser.get(browser.base_url)
        MainPage(browser).click_login_button()
        Steps.login(browser)
        ProfilePage(browser).menu_button()
        ProfilePage(browser).profile_button()
        ProfilePage(browser).profile_settings()
        ProfilePage(browser).edit_profile()
        ProfilePage(browser).username_enter()
        ProfilePage(browser).update_account_btn()

    @allure.story('Проверка формы быстрой регистрации по email')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Форма регистрации по вводу email на главной странице')
    @allure.title('Проверка формы быстрой регистрации пользователя по email')
    def test_quick_sign_up_via_email(self, browser):
        with allure.step("Переход по базовой ссылке"):
            browser.get(browser.base_url)
        MainPage(browser).main_title()
        MainPage(browser).sign_up_field()
        MainPage(browser).click_signup_button()
        SignupPage(browser).click_signup_button_email()
        SignupPage(browser).main_title()
        SignupPage(browser).first_name()
        SignupPage(browser).last_name()
        SignupPage(browser).username()

    @allure.story('Проверка отображения категорий во вкладке Marketplace')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Отображение категорий во вкладке Marketplace')
    @allure.title('Категории во вкладке Marketplace')
    def test_marketplace_categories(self, browser):
        with allure.step("Переход по базовой ссылке"):
            browser.get(browser.base_url)
        MainPage(browser).main_title()
        Steps.marketplace(browser)
        MarketplacePage(browser).giftcards()
        MarketplacePage(browser).title_gift_cards()
        MarketplacePage(browser).domains()
        MarketplacePage(browser).title_domains()
        MarketplacePage(browser).watches()
        MarketplacePage(browser).title_watches()
        MarketplacePage(browser).usernames()
        MarketplacePage(browser).title_usernames()
        MarketplacePage(browser).realestate()
        MarketplacePage(browser).title_real_estate()

    @allure.story('Проверка добавления товара в корзину')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Добавление товара в корзину')
    @allure.title('Добавление товара в корзину')
    def test_add_item_to_card(self, browser):
        with allure.step("Переход по ссылке с категориями"):
            browser.get(browser.base_url + f"marketplace/cars")
        MarketplacePage(browser).title_cars()
        MarketplacePage(browser).click_lamborghini()
        MarketplacePage(browser).choose_item()
        MarketplacePage(browser).click_add_to_card()
        Steps.login(browser)
        time.sleep(1)
        el = MarketplacePage(browser).get_card()
        with allure.step("Проверка наличия товара в корзине"):
            assert el.text == "1"

    @allure.story('Проверка удаления товара из корзины')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Удаление товара из корзины')
    @allure.title('Удаление товара из корзины')
    def test_remove_item_from_card(self, browser):
        with allure.step("Переход по ссылке с категориями"):
            browser.get(browser.base_url)
        MainPage(browser).main_title()
        MainPage(browser).click_login_button()
        Steps.login(browser)
        ProfilePage(browser).card_btn()
        ProfilePage(browser).delete_btn()
        ProfilePage(browser).empty_card()

    @allure.story('Проверка вкладки Exchange')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Проверка вкладки Exchange')
    @allure.title('Вкладка Exchange')
    def test_exchange_tab(self, browser):
        with allure.step("Переход по ссылке с категориями"):
            browser.get(browser.base_url)
        browser.get(browser.base_url)
        MainPage(browser).main_title()
        MainPage(browser).exchange_tab()
        LoginPage(browser).email_to_inform()
        LoginPage(browser).let_me_know_click()

    @allure.story('Проверка вкладки Escrow в неавторизованном режиме')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Вкладка Escrow в неавторизованном режиме')
    @allure.title('Вкладка Escrow в неавторизованном режиме')
    def test_escrow_unauth(self, browser):
        with allure.step("Переход по ссылке с категориями"):
            browser.get(browser.base_url)
        MainPage(browser).main_title()
        MainPage(browser).click_escrow_tab()
        MainPage(browser).start_new_transaction()
        SignupPage(browser).click_signup_button_email()
        SignupPage(browser).main_title()

    @allure.story('Проверка вкладки Escrow в авторизованном режиме')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Вкладка Escrow в авторизованном режиме')
    @allure.title('Вкладка Escrow в авторизованном режиме')
    def test_escrow_auth(self, browser):
        with allure.step("Переход по ссылке с категориями"):
            browser.get(browser.base_url)
        MainPage(browser).main_title()
        MainPage(browser).click_login_button()
        Steps.login(browser)
        time.sleep(0.5)
        MainPage(browser).click_escrow_tab()
        MainPage(browser).start_new_transaction()
        MainPage(browser).start_trx_title()

    @allure.story('Проверка валютных пар')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Проверка валютных пар для получения курса обмена')
    @allure.title('Проверка валютных пар')
    def test_currency_exchage_pairs(self, browser):
        browser.get(browser.base_url)
        MainPage(browser).main_title()
        MainPage(browser).currency_pairs_btn()
        MainPage(browser).bnb_usd()
        MainPage(browser).currency_pairs_btn()
        MainPage(browser).trx_usd()
