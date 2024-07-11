import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url", default="https://api.gectaro.com/v1", help="Request Url"
    )
    parser.addoption(
        "--status_code", default=200, help="Status Success"
    )
    parser.addoption(
        "--status_code_error", default=404, help="Not Found"
    )


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def status_code(request):
    return request.config.getoption("--status_code")


@pytest.fixture()
def status_code_error(request):
    return request.config.getoption("--status_code_error")