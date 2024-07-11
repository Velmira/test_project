from API.config.base_request import BaseRequest

class Auth(BaseRequest):
    @classmethod
    def get_current_user(cls, url, api_route, headers):
        return cls.get(url, api_route, headers)
