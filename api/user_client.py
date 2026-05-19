from __future__ import annotations
import allure
from api.base_client import BaseClient
from api.endpoints import AUTH_REGISTER, AUTH_LOGIN, AUTH_USER
# клиент для работы с API пользователей
class UserClient(BaseClient):
    @allure.step("Зарегистрировать пользователя")
    def register(self, payload: dict):
        return self.request("POST", AUTH_REGISTER, json=payload)

    @allure.step("Авторизоваться пользователем")
    def login(self, payload: dict):
        return self.request("POST", AUTH_LOGIN, json=payload)

    @allure.step("Удалить пользователя по accessToken")
    def delete_user(self, access_token: str):
        headers = {"Authorization": access_token}
        return self.request("DELETE", AUTH_USER, headers=headers)