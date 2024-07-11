import allure
import pytest
from API.api_methods.issues import Issues
from API.helper.api_helper import RequestHelper
from API.config.config import ApiConfig, Headers


@allure.epic('API Tests')
@allure.feature('Задачи')
class TestIssues:

    @allure.story('Добавление новой задачи')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Запрос на добавление новой задачи')
    @allure.title('Добавление новой задачи компании')
    @pytest.mark.parametrize('company_id, name, description, creator_id, executor_id',
                             [(19098, 'MaxPower', 'Retails', 68, 35)])
    def test_add_new_issue(self, company_id, name, description, creator_id, executor_id):
        response = Issues.add_new_issue(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{company_id}/issues',
            headers=Headers.headers,
            company_id=company_id,
            name=name,
            description=description,
            creator_id=creator_id,
            executor_id=executor_id
        )
        RequestHelper.response_code_checker(response, 201)
        RequestHelper.check_response_content(
            response,
            {
                "executor_id": executor_id,
                "name": name,
                "creator_id": creator_id,
                "description": description,
                "company_id": f"{company_id}",
                "created_at": None,
                "id": None
            })

    @allure.story('Добавление новой задачи без имени и описания')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Запрос на добавление новой задачи без имени и описания')
    @allure.title('Добавление новой задачи компании без имени и описания')
    @pytest.mark.parametrize('company_id, name, description, creator_id, executor_id',
                             [(19098, ' ', ' ', 67, 34)])
    def test_add_new_issue_error(self, company_id, name, description, creator_id, executor_id):
        response = Issues.add_new_issue(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{company_id}/issues',
            headers=Headers.headers,
            company_id=company_id,
            name=name,
            description=description,
            creator_id=creator_id,
            executor_id=executor_id
        )
        RequestHelper.response_code_checker(response, 422)
        RequestHelper.check_response_content(
            response,
            [
                {
                    "field": "name",
                    "message": "Необходимо заполнить «Название задачи»."
                }
            ]
        )

    @allure.story('Получение всех задач компании')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Запрос на получение всех задач компании')
    @allure.title('Получение всех задач компании')
    @pytest.mark.parametrize('company_id', [19098])
    def test_get_issues(self, company_id):
        response = Issues.get_issues(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{company_id}/issues',
            headers=Headers.headers)
        RequestHelper.response_code_checker(response, 200)
        RequestHelper.check_response_content(
            response.json()[0],
            {
                "id": None,
                "company_id": company_id,
                "name": None,
                "description": None,
                "status": None,
                "creator_id": None,
                "executor_id": None,
                "created_at": None,
                "deadline": None,
                "project_id": None,
                "is_deleted": None
            })

    @allure.story('Получение задач чужой компании')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Запрос на получение задач чужой компании')
    @allure.title('Получение задач чужой компании')
    @pytest.mark.parametrize('company_id', [11])
    def test_get_issues_error(self, company_id):
        response = Issues.get_issues(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{company_id}/issues',
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

    @allure.story('Получение информации по определенной задаче компании')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Запрос на получение информации о задачее компании по id')
    @allure.title('Получение информации по определенной задаче компании')
    @pytest.mark.parametrize('company_id, issue_id', [(19098, 6287)])
    def test_get_issue_by_id(self, company_id, issue_id):
        response = Issues.get_issue_by_id(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{company_id}/issues/{issue_id}',
            headers=Headers.headers
        )
        RequestHelper.response_code_checker(response, 200)
        RequestHelper.check_response_content(
            response,
            {
                "id": issue_id,
                "company_id": company_id,
                "name": None,
                "description": None,
                "status": None,
                "creator_id": None,
                "executor_id": None,
                "created_at": None,
                "deadline": None,
                "project_id": None,
                "is_deleted": None
            })

    @allure.story('Получение информации по несуществующей задаче')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Запрос на получение информации по несуществующей задаче')
    @allure.title('Получение информации по несуществующей задаче')
    @pytest.mark.parametrize('company_id, issue_id', [(19098, 500)])
    def test_get_issue_by_id_error(self, company_id, issue_id):
        response = Issues.get_issue_by_id(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{company_id}/issues/{issue_id}',
            headers=Headers.headers
        )
        RequestHelper.response_code_checker(response, 404)
        RequestHelper.check_response_content(
            response,
            {
                "name": "Not Found",
                "message": "Запрошенная задача не найдена.",
                "code": 0,
                "status": 404
            })

    @allure.story('Обновление информации по задаче')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Запрос на обновление информации по задаче')
    @allure.title('Обновление информации по задаче')
    @pytest.mark.parametrize('company_id, issue_id, description', [(19098, 6287, "Traders")])
    def test_update_issue(self, company_id, issue_id, description):
        response = Issues.update_issue(
            url=ApiConfig.BASE_URL,
            api_route=f'companies/{company_id}/issues/{issue_id}',
            headers=Headers.headers,
            company_id=company_id,
            issue_id=issue_id,
            description=description
        )
        RequestHelper.response_code_checker(response, 200)
        RequestHelper.check_response_content(
            response,
            {
                "id": issue_id,
                "company_id": company_id,
                "name": None,
                "description": description,
                "status": None,
                "creator_id": None,
                "executor_id": None,
                "created_at": None,
                "deadline": None,
                "project_id": None,
                "is_deleted": None,
                "deleted_at": None
            })
