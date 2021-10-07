from unittest.mock import MagicMock

from fastapi.testclient import TestClient
from starlette import status

import main
from api.model.sports_facilities import Sports_Facilities

client = TestClient(main.get_app())
sports_facilities_path = "/api/v1/sports-facilities"


def test_get_sports_facilities_filter_province_like_gets_200(mocker):
    # Given
    db_engine_mock = mocker.patch('api.v1.routers.sports_facilities.DBEngine')
    select_mock = mocker.patch('api.v1.routers.sports_facilities.select')
    session_exec_mock = mocker.patch('api.v1.routers.sports_facilities.Session.exec')
    session_exec_mock.return_value.all = MagicMock(return_value=["not a real record", "also not a real record"])

    province_param = "Sevilla"

    # When
    response = client.get(f"{sports_facilities_path}/filter-province-like?province={province_param}")

    # Then
    db_engine_mock.return_value.get_db_engine.assert_called_once()
    select_mock.assert_called_once_with(Sports_Facilities)
    select_mock.return_value.where.assert_called_once()
    session_exec_mock.assert_called_once_with(select_mock.return_value.where.return_value)
    session_exec_mock.return_value.all.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert response.content == b'["not a real record","also not a real record"]'


def test_get_sports_facilities_filter_province_like_without_params_gets_422(mocker):
    # Given
    db_engine_mock = mocker.patch('api.v1.routers.sports_facilities.DBEngine')
    select_mock = mocker.patch('api.v1.routers.sports_facilities.select')
    session_exec_mock = mocker.patch('api.v1.routers.sports_facilities.Session.exec')

    # When
    response = client.get(f"{sports_facilities_path}/filter-province-like")

    # Then
    db_engine_mock.return_value.get_db_engine.assert_not_called()
    select_mock.assert_not_called()
    session_exec_mock.assert_not_called()

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.content == b'{"detail":[{"loc":["query","province"],' \
                               b'"msg":"field required","type":"value_error.missing"}]}'


def test_get_sports_facilities_filter_town_like_gets_200(mocker):
    # Given
    db_engine_mock = mocker.patch('api.v1.routers.sports_facilities.DBEngine')
    select_mock = mocker.patch('api.v1.routers.sports_facilities.select')
    session_exec_mock = mocker.patch('api.v1.routers.sports_facilities.Session.exec')
    session_exec_mock.return_value.all = MagicMock(return_value=["not a real record", "also not a real record"])

    town_param = "Sevilla"

    # When
    response = client.get(f"{sports_facilities_path}/filter-town-like?town={town_param}")

    # Then
    db_engine_mock.return_value.get_db_engine.assert_called_once()
    select_mock.assert_called_once_with(Sports_Facilities)
    select_mock.return_value.where.assert_called_once()
    session_exec_mock.assert_called_once_with(select_mock.return_value.where.return_value)
    session_exec_mock.return_value.all.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert response.content == b'["not a real record","also not a real record"]'


def test_get_sports_facilities_filter_town_like_without_params_gets_422(mocker):
    # Given
    db_engine_mock = mocker.patch('api.v1.routers.sports_facilities.DBEngine')
    select_mock = mocker.patch('api.v1.routers.sports_facilities.select')
    session_exec_mock = mocker.patch('api.v1.routers.sports_facilities.Session.exec')

    # When
    response = client.get(f"{sports_facilities_path}/filter-town-like")

    # Then
    db_engine_mock.return_value.get_db_engine.assert_not_called()
    select_mock.assert_not_called()
    session_exec_mock.assert_not_called()

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.content == b'{"detail":[{"loc":["query","town"],' \
                               b'"msg":"field required","type":"value_error.missing"}]}'


def test_get_sports_facilities_list_by_province_and_town_like_gets_200(mocker):
    # Given
    db_engine_mock = mocker.patch('api.v1.routers.sports_facilities.DBEngine')
    select_mock = mocker.patch('api.v1.routers.sports_facilities.select')
    session_exec_mock = mocker.patch('api.v1.routers.sports_facilities.Session.exec')
    session_exec_mock.return_value.all = MagicMock(return_value=["not a real record", "also not a real record"])

    province_param = "Sevilla"
    town_param = "Dos Hermanas"

    # When
    response = client.get(f"{sports_facilities_path}/list-by-province-and-town?"
                          f"province={province_param}&town={town_param}")

    # Then
    db_engine_mock.return_value.get_db_engine.assert_called_once()
    select_mock.assert_called_once_with(Sports_Facilities)
    select_mock.return_value.where.assert_called_once()
    session_exec_mock.assert_called_once_with(select_mock.return_value.where.return_value)
    session_exec_mock.return_value.all.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert response.content == b'["not a real record","also not a real record"]'


