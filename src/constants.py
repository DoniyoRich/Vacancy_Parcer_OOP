import os
from pathlib import Path

BASE_DIR = str(Path(__file__).parent.parent)
DATA_DIR = BASE_DIR + '\\data\\'
TEST_DATA_SETS = BASE_DIR + '\\tests\\' + '\\test_datasets\\'

FILE_NAME_API = 'VACANCIES_API'
PATH_TO_VACANCIES_FILE = os.path.join(DATA_DIR, FILE_NAME_API)

USER_MENU_LIST = [
    '1. Отфильтровать вакансии.',
    '2. Сортировать вакансии.',
    '3. Удалить вакансии.',
    '4. Сохранить основные данные в JSON.',
    '5. Сохранить основные данные в Excel.',
    '6. Сделать выборку из топ зарплат.',
    '7. Вывести вакансии в консоль.',
    '0. На сегодня хватит ;)'
]

SORT_FIELDS = [
    '0. ID',
    '1. Должность',
    '2. Регион',
    '3. Зарплата',
    '4. Требуемый опыт'
]

SORT_FIELD_MATRIX = {
    0: ['id_num', 'ID'],
    1: ['name', 'Должность'],
    2: ['area', 'Регион'],
    3: ['salary', 'Зарплата'],
    4: ['experience', 'Требуемый опыт']
}

SORT_TYPE = [
    '0. По возрастанию',
    '1. По убыванию',
]

FILTER_MENU = [
    '0. По ключевому слову в поле должность',
    '1. По уровню зарплат (задать диапазон)',
    '2. По региону'
]

YES_NO_CHOICE = ['1. Да', '0. Нет']
