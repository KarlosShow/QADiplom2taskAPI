VALID_TEMPLATE = {
    "email": "velan@yandex.ru",
    "password": "MQc7FDK",
    "name": "Karlos",
}

MISSING_FIELD_CASES = [
    ("email", {"password": "Pass1", "name": "User1"}),
    ("password", {"email": "test1@yandex.ru", "name": "User1"}),
    ("name", {"email": "test1@yandex.ru", "password": "Pass1"}),
]