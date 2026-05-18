from __future__ import annotations
from typing import Any, Dict, Optional
import requests
import allure

#Базовый http клиент для работы с API
class BaseClient:
    def __init__(self, base_url: str, timeout: int = 20):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
# Универсальный метод для отправки http запросов
    @allure.step("HTTP {method} {path}")
    def request(
        self,
        method: str,
        path: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        url = f"{self.base_url}{path}"
        return self.session.request(
            method=method,
            url=url,
            headers=headers,
            json=json,
            params=params,
            timeout=self.timeout,
        )