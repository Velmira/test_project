from API.config.base_request import BaseRequest


class Companies(BaseRequest):
    @classmethod
    def add_new_company(cls, url, api_route, name, owner_user_id, headers):
        data = {
            "name": name,
            "owner_user_id": owner_user_id
        }
        return cls.post(url, api_route, headers, data)

    @classmethod
    def get_current_company_by_id(cls, url, api_route, headers):
        return cls.get(url, api_route, headers)

    @classmethod
    def get_companies(cls, url, api_route, headers):
        return cls.get(url, api_route, headers)

    @classmethod
    def update_company(cls, url, api_route, name, owner_user_id, headers):
        data = {
            "name": name,
            "owner_user_id": owner_user_id
        }
        return cls.put(url, api_route, headers, data)
