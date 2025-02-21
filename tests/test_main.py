from unittest.mock import patch

from src.constants import USER_MENU_LIST
from src.main import intro, main
from src.User import User


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
