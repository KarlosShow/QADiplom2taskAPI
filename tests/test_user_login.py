import allure
from api.user_client import UserClient

@allure.epic("Stellar Burgers API")
@allure.feature("Логин пользователя")
class TestUserLogin:
    @allure.title("Можно залогиниться под существующим пользователем: 200 и есть токены")
    def test_login_existing_user_success(self, base_url, registered_user):
        client = UserClient(base_url)
        resp = client.login(
            {
                "email": registered_user["email"],
                "password": registered_user["password"],
            }
        )
        assert resp.status_code == 200
        body = resp.json()
        assert body.get("success") is True
        assert "accessToken" in body
        assert "refreshToken" in body

    @allure.title("Логин с неверным email/паролем: 401 и email or password are incorrect")
    def test_login_wrong_credentials_returns_error(self, base_url):
        client = UserClient(base_url)
        resp = client.login({"email": "no_such_user@yandex.ru", "password": "wrongpass"})
        assert resp.status_code == 401
        body = resp.json()
        assert body.get("success") is False
        assert body.get("message") == "email or password are incorrect"
        