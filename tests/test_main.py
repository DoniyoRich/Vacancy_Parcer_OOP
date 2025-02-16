from unittest.mock import Mock, patch

from src.User import User
from src.main import intro, main


def test_intro(capsys):
    """ Тест приветствия. """
    intro()
    data = capsys.readouterr()
    assert "Добро пожаловать в программу получения и обработки вакансий с сайта hh.ru" in data.out


# @patch('builtins.input', side_effect=list(range(8)))
# @patch('builtins.input', return_value='python')
# def test_main(mocked_search, mocked_choice, capsys):
#     assert mocked_search.return_value == 'python'
#     mock_user = Mock(spec=User)
#     main()
#     mocked_choice()
#     captured = capsys.readouterr()
#     assert "Хорошего дня" in captured.out
