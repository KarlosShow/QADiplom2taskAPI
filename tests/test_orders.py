import allure
import pytest
from api.orders_client import OrdersClient
from data.constants import INVALID_INGREDIENT_ID

@allure.epic("Stellar Burgers API")
@allure.feature("Создание заказа")
class TestOrders:
    @allure.title("Создание заказа с авторизацией: 200 и success=true")
    def test_create_order_with_auth_success(self, base_url, authorized_user, ingredient_ids):
        orders_client = OrdersClient(base_url)
        resp = orders_client.create_order(
            ingredient_ids[:2],
            access_token=authorized_user["access_token"],
        )
        assert resp.status_code == 200
        body = resp.json()
        assert body.get("success") is True
        assert "order" in body
        assert "number" in body["order"]

    @allure.title("Создание заказа без авторизации: 200 и success=true")
    def test_create_order_without_auth_success(self, base_url, ingredient_ids):
        orders_client = OrdersClient(base_url)
        resp = orders_client.create_order(ingredient_ids[:2], access_token=None)
        assert resp.status_code == 200
        body = resp.json()
        assert body.get("success") is True
        assert "order" in body
        assert "number" in body["order"]

    @allure.title("Создание заказа без ингредиентов: 400")
    def test_create_order_without_ingredients_returns_error(self, base_url):
        orders_client = OrdersClient(base_url)
        resp = orders_client.create_order(None)
        assert resp.status_code == 400
        body = resp.json()
        assert body.get("success") is False
        assert body.get("message") == "Ingredient ids must be provided"

    @allure.title("Создание заказа с невалидным id ингредиента: ошибка")
    def test_create_order_with_invalid_ingredient_returns_error(self, base_url):
        orders_client = OrdersClient(base_url)
        resp = orders_client.create_order([INVALID_INGREDIENT_ID])
        assert resp.status_code >= 400
        body = resp.json()
        assert body.get("success") is False

    @allure.title("Создание заказа с ингредиентами: параметризация")
    @pytest.mark.parametrize("count", [1, 2])
    def test_create_order_with_ingredients_parametrized(self, base_url, ingredient_ids, count):
        orders_client = OrdersClient(base_url)
        resp = orders_client.create_order(ingredient_ids[:count])
        assert resp.status_code == 200
        body = resp.json()
        assert body.get("success") is True
        assert "order" in body
        assert "number" in body["order"]
