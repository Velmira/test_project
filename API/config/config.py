def get_url(url, api_route):
    return f'{url}/{api_route}'


class ApiConfig:
    BASE_URL = 'https://api.gectaro.com/v1'


class Headers:
    TOKEN = '1Rmv-AIO9a65hDC_bnAUdigSz2lZnd42'
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
