VALID_TEMPLATE = {
    "email": "velanishkis@yandex.ru",
    "password": "MQc7FDKt",
    "name": "Karlos",
}

MISSING_FIELD_CASES = [
    ("email", {"password": "MQc7FDKt", "name": "User1"}),
    ("password", {"email": "velanishkis@yandex.ru", "name": "Iser1"}),
    ("name", {"email": "velanishkis@yandex.ru", "password": "MQc7FDKt"}),
]