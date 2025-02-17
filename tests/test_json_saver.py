from unittest.mock import mock_open, patch

from src.JSONSaver import JSONSaver


def test_save_to_file(some_list_of_vacancies) -> None:
    """ Тест на сохранение файла формата json. """
    file_name = "test"
    with patch('builtins.open', mock_open()) as mocked_file:
        saver = JSONSaver()
        saver.save_to_file(some_list_of_vacancies, file_name)

        mocked_file.assert_called_once_with(file_name + ".json", "a", encoding="utf-8")
        mocked_file().write.assert_called()
