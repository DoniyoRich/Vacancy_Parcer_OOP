from src.constants import USER_MENU_LIST
from src.ExcelSaver import ExcelSaver
from src.JSONSaver import JSONSaver
from src.User import User
from src.utils import output_to_console, saving_file, user_menu


# pragma: no cover
def intro() -> None:
    """ Приветствие Пользователя и описание работы программы. """
    print('\n' + "#" * 75)
    print("Добро пожаловать в программу получения и обработки вакансий с сайта hh.ru.\n"
          "Программа позволяет получить набор вакансий по Вашему запросу\n"
          "и вывести их в файл формата JSON.\n"
          "Полученные данные также можно фильтровать, сортировать, удалять,\n"
          "и результат записать в отдельный файл формата JSON или EXCEL."
          )
    print("#" * 75)


def main() -> None:
    """ Основная функция программы. """

    # создаем экземпляр класса User и приветствуем
    user = User()
    intro()

    # запрашиваем у Пользователя вакансии для поиска
    user.query_to_search()

    # меню Пользователя
    user_choice = -1
    while user_choice != 0:
        user_choice = user_menu(USER_MENU_LIST)
        match user_choice:
            case 0:
                print("\nХорошего дня! ;)")
                break
            case 1:
                # фильтруем вакансии
                user.filter_vacancies()
            case 2:
                # сортируем вакансии
                user.sort_vacancies()
            case 3:
                # удаляем вакансии
                user.delete_vacancies()
            case 4:
                # сохраняем в json файл
                json_saver = JSONSaver()
                saving_file(user.vacancies, 'JSON', json_saver)
            case 5:
                # сохраняем в excel файл
                excel_saver = ExcelSaver()
                saving_file(user.vacancies, 'Excel', excel_saver)
            case 6:
                # получить выборку N вакансий
                user.get_top_n()
            case 7:
                # отобразить вакансии в консоли
                output_to_console(user.vacancies)


# точка входа в программу
if __name__ == "__main__":
    main()
