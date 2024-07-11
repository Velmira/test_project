import allure
import pytest
from API.api_methods.contractors import Contractors
from API.helper.api_helper import RequestHelper
from API.config.config import ApiConfig, Headers


@allure.epic('API Tests')
@allure.feature('Контрагенты')
class TestContractors:

    @allure.story('Получение доступных типов контрагентов')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Запрос на получение доступных типов контрагентов')
    @allure.title('Получение доступных типов контрагентов')
    @pytest.mark.parametrize('name, owner_user_id', [('BlackBar', 667)])
    def test_types_contractors(self, name, owner_user_id):
        response = Contractors.types_contractors(
            url=ApiConfig.BASE_URL,
            api_route='contractor-types',
            headers=Headers.headers
        )
        RequestHelper.response_code_checker(response, 200)
        RequestHelper.check_response_content(
            response,
            [
                {
                    "id": 10,
                    "label": "Поставщик"
                },
                {
                    "id": 20,
                    "label": "Заказчик"
                },
                {
                    "id": 30,
                    "label": "Контрагент"
                },
                {
                    "id": 40,
                    "label": "Инвестор"
                },
                {
                    "id": 60,
                    "label": "Сотрудник"
                },
                {
                    "id": 50,
                    "label": "Другое"
                }
            ]
        )

    @allure.story('Добавление группы контрагентов')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Запрос на добавление группы контрагентов')
    @allure.title('Добавление группы контрагентов')
    @pytest.mark.parametrize('company_id, name', [(19098, "NoName")])
    def test_add_contractor_group(self, company_id, name):
        response = Contractors.add_contractor_group(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{company_id}/contractors-groups',
            headers=Headers.headers,
            company_id=company_id,
            name=name,
            is_system=None
        )
        assert response.ok is True
        RequestHelper.check_response_content(
            response,
            {
                "company_id": company_id
            })
        return response

    @allure.story('Получение информации о контрагентах компании')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Запрос на получение информации о контрагентах компании')
    @allure.title('Получение информации о контрагентах компании')
    @pytest.mark.parametrize('company_id', [19098])
    def test_get_contractors_by_company_id(self, company_id):
        response = Contractors.get_contractor_by_company_id(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{company_id}/contractors',
            headers=Headers.headers
        )
        RequestHelper.response_code_checker(response, 200)
        RequestHelper.check_response_content(
            response,
            [{
                "company_id": company_id
            }])

    @allure.story('Получение информации о контрагентах недоступной компании')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Запрос на получение информации о контрагентах недоступной компании')
    @allure.title('Получение информации о контрагентах недоступной компании')
    @pytest.mark.parametrize('company_id', [12])
    def test_get_contractors_by_company_id_error(self, company_id):
        response = Contractors.get_contractor_by_company_id(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{company_id}/contractors',
            headers=Headers.headers
        )
        RequestHelper.response_code_checker(response, 400)
        RequestHelper.check_response_content(
            response,
            {
                "name": "Bad Request",
                "message": "Выбранная компания недоступна.",
                "code": 56300,
                "status": 400
            })

    @allure.story('Получение информации о реквизитах контрагента компании')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Запрос на получение информации о реквизитах контрагента компании')
    @allure.title('Получение иинформации о реквизитах контрагента компании')
    @pytest.mark.parametrize('company_id, contractor_id', [(19098, 160824)])
    def test_get_contractors_requisites(self, company_id, contractor_id):
        response = Contractors.get_contractor_requisites(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{company_id}/contractors/{contractor_id}/requisites',
            headers=Headers.headers
        )
        RequestHelper.response_code_checker(response, 200)
        RequestHelper.check_response_content(
            response,
            {
                "contractor_id": contractor_id,
                "full_name": None,
                "inn": None,
                "kpp": None,
                "ogrn": None,
                "bank": None,
                "bik": None,
                "cor_account": None,
                "account": None,
                "legal_address": None,
                "fio": None,
                "passport": None,
                "passport_issued": None,
                "okved": None,
                "okfs": None,
                "okogu": None,
                "okato": None,
                "oktmo": None,
                "okpo": None
            })

    @allure.story('Получение информации о реквизитах контрагента компании')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Запрос на получение информации о реквизитах контрагента компании')
    @allure.title('Получение иинформации о реквизитах контрагента компании')
    @pytest.mark.parametrize('company_id, contractor_id', [(19098, 0)])
    def test_get_contractors_requisites_error(self, company_id, contractor_id):
        response = Contractors.get_contractor_requisites(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{company_id}/contractors/{contractor_id}/requisites',
            headers=Headers.headers
        )
        RequestHelper.response_code_checker(response, 400)
        RequestHelper.check_response_content(
            response,
            {
                "name": "Bad Request",
                "message": "Запрошенный комтрагент не найден",
                "code": 0,
                "status": 400
            })

    @allure.story('Получение информации о реквизитах контрагента компании')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Запрос на получение информации о реквизитах контрагента компании')
    @allure.title('Получение информации о реквизитах контрагента компании')
    @pytest.mark.parametrize('company_id, name, is_system', [(19098, "NoName", "true")])
    def test_add_contractor_group_error(self, company_id, name, is_system):
        response = Contractors.add_contractor_group(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{company_id}/contractors-groups',
            headers=Headers.headers,
            company_id=company_id,
            name=name,
            is_system=is_system
        )
        RequestHelper.response_code_checker(response, 422)
        RequestHelper.check_response_content(
            response,
            [
                {
                    "field": "is_system",
                    "message": "Значение «Is System» должно быть равно «1» или «0»."
                }])

    @allure.story('Попытка удалить контрагента чужой компании')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Запрос на удаление контрагента чужой компании')
    @allure.title('Удаление контрагента чужой компании')
    @pytest.mark.parametrize('company_id, contract_id', [(19098, 122)])
    def test_delete_contractor_group(self, company_id, contract_id):
        response = Contractors.delete_contractor_group(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{company_id}/contractors/{contract_id}',
            headers=Headers.headers,
            company_id=company_id,
            contract_id=contract_id
        )
        RequestHelper.response_code_checker(response, 403)
        RequestHelper.check_response_content(
            response,
            {
                "name": "Forbidden",
                "message": "Доступ запрещен.",
                "code": 0,
                "status": 403
            }
        )
