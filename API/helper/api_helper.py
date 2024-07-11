class RequestHelper:

    @classmethod
    def response_code_checker(cls, response, expected_response_code):
        if response.status_code != expected_response_code:
            raise ValueError(
                f'Полученный код {response.status_code} отличается от ожидаемого {expected_response_code}',
                response.text
            )

    @classmethod
    def check_response_content(cls, response, expected_content):
        if hasattr(response, 'json'):
            try:
                response_data = response.json()
            except ValueError:
                raise ValueError("Ответ не является валидным JSON объектом")
        else:
            response_data = response

        if isinstance(expected_content, str):
            assert expected_content in str(response_data), f"Ответ не содержит ожидаемый ключ '{expected_content}'"
            return

        if isinstance(response_data, list):
            assert isinstance(expected_content, list), "Ожидаемый контент должен быть списком"
            for item_expected in expected_content:
                assert any(item_expected.items() <= actual_item.items() for actual_item in
                           response_data), f"Элемент '{item_expected}' не найден в ответе"
        elif isinstance(response_data, dict):
            for key, expected_value in expected_content.items():
                assert key in response_data, f"Ответ не содержит ожидаемый ключ '{key}'"
                actual_value = response_data[key]

                if expected_value is None:
                    continue

                if isinstance(expected_value, dict):
                    cls.check_response_content(actual_value, expected_value)
                elif isinstance(expected_value, list):
                    if all(isinstance(item, dict) for item in expected_value):
                        for item in expected_value:
                            assert item in actual_value, f"Элемент '{item}' не найден в '{key}'"
                    else:
                        assert all(item in actual_value for item in
                                   expected_value), f"Массив '{key}' не содержит элементы {expected_value}"
                else:
                    assert actual_value == expected_value, (f"Значение '{actual_value}' для ключа '{key}' "
                                                            f"не соответствует ожидаемому '{expected_value}'")

    @classmethod
    def check_response_body_is_string(cls, response):
        content = response.text.strip()
        assert content, "Тело ответа пустое"
        assert isinstance(content, str), f"Тело ответа не является строкой: {content}"