def test_get_sports_facilities_list_by_province_and_town_like_without_params_gets_422(mocker):
    # Given
    db_engine_mock = mocker.patch('api.v1.routers.sports_facilities.DBEngine')
    select_mock = mocker.patch('api.v1.routers.sports_facilities.select')
    session_exec_mock = mocker.patch('api.v1.routers.sports_facilities.Session.exec')

    # When
    response = client.get(f"{sports_facilities_path}/list-by-province-and-town")

    # Then
    db_engine_mock.return_value.get_db_engine.assert_not_called()
    select_mock.assert_not_called()
    session_exec_mock.assert_not_called()

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.content == b'{"detail":[{"loc":["query","province"],' \
                               b'"msg":"field required","type":"value_error.missing"},' \
                               b'{"loc":["query","town"],"msg":"field required","type":"value_error.missing"}]}'


def test_get_sports_facilities_list_by_postal_code_gets_200(mocker):
    # Given
    db_engine_mock = mocker.patch('api.v1.routers.sports_facilities.DBEngine')
    select_mock = mocker.patch('api.v1.routers.sports_facilities.select')
    session_exec_mock = mocker.patch('api.v1.routers.sports_facilities.Session.exec')
    session_exec_mock.return_value.all = MagicMock(return_value=["not a real record", "also not a real record"])

    postal_code_param = 41006

    # When
    response = client.get(f"{sports_facilities_path}/list-by-postal-code?postal_code={postal_code_param}")

    # Then
    db_engine_mock.return_value.get_db_engine.assert_called_once()
    select_mock.assert_called_once_with(Sports_Facilities)
    select_mock.return_value.where.assert_called_once()
    session_exec_mock.assert_called_once_with(select_mock.return_value.where.return_value)
    session_exec_mock.return_value.all.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert response.content == b'["not a real record","also not a real record"]'


def test_get_sports_facilities_list_by_postal_code_without_params_gets_422(mocker):
    # Given
    db_engine_mock = mocker.patch('api.v1.routers.sports_facilities.DBEngine')
    select_mock = mocker.patch('api.v1.routers.sports_facilities.select')
    session_exec_mock = mocker.patch('api.v1.routers.sports_facilities.Session.exec')

    # When
    response = client.get(f"{sports_facilities_path}/list-by-postal-code")

    # Then
    db_engine_mock.return_value.get_db_engine.assert_not_called()
    select_mock.assert_not_called()
    session_exec_mock.assert_not_called()

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.content == b'{"detail":[{"loc":["query","postal_code"],' \
                               b'"msg":"field required","type":"value_error.missing"}]}'


def test_get_sports_facilities_item_by_id_gets_200(mocker):
    # Given
    db_engine_mock = mocker.patch('api.v1.routers.sports_facilities.DBEngine')
    select_mock = mocker.patch('api.v1.routers.sports_facilities.select')
    session_exec_mock = mocker.patch('api.v1.routers.sports_facilities.Session.exec')
    session_exec_mock.return_value.first = MagicMock(return_value="not a real record")

    id_param = 1

    # When
    response = client.get(f"{sports_facilities_path}/{id_param}")

    # Then
    db_engine_mock.return_value.get_db_engine.assert_called_once()
    select_mock.assert_called_once_with(Sports_Facilities)
    select_mock.return_value.where.assert_called_once()
    session_exec_mock.assert_called_once_with(select_mock.return_value.where.return_value)
    session_exec_mock.return_value.first.assert_called_once()
    assert response.status_code == status.HTTP_200_OK
    assert response.content == b'"not a real record"'


def test_get_sports_facilities_item_by_id_with_wrong_param_gets_422(mocker):
    # Given
    db_engine_mock = mocker.patch('api.v1.routers.sports_facilities.DBEngine')
    select_mock = mocker.patch('api.v1.routers.sports_facilities.select')
    session_exec_mock = mocker.patch('api.v1.routers.sports_facilities.Session.exec')
    session_exec_mock.return_value.first = MagicMock(return_value="not a real record")

    id_param = "definitely_not_a_number"

    # When
    response = client.get(f"{sports_facilities_path}/{id_param}")

    # Then
    db_engine_mock.return_value.get_db_engine.assert_not_called()
    select_mock.assert_not_called()
    session_exec_mock.assert_not_called()

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.content == b'{"detail":[{"loc":["path","id"],"msg":"value is not a valid integer",' \
                               b'"type":"type_error.integer"}]}'
