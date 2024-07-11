# import requests
# from API.config.config import get_url
#
#
# class Contractors:
#
#     @classmethod
#     def types_contractors(cls, url, api_route, headers):
#         url = get_url(url=url, api_route=api_route)
#         response = requests.get(url=url, headers=headers)
#         return response
#
#     @classmethod
#     def get_contractor_by_company_id(cls, url, api_route, headers):
#         url = get_url(url=url, api_route=api_route)
#         response = requests.get(url=url, headers=headers)
#         return response
#
#     @classmethod
#     def get_contractor_requisites(cls, url, api_route, headers):
#         url = get_url(url=url, api_route=api_route)
#         response = requests.get(url=url, headers=headers)
#         return response
#
#     @classmethod
#     def add_contractor_group(cls, url, api_route, company_id: int, name: str, is_system, headers):
#         url = get_url(url=url, api_route=api_route)
#         data = {
#             "company_id": company_id,
#             "name": name,
#             "is_system": is_system
#         }
#         response = requests.post(url=url, headers=headers, json=data)
#         return response
#
#     @classmethod
#     def delete_contractor_group(cls, url, api_route, company_id: int, contract_id: int, headers):
#         url = get_url(url=url, api_route=api_route)
#         data = {
#             "company_id": company_id,
#             "id": contract_id
#         }
#         response = requests.delete(url=url, headers=headers, json=data)
#         return response

from API.config.base_request import BaseRequest

class Contractors(BaseRequest):
    @classmethod
    def types_contractors(cls, url, api_route, headers):
        return cls.get(url, api_route, headers)

    @classmethod
    def get_contractor_by_company_id(cls, url, api_route, headers):
        return cls.get(url, api_route, headers)

    @classmethod
    def get_contractor_requisites(cls, url, api_route, headers):
        return cls.get(url, api_route, headers)

    @classmethod
    def add_contractor_group(cls, url, api_route, company_id: int, name: str, is_system, headers):
        data = {
            "company_id": company_id,
            "name": name,
            "is_system": is_system
        }
        return cls.post(url, api_route, headers, data)

    @classmethod
    def delete_contractor_group(cls, url, api_route, company_id: int, contract_id: int, headers):
        data = {
            "company_id": company_id,
            "id": contract_id
        }
        return cls._make_request('DELETE', url, api_route, headers, data)