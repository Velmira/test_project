import allure
from API.api_methods.auth import Auth
from API.helper.api_helper import RequestHelper
from API.config.config import ApiConfig, Headers


@allure.epic('API Tests')
@allure.feature('Авторизация')
class TestAuth:

    @allure.story('Получение информации о текущем пользователе')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Запрос на получение информации о пользователе')
    @allure.title('Информация о текущем пользователе')
    def test_get_current_user(self):
        response = Auth.get_current_user(
            url=ApiConfig.BASE_URL,
            api_route='users/current',
            headers=Headers.headers
        )
        RequestHelper.response_code_checker(response, 200)
        RequestHelper.check_response_content(
            response,
            {
                "id": None,
                "phone": None,
                "email": None,
                "created_at": None,
                "first_name": None,
                "last_name": None,
                "color": None,
                "photo": None,
                "lang": None
            })

    @allure.story('Получение информации о чужом пользователе')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Попытка получить информации о чужом пользователе')
    @allure.title('Информация о чужом пользователе')
    def test_get_current_user_unauth(self):
        response = Auth.get_current_user(
            url=ApiConfig.BASE_URL,
            api_route='users/current',
            headers={
                "Authorization": f"Bearer '1Rmv-AIO9a65hDC_bnAUdigSz2lZn32'"
            })
        RequestHelper.response_code_checker(response, 401)
        RequestHelper.check_response_content(
            response,
            {
                "name": "Unauthorized",
                "message": "Your request was made with invalid credentials.",
                "code": 0,
                "status": 401
            })
