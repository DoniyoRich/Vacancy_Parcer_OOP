from unittest.mock import patch

from src.constants import FILTER_MENU
from src.HeadHunterAPI import HeadHunterAPI
from src.JSONSaver import JSONSaver
from src.User import User
from src.Vacancy import Vacancy


@patch.object(Vacancy, 'cast_to_object_list')
@patch.object(JSONSaver, 'save_to_file')
@patch.object(HeadHunterAPI, "vacancies")
@patch.object(HeadHunterAPI, 'get_vacancies')
@patch('builtins.input', return_value='python')
def test_query_to_search(mocked_input, mocked_hh_api, mocked_vac, mocked_save, mocked_vac_class) -> None:
    """ Тестирование метода запроса поисковой строки от Пользователя и ее обработки. """
    user = User()
    user.query_to_search()

    mocked_save.assert_called_once()
    mocked_vac_class.assert_called_once()


@patch('src.User.user_menu', side_effect=[0, 1, 2])
def test_filter_vacancies(mocked_choice, some_test_list_of_objects) -> None:
    """ Тестирование метода фильтрации вакансий. """
    user = User()
    user.vacancies = some_test_list_of_objects

    with patch('builtins.input', return_value="python") as mock_name, \
            patch('src.User.output_to_console') as mock_output, \
            patch('src.User.ask_to_save') as mock_ask:
        user.filter_vacancies()  # user_choice = 0
        mocked_choice.assert_called_once_with(FILTER_MENU)
        filtered = [vacancy for vacancy in user.vacancies if mock_name.return_value.lower() in vacancy.name.lower()]
        mock_output.assert_called_with(filtered)
        mock_ask.assert_called_once()

    with patch('builtins.input', return_value="90000, 180000") as mock_name, \
            patch('src.User.output_to_console') as mock_output, \
            patch('src.User.ask_to_save') as mock_ask:
        user.filter_vacancies()  # user_choice = 1

        mocked_choice.assert_called_with(FILTER_MENU)
        sal_down = int(mock_name.return_value.split(',')[0])
        sal_up = int(mock_name.return_value.split(',')[1])
        filtered = [vacancy for vacancy in user.vacancies if sal_down < vacancy.salary < sal_up]
        mock_output.assert_called_once_with(filtered)
        mock_ask.assert_called_once()

    with patch('builtins.input', return_value="Краснодар") as mock_name, \
            patch('src.User.output_to_console') as mock_output, \
            patch('src.User.ask_to_save') as mock_ask:
        user.filter_vacancies()  # user_choice = 2
        mocked_choice.assert_called_with(FILTER_MENU)
        filtered = [vacancy for vacancy in user.vacancies if mock_name.return_value in vacancy.area]
        mock_output.assert_called_once_with(filtered)
        mock_ask.assert_called_once()


@patch('src.User.user_menu', side_effect=[0, 1])
def test_sort_vacancies(mocked_choice, some_test_list_of_objects, sorted_vacancies) -> None:
    """ Тестирование метода сортировки вакансий. """
    user = User()
    user.vacancies = some_test_list_of_objects
    user.sort_vacancies()

    assert mocked_choice.call_count == 2
    assert user.vacancies == sorted_vacancies


@patch('src.User.ask_to_save')
@patch('src.User.output_to_console')
@patch('builtins.input', return_value=3)
def test_get_top_n(mocked_input, mocked_output, mocked_ask, some_test_list_of_objects, top_3_vacancies) -> None:
    """ Тестирование метода топ зарплат. """
    user = User()
    user.vacancies = some_test_list_of_objects
    user.get_top_n()
    user.vacancies.sort(key=lambda x: x.salary, reverse=True)

    assert user.vacancies[:mocked_input.return_value] == top_3_vacancies
    mocked_output.assert_called_once()
    mocked_ask.assert_called_once()


@patch('src.User.ask_to_save')
@patch('src.User.output_to_console')
@patch('builtins.input', return_value='python')
def test_delete_vacancies(mocked_input, mocked_output, mocked_ask, some_test_list_of_objects, after_deletion) -> None:
    """ Тестирование метода удаления вакансий. """
    user = User()
    user.vacancies = some_test_list_of_objects
    user.delete_vacancies()

    assert [x for x in user.vacancies if mocked_input.return_value.lower() not in x.name.lower()] == after_deletion
    mocked_output.assert_called_once()
    mocked_ask.assert_called_once()
