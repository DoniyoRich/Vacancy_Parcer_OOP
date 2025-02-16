from unittest.mock import patch

from src.HeadHunterAPI import HeadHunterAPI


def test_hh_init():
    """ Тест инициализации экземпляра класса HeadHunterAPI. """
    hh_test = HeadHunterAPI('python', 'vacancies.json')
    assert hh_test.url == 'https://api.hh.ru/vacancies'
    assert hh_test.headers == {'User-Agent': 'HH-User-Agent'}
    assert hh_test.params == {'text': '', 'page': 0, 'per_page': 100, 'host': 'hh.ru'}
    assert hh_test.vacancies == []
    assert hh_test.search == 'python'
    assert hh_test.file_worker == 'vacancies.json'


@patch('requests.get')
def test_hh_load_vacancies(mock_get, some_json_from_api, lisf_of_dicts_api, capsys):
    """ Тест получения вакансий. """
    hh_test = HeadHunterAPI('python Москва')
    with patch.object(hh_test, 'params', {'text': '', 'page': 19, 'per_page': 1, 'host': 'hh.ru'}):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = some_json_from_api
        hh_test.get_vacancies()
        assert hh_test.vacancies == lisf_of_dicts_api

        captured = capsys.readouterr()
        print(captured.out)
        assert 'Загружаю вакансии с сайта hh.ru. Завершено:' in captured.out


@patch('requests.get')
def test_hh_load_vacancies_fail(mock_get, capsys):
    """ Тест на неудачный запрос. """
    hh_test = HeadHunterAPI('python Москва')
    with patch.object(hh_test, 'params', {'text': '', 'page': 19, 'per_page': 1, 'host': 'hh.ru'}):
        mock_get.return_value.status_code = 400
        hh_test.get_vacancies()
        assert hh_test.vacancies == []

        captured = capsys.readouterr()
        print(captured.out)
        assert 'Что-то пошло не так с запросом, ошибка' in captured.out
