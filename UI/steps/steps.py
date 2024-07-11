import allure

from UI.pages.main_page import MainPage
from UI.pages.login_page import LoginPage
from UI.pages.profile_page import ProfilePage
from UI.pages.marketplace_page import MarketplacePage


class Steps:

    def login(browser):
        with allure.step("Ввод email"):
            LoginPage(browser).input_email()
        with allure.step("Ввод пароля"):
            LoginPage(browser).input_password()
        with allure.step("Активация чекбокса о согласии с условиями"):
            LoginPage(browser).agree_box()
        with allure.step("Авторизация пользователя"):
            LoginPage(browser).login_button()

    def logout(browser):
        with allure.step("Клик по кнопке Меню"):
            ProfilePage(browser).menu_button()
        with allure.step("Клик по кнопке Выход из профиля"):
            ProfilePage(browser).logout_button()
        with allure.step("Экран авторизации"):
            LoginPage(browser).main_title()

    def marketplace(browser):
        with allure.step("Переход на вкладку Marketplace"):
            MainPage(browser).click_marketplace_tab()
        with allure.step("Страница Marketplace"):
            MarketplacePage(browser).main_title()
