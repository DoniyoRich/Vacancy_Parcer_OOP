from unittest.mock import patch

from src.User import User
from src.constants import USER_MENU_LIST
from src.main import intro, main


def test_intro(capsys) -> None:
    """ Тест приветствия. """
    intro()
    data = capsys.readouterr()
    assert "Добро пожаловать в программу получения и обработки вакансий с сайта hh.ru" in data.out


@patch.object(User, 'query_to_search')
@patch('src.main.user_menu', return_value=0)
def test_main_over(mocked_choice, mocked_query, capsys):
    mocked_query.return_value = 'python'

    main()
    mocked_choice.assert_called_once_with(USER_MENU_LIST)
    captured = capsys.readouterr()
    assert 'Хорошего дня' in captured.out


# @patch.object(User, 'filter_vacancies')
# @patch.object(User, 'query_to_search')
# @patch('src.main.user_menu', return_value=1)
# def test_main_filter(mocked_choice, mocked_query, mocked_filter):
#     mocked_query.return_value = 'python'
#
#     main()
#     mocked_choice.assert_called_once_with(USER_MENU_LIST)
#     mocked_filter.assert_called_once()


# @patch('src.main.output_to_console')
# @patch.object(User, 'query_to_search')
# @patch('src.main.user_menu', return_value=1)
# def test_main_output(mocked_choice, mocked_query, mocked_output):
#     mocked_query.return_value = 'python'
#     vacancies = [{}, {}]
#
#     main()
#     mocked_choice.assert_called_once_with(USER_MENU_LIST)
#     mocked_output.assert_called(vacancies)
