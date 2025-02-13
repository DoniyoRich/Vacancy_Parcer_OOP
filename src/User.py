from src.HeadHunterAPI import HeadHunterAPI
from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy
from src.VacancyOperationsABS import VacancyOperations
from src.constants import FILTER_MENU, SORT_FIELDS, SORT_TYPE, SORT_FIELD_MATRIX, PATH_TO_VACANCIES_FILE
from src.utils import user_menu, ask_to_save, output_to_console


class User(VacancyOperations):

    def __init__(self):
        self.vacancies = []

    def query_to_search(self) -> None:
        """ Метод взаимодействия с Пользователем. """
        # search_query = input("Введите поисковый запрос(например, python разработчик Москва): ")
        search_query = 'python владивосток'

        # Создание экземпляра класса для работы с API сайтов с вакансиями
        hh = HeadHunterAPI(search_query, PATH_TO_VACANCIES_FILE)
        hh.get_vacancies()
        json_file_api = JSONSaver()
        json_file_api.save_to_file(hh.vacancies, hh.file_worker)

        if hh.vacancies:
            print('\nВакансии найдены и сохранены в файл JSON в папке data')
        else:
            print('\nВакансий по Вашему запросу не найдено')
        self.vacancies = Vacancy.cast_to_object_list(hh.vacancies)  # список объектов вакансий

    def filter_vacancies(self) -> None:
        """ Метод фильтрации вакансий по ключевому слову. """
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

        self.vacancies.sort(key=lambda x: getattr(x,
                                                  SORT_FIELD_MATRIX[sort_field_choice][0]),
                            reverse=bool(sort_type_choice))
        print(f'Вакансии отсортированы по полю "{SORT_FIELD_MATRIX[sort_field_choice][1]}"')

    def get_top_N(self) -> None:
        """ Метод возвращает топ N вакансий по уровню зарплат. """
        top_n = int(input("\nВведите количество вакансий для вывода в топ N по зарплате: "))
        self.vacancies.sort(key=lambda x: x.salary, reverse=True)
        top_n_list = self.vacancies[:top_n]
        output_to_console(top_n_list)
        ask_to_save(self, top_n_list)

    def delete_vacancies(self) -> None:
        print('Удаление вакансий будет производится по ключевому слову в полю "Должность"')
        keyword = input("Введите ключевое слово: ")

        after_deletion = [x for x in self.vacancies if keyword.lower() not in x.name.lower()]
        output_to_console(after_deletion)
        ask_to_save(self, after_deletion)
