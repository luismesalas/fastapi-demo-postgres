from api.utils.db_engine import DBEngine


def test_db_engine(mocker, monkeypatch):
    # Given none
    monkeypatch.setenv("PG_USER", "fake_user")
    monkeypatch.setenv("PG_PASS", "p4ssw0rd")
    monkeypatch.setenv("PG_HOST", "fake_host")
    monkeypatch.setenv("PG_PORT", "9999")
    monkeypatch.setenv("PG_DB", "fake_db")
    create_engine_mock = mocker.patch('api.utils.db_engine.create_engine')

    # When
    db_engine_instance = DBEngine()

    # Then
    create_engine_mock.assert_called_once_with('postgresql://fake_user:p4ssw0rd@fake_host:9999/fake_db')
    assert db_engine_instance._DBEngine__engine == db_engine_instance.get_db_engine()
