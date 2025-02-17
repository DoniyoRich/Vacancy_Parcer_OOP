from unittest.mock import patch, Mock

from src.HeadHunterAPI import HeadHunterAPI
from src.User import User
from src.constants import FILTER_MENU


# @patch('src.HeadHunterAPI.get_vacancies')
# @patch('builtins.input', return_value='python')
# def test_query_to_search(mocked_input, mocked_HH_API):
#     hh_test = HeadHunterAPI(mocked_input.return_value, file_worker='test')


@patch('src.User.user_menu', side_effect=[0, 1, 2])
def test_filter_vacancies(mocked_choice, some_test_list_of_objects):
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


def test_sort_vacancies() -> None:
    pass


def test_get_top_n() -> None:
    pass


def test_delete_vacancies() -> None:
    pass
