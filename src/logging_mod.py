import logging

from src.constants import LOGS

# Создание логгера
app_logger = logging.getLogger(__name__)
app_logger.setLevel(logging.INFO)

# Создание форматтера для определения формата лога
formatter = logging.Formatter('%(asktime)s - %(levelname)s - %(message)s')

# Создание файлового обработчика для записи логов в файл
file_handler = logging.FileHandler(LOGS)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Создание обработчика для записи логов в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
# console_handler.setFormatter(formatter)

# Добавление обработчиков к логгеру
app_logger.addHandler(file_handler)
app_logger.addHandler(console_handler)
