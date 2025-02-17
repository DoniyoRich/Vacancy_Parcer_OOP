import json

from src.Vacancy import Vacancy
from src.constants import TEST_DATA_SETS

import pytest


@pytest.fixture
def some_list_of_vacancies():
    """ Тестовый список словарей."""
    return [
        {
            "id": "117258854",
            "name": "Семейный повар",
            "area": {
                "id": "78",
                "name": "Самара",
                "url": "https://api.hh.ru/areas/78?host=hh.ru"
            },
            "salary": {
                "from": 80000,
                "to": 150000,
                "currency": "RUR",
                "gross": True
            },
            "alternate_url": "https://hh.ru/vacancy/117258854",
        },
        {
            "id": "117261906",
            "name": "Главный инженер проекта",
            "area": {
                "id": "78",
                "name": "Самара",
                "url": "https://api.hh.ru/areas/82?host=hh.ru"
            },
            "salary": {
                "from": 160000,
                "to": None,
                "currency": "RUR",
                "gross": True
            },
            "alternate_url": "https://hh.ru/vacancy/117261903"
        }
    ]


@pytest.fixture
def some_json_from_api():
    with open(TEST_DATA_SETS + 'test_set_json.json', encoding='utf-8') as file:
        json_dict = json.loads(file.read())
    return json_dict


@pytest.fixture
def lisf_of_dicts_api():
    with open(TEST_DATA_SETS + 'test_list_dicts_api.txt', encoding='utf-8') as file:
        list_dicts = json.loads(file.read())
    return list_dicts


@pytest.fixture
def vacancy_from_ok():
    with open(TEST_DATA_SETS + 'vac_from_ok.txt', encoding='utf-8') as file:
        list_dicts = json.loads(file.read())
    return list_dicts


@pytest.fixture
def vacancy_to_none():
    with open(TEST_DATA_SETS + 'vac_to_none.txt', encoding='utf-8') as file:
        list_dicts = json.loads(file.read())
    return list_dicts


@pytest.fixture
def some_vacancy():
    return ['123456', 'Разработчик Python', 'Москва', 'http://blabla.ru', 10000, 15000, 'без опыта']


@pytest.fixture
def some_test_list_of_objects():
    return [
        Vacancy('21596875', 'Разработчик Python', 'Москва', 'http://blabla11.ru', 100000, 120000, 'от 1 года'),
        Vacancy('65432498', 'Junior python developer', 'Хабаровск', 'http://blabla22.ru', 70000, 90000, 'без опыта'),
        Vacancy('98432455', 'Junior-разработчик Java', 'Москва', 'http://blabla33.ru', 80000, None, 'без опыта'),
        Vacancy('98435481', 'Middle+ Python developer', 'Москва', 'http://blabla44.ru', None, 250000, 'от 3 до 6 лет'),
        Vacancy('32113874', 'Системный аналитик', 'Краснодар', 'http://blabla55.ru', 10000, 15000, 'от 3 лет'),
        Vacancy('98743216', 'Senior Python Developer', 'Москва', 'http://blabla68.ru', 350000, 400000, '6 лет и более'),
        Vacancy('32198752', 'QA тестировщик', 'Екатеринбург', 'http://blabla77.ru', 140000, 160000, 'от 3 лет')
    ]
