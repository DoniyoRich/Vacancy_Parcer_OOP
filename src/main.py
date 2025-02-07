from src.HeadHunterAPI import HeadHunterAPI
from src.Vacancy import Vacancy
from src.JSONSaver import JSONSaver
from random import choice

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI('some_file.txt')
cities = ["", "Москва", "Челябинск", "Мурманск", "Екатеринбург", "Владивосток", "Иркутск", "Калининград"]
position = ['python', 'c++', 'java developer', 'unreal engine', 'gamedev', 'django', 'junior', 'тимлид']


# Пример работы конструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
# "Требования: опыт работы от 3 лет...")


# Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.delete_vacancy(vacancy)


# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input(f"Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input(
        f"Введите ключевые слова для фильтрации вакансий (например, {choice(position)} {choice(cities)}): ").split()
    salary_range = input("Введите через пробел диапазон зарплат: (например, '100000 150000'): ").split()

    hh_api.get_vacancies(search_query.lower())

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_api.vacancies)

    # filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    #
    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
