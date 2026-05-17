import random
import string

def random_string(length: int = 10) -> str:
    alphabet = string.ascii_lowercase
    return "".join(random.choice(alphabet) for _ in range(length))

def random_email() -> str:
    return f"{random_string(10)}@yandex.ru"

def random_password(length: int = 10) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))

def random_name() -> str:
    return f"User_{random_string(8)}"