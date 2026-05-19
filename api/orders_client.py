from __future__ import annotations
import allure
from api.base_client import BaseClient
from api.endpoints import ORDERS, ORDERS_ALL
# клиент для работы с API заказов
class OrdersClient(BaseClient):
    @allure.step("Создать заказ")
    def create_order(self, ingredient_ids: list[str] | None, access_token: str | None = None):
        headers = {}
        if access_token:
            headers["Authorization"] = access_token
        payload = {}
        if ingredient_ids is not None:
            payload["ingredients"] = ingredient_ids
        return self.request("POST", ORDERS, headers=headers or None, json=payload)

    @allure.step("Получить все заказы (публичная лента)")
    def get_all_orders(self):
        return self.request("GET", ORDERS_ALL)
    