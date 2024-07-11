import allure
import pytest
from API.api_methods.companies import Companies
from API.helper.api_helper import RequestHelper
from API.config.config import ApiConfig, Headers


@allure.epic('API Tests')
@allure.feature('Компании')
class TestCompanies:

    @allure.story('Добавление новой компании')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Запрос на добавление новой компании')
    @allure.title('Добавление новой компании')
    @pytest.mark.parametrize('name, owner_user_id', [('BlackBar', 667)])
    def test_add_new_company(self, name, owner_user_id):
        response = Companies.add_new_company(
            url=ApiConfig.BASE_URL,
            api_route='companies',
            headers=Headers.headers,
            name=name,
            owner_user_id=owner_user_id
        )
        RequestHelper.response_code_checker(response, 201)
        RequestHelper.check_response_body_is_string(response)

    @allure.story('Попытка добавить компанию с пустым именем')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Запрос на добавление компанию с пустым имене')
    @allure.title('Добавление новой компании с пустым имененем')
    @pytest.mark.parametrize('name, owner_user_id', [('', 0)])
    def test_add_new_company_data_validation_failed(self, name, owner_user_id):
        response = Companies.add_new_company(
            url=ApiConfig.BASE_URL,
            api_route='companies',
            headers=Headers.headers,
            name=name,
            owner_user_id=owner_user_id
        )
        RequestHelper.response_code_checker(response, 422)
        RequestHelper.check_response_content(
            response,
            [
                {
                    "field": "name",
                    "message": "Необходимо заполнить «Название компании»."
                },
                {
                    "field": "owner_user_id",
                    "message": "Значение «Владелец» неверно."
                }])

    @allure.story('Получение информации о компании пользователя по id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Запрос на получение информации о компании по id')
    @allure.title('Получение информации о компании по id')
    @pytest.mark.parametrize('id', [19098])
    def test_get_current_company_by_id(self, id):
        response = Companies.get_current_company_by_id(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{id}',
            headers=Headers.headers
        )
        RequestHelper.response_code_checker(response, 200)
        RequestHelper.check_response_content(
            response,
            {
                "id": id,
                "name": None,
                "owner_user_id": None,
                "employer_count_interval": None,
                "owner_post": None,
                "working_direction": None,
                "billing_tariff_id": None,
                "created_at": None,
                "updated_at": None,
                "logo": None,
                "billing_is_over": None,
                "companyOutboundWebhooks": None,
                "currency_id": None
            })

    @allure.story('Получение информации о чужой компании по id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Запрос на получение информации о чужой компании по id')
    @allure.title('Получение информации о чужой компании по id')
    @pytest.mark.parametrize('id', [666])
    def test_get_current_company_by_id_forbidden(self, id):
        response = Companies.get_current_company_by_id(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{id}',
            headers=Headers.headers
        )
        RequestHelper.response_code_checker(response, 403)
        RequestHelper.check_response_content(
            response,
            {
                "name": "Forbidden",
                "message": "Доступ запрещен.",
                "code": 0,
                "status": 403
            })

    @allure.story('Получение информации о компаниях')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Запрос на получение информации о компаниях')
    @allure.title('Получение информации о компаниях')
    def test_get_companies(self):
        response = Companies.get_companies(
            url=ApiConfig.BASE_URL,
            api_route='companies',
            headers=Headers.headers,
        )
        RequestHelper.response_code_checker(response, 200)

    @allure.story('Обновление информации о компании')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Запрос на обновление информации о компании')
    @allure.title('Обновление информации о компании по id')
    @pytest.mark.parametrize('id, name, owner_user_id', [(19098, 'WhiteBar', 669)])
    def test_update_company(self, id, name, owner_user_id):
        response = Companies.update_company(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{id}',
            headers=Headers.headers,
            name=name,
            owner_user_id=owner_user_id
        )
        RequestHelper.response_code_checker(response, 200)
        RequestHelper.check_response_content(
            response,
            {
                "id": id,
                "name": name,
                "owner_user_id": owner_user_id
            })
