def convert_to_list(vacancies: list[object]) -> list[dict]:
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
