from src.Vacancy import Vacancy


def test_vacancy_init(some_vacancy):
    vacancy = Vacancy(*some_vacancy)
    assert vacancy.id_num == '123456'
    assert vacancy.name == 'Разработчик Python'
    assert vacancy.area == 'Москва'
    assert vacancy.alt_url == 'http://blabla.ru'
    assert vacancy.salary == 15000
    assert vacancy.experience == 'без опыта'


def test_cast_to_object_list():
    pass


def test_validate_salary():
    vacancy_from_none = Vacancy('123456', 'Разработчик', 'Москва', 'http://blabla.ru', None, 180000, 'от 1 года')
    vacancy_to_none = Vacancy('123456', 'Разработчик', 'Москва', 'http://blabla.ru', 150000, None, 'от 1 года')
    vacancy_both_none = Vacancy('123456', 'Разработчик', 'Москва', 'http://blabla.ru', None, None, 'от 1 года')

    assert vacancy_from_none.salary == 180000
    assert vacancy_to_none.salary == 150000
    assert vacancy_both_none.salary == 0