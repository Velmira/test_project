import requests
from API.config.config import get_url


class BaseRequest:
    @staticmethod
    def _make_request(method, url, api_route, headers, data=None):
        full_url = get_url(url=url, api_route=api_route)

        if method == 'GET':
            response = requests.get(url=full_url, headers=headers)
        elif method == 'POST':
            response = requests.post(url=full_url, headers=headers, json=data)
        elif method == 'PUT':
            response = requests.put(url=full_url, headers=headers, json=data)
        elif method == 'DELETE':
            response = requests.delete(url=full_url, headers=headers, json=data)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        return response

    @classmethod
    def get(cls, url, api_route, headers):
        return cls._make_request('GET', url, api_route, headers)

    @classmethod
    def post(cls, url, api_route, headers, data):
        return cls._make_request('POST', url, api_route, headers, data)

    @classmethod
    def put(cls, url, api_route, headers, data):
        return cls._make_request('PUT', url, api_route, headers, data)

    @classmethod
    def delete(cls, url, api_route, headers, data=None):
        return cls._make_request('DELETE', url, api_route, headers, data)
