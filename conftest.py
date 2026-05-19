import pytest
from data.constants import BASE_URL
from api.user_client import UserClient
from api.ing_client import IngredientsClient
from helpers.user_gen import build_new_user_payload
# url api
@pytest.fixture
def base_url() -> str:
    return BASE_URL
# очистка тестовых пользователей после тестов
@pytest.fixture
def cleanup_users(base_url):
    client = UserClient(base_url)
    tokens = []
    credentials = []
# регистрация пользователя и удаление
    def _register_for_cleanup(*, access_token=None, email=None, password=None):
        if access_token:
            tokens.append(access_token)
        elif email and password:
            credentials.append((email, password))
# передаем функцию в тест удаляем пользователя если токена нет пробуем залогинится и снова удалить поьзователя
    yield _register_for_cleanup
    for token in tokens:
        try:
            client.delete_user(token)
        except Exception:
            pass 
    for email, password in credentials:
        try:
            login_resp = client.login({"email": email, "password": password})
            if login_resp.status_code == 200:
                access_token = login_resp.json().get("accessToken")
                if access_token:
                    client.delete_user(access_token)
        except Exception:
            pass
# регистрируем пользователя
@pytest.fixture
def registered_user(base_url, cleanup_users):
    client = UserClient(base_url)
    payload = build_new_user_payload()
    response = client.register(payload)
    body = response.json()
    access_token = body.get("accessToken")
    if access_token:
        cleanup_users(access_token=access_token)
    return payload
# авторизированный пользователь создает и логинит
@pytest.fixture
def authorized_user(base_url, registered_user):
    client = UserClient(base_url)
    login_resp = client.login(
        {
            "email": registered_user["email"],
            "password": registered_user["password"],
        }
    )
    body = login_resp.json()
    return {
        "email": registered_user["email"],
        "password": registered_user["password"],
        "access_token": body.get("accessToken"),
        "response": login_resp,
    }
# получить список ингридиентов
@pytest.fixture
def ingredient_ids(base_url):
    client = IngredientsClient(base_url)
    response = client.get_ingredients()
    body = response.json()
    return [item["_id"] for item in body["data"]]
