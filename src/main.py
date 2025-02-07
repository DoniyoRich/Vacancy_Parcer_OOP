from src.ExcelSaver import ExcelSaver
from src.HeadHunterAPI import HeadHunterAPI
from src.Vacancy import Vacancy
from src.JSONSaver import JSONSaver
from random import choice
from pathlib import Path
import os

import logging

BASE_DIR = str(Path(__file__).parent.parent)
DATA_DIR = BASE_DIR + '\\data\\'
LOGS = BASE_DIR + '\\logs\\logs.log'

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

cities = ["", "Москва", "Челябинск", "Мурманск", "Екатеринбург", "Владивосток", "Иркутск", "Калининград"]
position = ['python', 'c++', 'java developer', 'unreal engine', 'gamedev', 'django', 'junior', 'тимлид']

file_name = 'vacancies.json'
path_to_vacancies_file = os.path.join(DATA_DIR, file_name)


# Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.delete_vacancy(vacancy)

def intro():
    print('\n' + "#" * 75)
    print("Добро пожаловать в программу получения и обработки вакансий с сайта hh.ru.\n"
          "Программа позволяет получить набор вакансий по Вашему запросу\n"
          "и вывести их в файл формата JSON.\n"
          "Полученные данные также можно фильтровать, сортировать, удалять,\n"
          "и результат записать в отдельный файл формата JSON, EXCEL, CSV или TXT."
          )
    print("#" * 75)


# Функция для взаимодействия с пользователем
def user_interaction():
    # platforms = ["HeadHunter"]
    intro()
    search_query = input(f"Введите поисковый запрос(например, python разработчик Москва): ")

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh = HeadHunterAPI(path_to_vacancies_file, search_query)

    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input(
    #     f"Введите ключевые слова для фильтрации вакансий (например, {choice(position)} {choice(cities)}): ").split()
    # salary_range = input("Введите через пробел диапазон зарплат: (например, '100000 150000'): ").split()

    hh.get_vacancies()
    excel_file = ExcelSaver()
    # excel_file.save_to_file(hh.vacancies)
    # app_logger.info('Все окей, данные получены и сохранены в файл JSON в папке data')

    # Преобразование набора данных из JSON в список объектов
    vac_objects = []
    for ind, vacancy in enumerate(hh.vacancies):
        id_ = vacancy['id']
        name = vacancy['name']
        area = vacancy['area']['name']
        alt_url = vacancy['alternate_url']
        try:
            salary_from = float(vacancy.get('salary').get('from'))
        except Exception:
            salary_from = 0
        try:
            salary_to = float(vacancy.get('salary').get('to', 0))
        except Exception:
            salary_to = 0
        experience = vacancy['experience']['name']
        vac_objects.append(Vacancy(id_, name, area, alt_url, salary_from, salary_to, experience))
        print(vac_objects[ind])
        # input()
    # vacancies_list = Vacancy.cast_to_object_list(hh.vacancies)

    # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    #
    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
