from typing import Any

from src.constants import FILTER_MENU, PATH_TO_VACANCIES_FILE, SORT_FIELD_MATRIX, SORT_FIELDS, SORT_TYPE
from src.HeadHunterAPI import HeadHunterAPI
from src.JSONSaver import JSONSaver
from src.utils import ask_to_save, output_to_console, user_menu
from src.Vacancy import Vacancy
from src.VacancyOperationsABS import VacancyOperations


class User(VacancyOperations):
    """
    Класс Пользователь. Позволяет создавать запрос на поиск вакансии,
    сортировать вакансии, фильтровать, удалять, делать выборку из топ N по зарплате.
    """

    def __init__(self) -> None:
        """ Конструктор класса. """
        self.vacancies: list[Any] = []

    def query_to_search(self) -> None:
        """ Метод взаимодействия с Пользователем. Запрашивает строку для поиска вакансий. """
        search_query = input("Введите поисковый запрос(например, python разработчик Москва): ")
        # search_query = 'python владивосток'

        # Создание экземпляра класса для работы с API сайтов с вакансиями
        hh = HeadHunterAPI(search_query, PATH_TO_VACANCIES_FILE)
        hh.get_vacancies()
        json_file_api = JSONSaver()
        json_file_api.save_to_file(hh.vacancies, hh.file_worker)

        if hh.vacancies:
            print('\nВакансии найдены и сохранены в файл JSON в папке data')
        else:
            print('\nВакансий по Вашему запросу не найдено')

        # преобразуем список словарей из json ответа от API в список объектов.
        self.vacancies = Vacancy.cast_to_object_list(hh.vacancies)

    def filter_vacancies(self) -> None:
        """ Метод фильтрации вакансий по ключевому слову. """
        # показываем меню Пользователю и получаем его выбор
        user_choice = user_menu(FILTER_MENU)
        filtered = []
        match user_choice:
            case 0:
                print('Фильтрация будет производится по полю "Должность"')
                keyword = input("Введите ключевое слово: ")
                filtered = list(filter(lambda x: keyword.lower() in x.name.lower(), self.vacancies))

                output_to_console(filtered)
            case 1:
                print('Фильтрация будет производится по полю "Зарплата"')
                while True:
                    try:
                        sal_down, sal_up = input(
                            "Задайте диапазон зарплат через запятую, например: 100000, 150000: ").split(',')
                        filtered = list(
                            filter(lambda x: (x.salary > int(sal_down) and x.salary < int(sal_up)), self.vacancies))
                        output_to_console(filtered)
                        break
                    except Exception:
                        continue
            case 2:
                print('Фильтрация будет производится по полю "Регион"')
                keyword = input("Введите название региона: ")
                filtered = list(filter(lambda x: keyword.lower() in x.area.lower(), self.vacancies))
                output_to_console(filtered)
        ask_to_save(self, filtered)

    def sort_vacancies(self) -> None:
        """ Метод сортировки вакансий по заданному полю с учетом заданного направления сортировки. """
        print("\nПо какому полю сортировать:")
        sort_field_choice = user_menu(SORT_FIELDS)

        print("Направление сортировки:")
        sort_type_choice = user_menu(SORT_TYPE)

        # ключ [0] - нам нужен первый элемент словаря, то есть имя самого поля экземпляра
        self.vacancies.sort(key=lambda x: getattr(x,
                                                  SORT_FIELD_MATRIX[sort_field_choice][0]),
                            reverse=bool(sort_type_choice))
        # ключ [1] - нам нужен второй элемент словаря, то есть человекочитаемое название
        print(f'Вакансии отсортированы по полю "{SORT_FIELD_MATRIX[sort_field_choice][1]}"')

    def get_top_n(self) -> None:
        """ Метод возвращает топ N вакансий по уровню зарплат. """
        top_n = 0
        # пока не получим целое положительное число
        while not (isinstance(top_n, int) and top_n > 0):
            try:
                top_n = int(input("\nВведите количество вакансий для вывода в топ N по зарплате: "))
            except Exception:
                continue
        self.vacancies.sort(key=lambda x: x.salary, reverse=True)
        top_n_list = self.vacancies[:top_n]
        output_to_console(top_n_list)
        ask_to_save(self, top_n_list)

    def delete_vacancies(self) -> None:
        """ Метод удаления вакансий по ключевому слову в поле 'Должность'. """
        print('Удаление вакансий будет производится по ключевому слову в полю "Должность"')
        keyword = input("Введите ключевое слово: ")

        after_deletion = [x for x in self.vacancies if keyword.lower() not in x.name.lower()]
        output_to_console(after_deletion)
        ask_to_save(self, after_deletion)
