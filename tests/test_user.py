from unittest.mock import patch, Mock


@patch('builtins.input', return_value='python владивосток')
def test_query_to_search(mock_input):
    pass


def test_filter_vacancies():
    pass


def test_sort_vacancies():
    pass


def test_get_top_n():
    pass


def test_delete_vacancies():
    pass
