import allure
import pytest
from api.user_client import UserClient
from helpers.user_gen import build_new_user_payload
from data.payload import MISSING_FIELD_CASES

@allure.epic("Stellar Burgers API")
@allure.feature("Создание пользователя")
class TestUserCreate:

    @allure.title("Можно создать уникального пользователя: 200 и success=true")
    def test_register_unique_user_success(
        self,
        base_url,
        cleanup_users
    ):
        client = UserClient(base_url)
        payload = build_new_user_payload()
        response = client.register(payload)
        data = response.json()
        assert response.status_code == 200
        assert data["success"] is True
        assert data.get("accessToken")
        assert data.get("refreshToken")
        assert data["user"]["email"] == payload["email"]
        assert data["user"]["name"] == payload["name"]
        cleanup_users(
            access_token=data.get("accessToken")
        )

    @allure.title("Нельзя создать пользователя, который уже зарегистрирован")
    def test_register_existing_user_returns_error(
        self,
        base_url,
        registered_user
    ):
        client = UserClient(base_url)
        response = client.register(registered_user)
        data = response.json()
        assert response.status_code == 403
        assert data["success"] is False
        assert data["message"] == "User already exists"

    @allure.title("Нельзя создать пользователя без обязательного поля")
    @pytest.mark.parametrize(
        "missing_field, bad_payload",
        MISSING_FIELD_CASES
    )
    def test_register_missing_required_field_returns_error(
        self,
        base_url,
        missing_field,
        bad_payload,
        cleanup_users
    ):
        client = UserClient(base_url)
        payload = build_new_user_payload()
        payload.update(bad_payload)
        payload.pop(missing_field, None)
        cleanup_users(
            email=payload.get("email"),
            password=payload.get("password")
        )
        response = client.register(payload)
        data = response.json()
        assert response.status_code == 403
        assert data["success"] is False
        assert (
            data["message"]
            == "Email, password and name are required fields"
        )
