from API.config.base_request import BaseRequest


class Issues(BaseRequest):
    @classmethod
    def add_new_issue(cls, url, api_route, company_id: int, name: str, description: str,
                      creator_id: int, executor_id: int, headers):
        data = {
            "company_id": company_id,
            "name": name,
            "description": description,
            "creator_id": creator_id,
            "executor_id": executor_id
        }
        return cls.post(url, api_route, headers, data)

    @classmethod
    def get_issues(cls, url, api_route, headers):
        return cls.get(url, api_route, headers)

    @classmethod
    def get_issue_by_id(cls, url, api_route, headers):
        return cls.get(url, api_route, headers)

    @classmethod
    def update_issue(cls, url, api_route, issue_id: int, company_id: int, description: str, headers):
        data = {
            "company_id": company_id,
            "id": issue_id,
            "description": description
        }
        return cls.put(url, api_route, headers, data)
