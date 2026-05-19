import allure
from api.user_client import UserClient

@allure.epic("Stellar Burgers API")
@allure.feature("Логин пользователя")
class TestUserLogin:

    @allure.title(
        "Можно залогиниться под существующим пользователем: "
        "200 и есть токены"
    )
    def test_login_existing_user_success(
        self,
        base_url,
        registered_user
    ):
        client = UserClient(base_url)
        response = client.login(
            {
                "email": registered_user["email"],
                "password": registered_user["password"]
            }
        )
        data = response.json()
        assert response.status_code == 200
        assert data["success"] is True
        assert data.get("accessToken")
        assert data.get("refreshToken")

    @allure.title(
        "Логин с неверным email/паролем: "
        "401 и email or password are incorrect"
    )
    def test_login_wrong_credentials_returns_error(
        self,
        base_url
    ):
        client = UserClient(base_url)
        response = client.login(
            {
                "email": "no_such_user@yandex.ru",
                "password": "wrongpass"
            }
        )
        data = response.json()
        assert response.status_code == 401
        assert data["success"] is False
        assert data["message"] == "email or password are incorrect"