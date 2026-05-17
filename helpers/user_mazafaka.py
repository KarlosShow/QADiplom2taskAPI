from __future__ import annotations
import allure
from data.payload import USER_VALID_TEMPLATE
from random_data import random_email, random_password, random_name

@allure.step("Сформировать payload для нового пользователя")
def build_new_user_payload() -> dict:
    payload = USER_VALID_TEMPLATE.copy()
    payload["email"] = random_email()
    payload["password"] = random_password()
    payload["name"] = random_name()
    return payload