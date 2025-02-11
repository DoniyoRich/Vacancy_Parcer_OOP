import os

from src.constants import DATA_DIR, YES_NO_CHOICE


def convert_to_list(vacancies: list[object]) -> list[dict]:
    """ Функция создает список словарей вакансий из списка объектов вакансий. """
    vacancies_list = [
        {'ID': vacancy.id_num,
         'должность': vacancy.name,
         'регион': vacancy.area,
         'зарплата': vacancy.salary,
         'требуемый опыт': vacancy.experience,
         'ссылка на вакансию': vacancy.alt_url}
        for vacancy in vacancies
    ]
    return vacancies_list


def user_menu(menu_list: list[str]) -> int:
    """ Функция возвращает корректный выбор операции над списком вакансий от Пользователя. """
    user_choice = -1
    while not user_choice in list(range(len(menu_list))):
        print('\nВыберите действие:\n')
        [print(menu_item) for menu_item in menu_list]
        try:
            user_choice = int(input('Ваш выбор: '))
        except Exception:
            print('Пожалуйста, введите число из списка..')
            continue
    return user_choice


def saving_file(vacancies: list[object], file_type: str, saver: object) -> None:
    filename = input(f"Введите имя {file_type} файла: ")
    file_vacancies = convert_to_list(vacancies)
    saver.save_to_file(file_vacancies, os.path.join(DATA_DIR, filename))
    ext = '.json'
    if file_type == 'Excel': ext = '.xlsx'
    print(f'Файл "{filename}{ext}" сохранен.')


def ask_to_save(obj: object, who_asked: str, top_n: int = 1):
    print("Сохранить выборку для дальнейшей работы?")
    if user_menu(YES_NO_CHOICE) == 1:
        if who_asked == 'get_top':
            setattr(obj, 'vacancies', obj.vacancies[:top_n])
            print("Выборка топ зарплат сохранена.")
        elif who_asked == 'filter':
            print("Выборка после фильтрации сохранена.")
    else:
        print("Выборка не сохранена.")


def output_to_console(vacancies: list[object]) -> None:
    """ Вывод вакансий в консоль. Задается количество выводимых вакансий за один раз. """
    print(f"Найдено вакансий: {len(vacancies)}")
    quantity = 1
    while isinstance(quantity, int):
        try:
            quantity = int(input("\nСколько вакансий выводить за один раз?: "))
            if quantity > 0: break
        except Exception:
            continue
    if len(vacancies):
        print(f"Будет выводиться по {quantity} вакансий за раз. Для продолжения нажимайте Enter\n")
        count = round(len(vacancies) / quantity)
        start, end = 0, quantity
        while count >= 0:
            input()
            [print(vacancy) for vacancy in vacancies[start:end]]
            start += quantity
            end += quantity
            count -= 1
    else:
        print("Вакансий нет")
