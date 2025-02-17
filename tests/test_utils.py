from src.utils import convert_to_list


def test_convert_to_list(some_test_list_of_objects):
    converted = convert_to_list(some_test_list_of_objects)
    assert converted[0]['ID'] == 21596875
    assert converted[0]['должность'] == 'Разработчик Python'
    assert converted[1]['зарплата'] == 90000
    assert converted[1]['требуемый опыт'] == 'без опыта'
    assert converted[3]['зарплата'] == 250000
    assert converted[4]['требуемый опыт'] == 'от 3 лет'
    assert converted[5]['ID'] == 98743216
    assert converted[5]['должность'] == 'Senior Python Developer'
    assert converted[5]['ссылка на вакансию'] == 'http://blabla68.ru'
    assert converted[6]['регион'] == 'Екатеринбург'


def test_user_menu() -> None:
    pass


def test_saving_file() -> None:
    pass


def test_ask_to_save() -> None:
    pass


def test_output_to_console() -> None:
    pass
