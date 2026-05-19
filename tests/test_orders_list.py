import allure
from api.orders_client import OrdersClient

@allure.epic("Stellar Burgers API")
@allure.feature("Список заказов")
class TestOrdersList:

    @allure.title("Получение списка всех заказов: 200 и в ответе есть orders")
    def test_get_all_orders_returns_orders_list(self, base_url):
        client = OrdersClient(base_url)
        response = client.get_all_orders()
        data = response.json()
        assert response.status_code == 200
        assert data["success"] is True
        assert isinstance(data["orders"], list)