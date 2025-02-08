from src.ExcelSaver import ExcelSaver
from src.HeadHunterAPI import HeadHunterAPI
from src.Vacancy import Vacancy
from src.JSONSaver import JSONSaver
from src.utils import convert_to_list
import os
from paths import DATA_DIR, LOGS

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

# cities = ["", "Москва", "Челябинск", "Мурманск", "Екатеринбург", "Владивосток", "Иркутск", "Калининград"]
# position = ['python', 'c++', 'java developer', 'unreal engine', 'gamedev', 'django', 'junior', 'тимлид']

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
    def interaction() -> list[dict]:
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

        return vacancies_list

    @staticmethod
    def get_and_check_user_input() -> int:
        """ Функция возвращает корректный выбор операции над списком вакансий от Пользователя. """
        user_choice = -1
        while not user_choice in list(range(8)):
            print('\nВыберите тип операции (нажмите цифру из списка):\n'
                  '1. Отфильтровать вакансии.\n'
                  '2. Отсортировать вакансии.\n'
                  '3. Удалить вакансии.\n'
                  '4. Сохранить основные данные в JSON.\n'
                  '5. Сохранить основные данные в Excel.\n'
                  '6. Сделать выборку из топ зарплат.\n'
                  '7. Вывести вакансии в консоль.\n'
                  '0. На сегодня хватит ;)')
            try:
                user_choice = int(input())
            except ValueError:
                print('Пожалуйста, введите число из списка..')
        return user_choice


def main():
    user = User()
    user.intro()
    vacancies = user.interaction()
    user_choice = -1
    while user_choice != 0:
        user_choice = user.get_and_check_user_input()
        match user_choice:
            case 0:
                break
            case 1:
                print("Отфильтровать вакансии...")
            case 2:
                print("Отсортировать вакансии...")
            case 3:
                print("Удалить вакансии...")
            case 4:
                json_filename = input("Введите имя JSON файла: ")
                json_vacancies = convert_to_list(vacancies)
                json_saver = JSONSaver()
                json_saver.save_to_file(json_vacancies, os.path.join(DATA_DIR, json_filename))
                print(f'Файл "{json_filename}.json" сохранен.')
            case 5:
                excel_filename = input("Введите имя EXCEL файла: ")
                excel_vacancies = convert_to_list(vacancies)
                excel_saver = ExcelSaver()
                excel_saver.save_to_file(excel_vacancies, os.path.join(DATA_DIR, excel_filename))
                print(f'Файл "{excel_filename}.xlsx" сохранен.')
            case 6:
                print("Сделать выборку вакансий из топ зарплат")
            case 7:
                if len(vacancies):
                    print(f"Найдено вакансий: {len(vacancies)}")
                    print("Будет выводиться по 15 вакансий за раз. Для продолжения нажимайте Enter\n")
                    count = round(len(vacancies) / 15)
                    start, end = 0, 15
                    while count >= 0:
                        for vacancy in vacancies[start:end]:
                            print(vacancy)
                        input()
                        start += 15
                        end += 15
                        count -= 1
                else:
                    print("Вакансий нет")


# top_n = int(input("Введите количество вакансий для вывода в топ N: "))


# filter_words = input(
#     f"Введите ключевые слова для фильтрации вакансий (например, {choice(position)} {choice(cities)}): ").split()
# salary_range = input("Введите через пробел диапазон зарплат: (например, '100000 150000'): ").split()

# excel_file = ExcelSaver()
# excel_file.save_to_file(hh.vacancies)
# Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.delete_vacancy(vacancy)
# filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
# ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
# sorted_vacancies = sort_vacancies(ranged_vacancies)
# top_vacancies = get_top_vacancies(sorted_vacancies, top_n)


if __name__ == "__main__":
    main()
