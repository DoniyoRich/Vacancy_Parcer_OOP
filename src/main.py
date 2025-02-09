from mypy.util import short_type

from src.ExcelSaver import ExcelSaver
from src.HeadHunterAPI import HeadHunterAPI
from src.UserOperations import UserOperations
from src.Vacancy import Vacancy
from src.JSONSaver import JSONSaver
from src.constants import USER_MENU_LIST
from src.utils import user_menu, saving_file, output_to_console
import os
from constants import DATA_DIR, LOGS

import logging

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

file_name = 'vacancies_API'
path_to_vacancies_file = os.path.join(DATA_DIR, file_name)


class User:

    @staticmethod
    def intro():
        """ Приветствие Пользователя и описание работы программы. """
        print('\n' + "#" * 75)
        print("Добро пожаловать в программу получения и обработки вакансий с сайта hh.ru.\n"
              "Программа позволяет получить набор вакансий по Вашему запросу\n"
              "и вывести их в файл формата JSON.\n"
              "Полученные данные также можно фильтровать, сортировать, удалять,\n"
              "и результат записать в отдельный файл формата JSON или EXCEL."
              )
        print("#" * 75)

    # Функция для взаимодействия с пользователем
    @staticmethod
    def interaction() -> list[object]:
        # platforms = ["HeadHunter"]
        search_query = input("Введите поисковый запрос(например, python разработчик Москва): ")
        # search_query = 'python владивосток C++'

        # Создание экземпляра класса для работы с API сайтов с вакансиями
        hh = HeadHunterAPI(search_query, path_to_vacancies_file)

        hh.get_vacancies()
        json_file_api = JSONSaver()
        json_file_api.save_to_file(hh.vacancies, hh.file_worker)

        if hh.vacancies:
            print('\nВакансии найдены и сохранены в файл JSON в папке data')
        else:
            print('\nВакансий по Вашему запросу не найдено')

        vacancies_list = Vacancy.cast_to_object_list(hh.vacancies)

        return vacancies_list  # список объектов вакансий


def main():
    user = User()
    user.intro()
    vacancies = user.interaction()  # cписок объектов вакансий
    user_choice = -1
    while user_choice != 0:
        user_choice = user_menu(USER_MENU_LIST)
        match user_choice:
            case 0:
                break
            case 1:
                print("Отфильтровать вакансии...")
            case 2:
                user_op = UserOperations()
                user_op.sort_vacancies(vacancies)
            case 3:
                print("Удалить вакансии...")
            case 4:
                json_saver = JSONSaver()
                saving_file(vacancies, 'JSON', json_saver)
            case 5:
                excel_saver = ExcelSaver()
                saving_file(vacancies, 'Excel', excel_saver)
            case 6:
                print("Сделать выборку вакансий из топ зарплат")
            case 7:
                output_to_console(vacancies)


# top_n = int(input("Введите количество вакансий для вывода в топ N: "))


# filter_words = input(
#     f"Введите ключевые слова для фильтрации вакансий (например, {choice(position)} {choice(cities)}): ").split()
# salary_range = input("Введите через пробел диапазон зарплат: (например, '100000 150000'): ").split()

# Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.delete_vacancy(vacancy)
# filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
# ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
# sorted_vacancies = sort_vacancies(ranged_vacancies)
# top_vacancies = get_top_vacancies(sorted_vacancies, top_n)


if __name__ == "__main__":
    main()
