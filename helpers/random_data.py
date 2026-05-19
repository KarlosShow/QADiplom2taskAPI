import random
import string
# генерация случайной строки (выбирает букву из алфавита и соединяет в строку)
def random_string(length: int = 8) -> str:
    alphabet = string.ascii_lowercase
    return "".join(random.choice(alphabet) for _ in range(length))
# хелпер генерация случайный email
def random_email() -> str:
    return f"{random_string(8)}@yandex.ru"
# хелпер генерация буквы и цифры в пароль
def random_password(length: int = 8) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))
# хелпер генерирует имя user_"""""
def random_name() -> str:
    return f"User_{random_string(5)}"