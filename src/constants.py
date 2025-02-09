from pathlib import Path

BASE_DIR = str(Path(__file__).parent.parent)
DATA_DIR = BASE_DIR + '\\data\\'
LOGS = BASE_DIR + '\\logs\\logs.log'

USER_MENU_LIST = [
    '1. Отфильтровать вакансии.\n'
    '2. Сортировать вакансии.\n'
    '3. Удалить вакансии.\n'
    '4. Сохранить основные данные в JSON.\n'
    '5. Сохранить основные данные в Excel.\n'
    '6. Сделать выборку из топ зарплат.\n'
    '7. Вывести вакансии в консоль.\n'
    '0. На сегодня хватит ;)'
]
