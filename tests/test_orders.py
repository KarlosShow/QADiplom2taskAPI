import allure
import pytest
from api.orders_client import OrdersClient
from data.constants import INVALID_INGREDIENT_ID

@allure.epic("Stellar Burgers API")
@allure.feature("Создание заказа")
class TestOrders:

    @allure.title("Создание заказа с авторизацией: 200 и success=true")
    def test_create_order_with_auth_success(
        self,
        base_url,
        authorized_user,
        ingredient_ids
    ):
        client = OrdersClient(base_url)
        response = client.create_order(
            ingredient_ids[:2],
            access_token=authorized_user["access_token"]
        )
        data = response.json()
        assert response.status_code == 200
        assert data["success"] is True
        assert data["order"]["number"]

    @allure.title("Создание заказа без авторизации: 200 и success=true")
    def test_create_order_without_auth_success(
        self,
        base_url,
        ingredient_ids
    ):
        client = OrdersClient(base_url)
        response = client.create_order(
            ingredient_ids[:2]
        )
        data = response.json()
        assert response.status_code == 200
        assert data["success"] is True
        assert data["order"]["number"]

    @allure.title("Создание заказа без ингредиентов: 400")
    def test_create_order_without_ingredients_returns_error(
        self,
        base_url
    ):
        client = OrdersClient(base_url)
        response = client.create_order(None)
        data = response.json()
        assert response.status_code == 400
        assert data["success"] is False
        assert data["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с невалидным id ингредиента: ошибка")
    def test_create_order_with_invalid_ingredient_returns_error(
        self,
        base_url
    ):
        client = OrdersClient(base_url)
        response = client.create_order(
            [INVALID_INGREDIENT_ID]
        )
        data = response.json()
        assert response.status_code >= 400
        assert data["success"] is False

    @allure.title("Создание заказа с ингредиентами: параметризация")
    @pytest.mark.parametrize("count", [1, 2])
    def test_create_order_with_ingredients_parametrized(
        self,
        base_url,
        ingredient_ids,
        count
    ):
        client = OrdersClient(base_url)
        response = client.create_order(
            ingredient_ids[:count]
        )
        data = response.json()
        assert response.status_code == 200
        assert data["success"] is True
        assert data["order"]["number"]
