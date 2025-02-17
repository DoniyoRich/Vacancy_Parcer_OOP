from src.Vacancy import Vacancy


def test_vacancy_init(some_vacancy) -> None:
    """ Тест на инициализацию объекта. """
    vacancy = Vacancy(*some_vacancy)
    assert vacancy.id_num == '123456'
    assert vacancy.name == 'Разработчик Python'
    assert vacancy.area == 'Москва'
    assert vacancy.alt_url == 'http://blabla.ru'
    assert vacancy.salary == 15000
    assert vacancy.experience == 'без опыта'


def test_validate_salary_from_ok(vacancy_from_ok) -> None:
    """ Тест на валидацию зарплаты в случае ее наличия в ответе на запрос. """
    assert Vacancy.validate(vacancy_from_ok, 'from') == 1500


def test_validate_salary_to_none(vacancy_to_none) -> None:
    """ Тест на валидацию зарплаты в случае ее отсутствия в ответе на запрос. """
    assert Vacancy.validate(vacancy_to_none, 'to') == 0


def test_validate_salary() -> None:
    """ Тест на валидацию зарплаты во время инициализации объекта. """
    vacancy_from_none = Vacancy('123456', 'Разработчик', 'Москва', 'http://blabla.ru', None, 180000, 'от 1 года')
    vacancy_to_none = Vacancy('123456', 'Разработчик', 'Москва', 'http://blabla.ru', 150000, None, 'от 1 года')
    vacancy_both_none = Vacancy('123456', 'Разработчик', 'Москва', 'http://blabla.ru', None, None, 'от 1 года')

    assert vacancy_from_none.salary == 180000
    assert vacancy_to_none.salary == 150000
    assert vacancy_both_none.salary == 0


def test_dunders() -> None:
    """ Тестирование магических методов. """
    vac1 = Vacancy('123456', 'Разработчик', 'Москва', 'http://blabla.ru', 120000, 145000, 'от 1 года')
    vac2 = Vacancy('123457', 'Разработчик', 'Москва', 'http://blabla.ru', 150000, 180000, 'от 1 года')
    vac3 = Vacancy('123458', 'Разработчик', 'Москва', 'http://blabla.ru', 130000, 180000, 'от 1 года')
    vac4 = Vacancy('123459', 'Разработчик', 'Москва', 'http://blabla.ru', None, None, 'от 1 года')

    assert vac1 < vac2
    assert vac2 > vac1
    assert vac2 == vac3
    assert str(
        vac1) == 'ID: 123456, должность: Разработчик, регион: Москва, зарплата: 145000 руб., требуемый опыт: от 1 года, ссылка на вакансию: http://blabla.ru'
    assert str(
        vac4) == 'ID: 123459, должность: Разработчик, регион: Москва, зарплата: не указана , требуемый опыт: от 1 года, ссылка на вакансию: http://blabla.ru'
