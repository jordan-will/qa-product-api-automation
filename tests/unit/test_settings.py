from config.settings import BASE_URL, TIMEOUT


def test_base_url_is_configured():
    assert BASE_URL == "https://dummyjson.com"


def test_timeout_is_positive_integer():
    assert isinstance(TIMEOUT, int)
    assert TIMEOUT > 0