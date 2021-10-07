from unittest.mock import call

from api.v1 import api
from api.v1.routers import sports_facilities


def test_get_api(mocker):
    # Given
    api_router_mock = mocker.patch('api.v1.api.APIRouter')
    health_mock = mocker.patch('api.v1.api.health')

    # When
    result = api.get_api()

    # Then
    api_router_mock.assert_called_once()
    api_router_mock.return_value.include_router.assert_has_calls(
        [call(health_mock.router), call(sports_facilities.router, prefix="/sports-facilities")])
    assert result == api_router_mock.return_value
