from VacancyOperationsABS import VacancyOperations


class UserOperations(VacancyOperations):
    """ Класс реализации операций фильтрации, сортировки, удаления вакансий. """

    def filter_vacancies(self, vacancies: list[dict], keyword: str) -> list[dict]:
        """ Метод фильтрации вакансий по ключевому слову. """
        search = input("Фильтровать по должности (0) или зарплате (1)")
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

    def sort_vacancies(self, vacancies: list[dict]) -> list[object]:
        """ Метод сортировки вакансий по заданному полю с учетом заданного направления сортировки. """
        print("По какому полю сортировать:")
        sort_field_matrix = {
            0: 'id_num',
            1: 'name',
            2: 'area',
            3: 'salary',
            4: 'experience'
        }
        sort_field = int(input(
            '0. ID'
            '1. Должность'
            '2. Регион'
            '3. Зарплата'
            '4. Требуемый опыт'
        ))
        print("Направление сортировки:")
        sort_type = int(input(
            '0. По возрастанию'
            '1. По убыванию'
        ))
        return vacancies.sort(key=lambda x: x.id_num, reverse=bool(sort_type))

    def get_top_N(self, vacancies: list[dict], salary_amount: int):
        """ Метод возвращает топ N вакансий по уровню зарплат. """
        pass

    def delete_vacancies(self, vacancies: list[dict], vac_id: str) -> list[dict]:
        pass
