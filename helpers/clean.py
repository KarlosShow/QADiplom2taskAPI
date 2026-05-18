from __future__ import annotations
import allure
from api.user_client import UserClient
# хелпер безопасного удаления пользователя
@allure.step("Удалить пользователя, если есть accessToken")
def safe_delete_user(user_client: UserClient, access_token: str | None) -> None:
    if not access_token:
        return
    user_client.delete_user(access_token)