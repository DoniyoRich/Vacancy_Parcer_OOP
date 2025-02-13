from src.ExcelSaver import ExcelSaver
from src.JSONSaver import JSONSaver
from src.User import User
from src.constants import USER_MENU_LIST
from src.utils import user_menu, saving_file, output_to_console


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


def main():
    """ Основная функция программы. """

    user = User()
    intro()

    user.query_to_search()

    user_choice = -1
    while user_choice != 0:
        user_choice = user_menu(USER_MENU_LIST)
        match user_choice:
            case 0:
                print("\nХорошего дня! ;)")
                break
            case 1:
                user.filter_vacancies()
            case 2:
                user.sort_vacancies()
            case 3:
                user.delete_vacancies()
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


if __name__ == "__main__":
    main()
