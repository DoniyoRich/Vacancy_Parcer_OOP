from src.ExcelSaver import ExcelSaver
from src.HeadHunterAPI import HeadHunterAPI
from src.Vacancy import Vacancy
from src.JSONSaver import JSONSaver
from src.VacancyOperationsABS import VacancyOperations
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


class User(VacancyOperations):

    def __init__(self):
        self.vacancies = []

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

    def interaction(self) -> None:
        """ Метод взаимодействия с Пользователем. """
        # search_query = input("Введите поисковый запрос(например, python разработчик Москва): ")
        search_query = 'python владивосток'

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

        self.vacancies = vacancies_list  # список объектов вакансий

    def filter_vacancies(self) -> None:
        """ Метод фильтрации вакансий по ключевому слову. """
        print("Отфильтровать вакансии...")
        menu_filter = int(input(
            '0. По ключевому слову в поле должность\n'
            '1. По уровню зарплат (задать диапазон)\n'
            '2. Регион\n'
        ))

    def sort_vacancies(self) -> None:
        """ Метод сортировки вакансий по заданному полю с учетом заданного направления сортировки. """
        print("\nПо какому полю сортировать:")
        sort_field_matrix = {
            0: ['id_num', 'ID'],
            1: ['name', 'Должность'],
            2: ['area', 'Регион'],
            3: ['salary', 'Зарплата'],
            4: ['experience', 'Требуемый опыт']
        }
        sort_field = int(input(
            '0. ID\n'
            '1. Должность\n'
            '2. Регион\n'
            '3. Зарплата\n'
            '4. Требуемый опыт\n'
        ))
        print("Направление сортировки:")
        sort_type = int(input(
            '0. По возрастанию\n'
            '1. По убыванию\n'
        ))
        self.vacancies.sort(key=lambda x: getattr(x, sort_field_matrix[sort_field][0]), reverse=bool(sort_type))
        print(f'Вакансии отсортированы по полю "{sort_field_matrix[sort_field][1]}"')

    def get_top_N(self) -> None:
        """ Метод возвращает топ N вакансий по уровню зарплат. """
        top_n = int(input("\nВведите количество вакансий для вывода в топ N по зарплате: "))
        self.vacancies.sort(key=lambda x: x.salary, reverse=True)
        # top_n_vacancies = self.vacancies[:top_n]
        output_to_console(self.vacancies[:top_n])
        # [print(vacancy) for vacancy in top_n_vacancies]
        to_save = int(input("\nСохранить выборку для дальнейшей работы? (да-1, нет-0): "))
        if to_save:
            setattr(self, 'vacancies', self.vacancies[:top_n])
            # vacancies = top_n_vacancies
            print("Выборка сохранена.")

    def delete_vacancies(self) -> list[dict]:
        pass


def main():
    """ Основная функция программы. """

    user = User()
    user.intro()

    user.interaction()

    user_choice = -1
    while user_choice != 0:
        user_choice = user_menu(USER_MENU_LIST)
        match user_choice:
            case 0:
                print("\nХорошего дня! ;)")
                break
            case 1:
                user.filter_vacancies()
                to_save = int(input("\nСохранить выборку для дальнейшей работы? (да-1, нет-0): "))
                # if to_save:
                #     user.vacancies = filtered_vacancies
                #     print("Выборка сохранена.")
            case 2:
                user.sort_vacancies()
            case 3:
                print("Удалить вакансии...")
            case 4:
                json_saver = JSONSaver()
                saving_file(user.vacancies, 'JSON', json_saver)
            case 5:
                excel_saver = ExcelSaver()
                saving_file(user.vacancies, 'Excel', excel_saver)
            case 6:
                user.get_top_N()
            case 7:
                output_to_console(user.vacancies)


# salary_range = input("Введите через пробел диапазон зарплат: (например, '100000 150000'): ").split()

# filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
# ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)


if __name__ == "__main__":
    main()
