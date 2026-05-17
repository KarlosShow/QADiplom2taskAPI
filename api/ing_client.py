from __future__ import annotations
import allure
from api.base_client import BaseClient
from api.endpoints import INGREDIENTS

class IngredientsClient(BaseClient):
    @allure.step("Получить список ингредиентов")
    def get_ingredients(self):
        return self.request("GET", INGREDIENTS)
    