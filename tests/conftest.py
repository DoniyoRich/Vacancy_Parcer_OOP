import json
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
def some_vacancy():
    return ['123456', 'Разработчик Python', 'Москва', 'http://blabla.ru', 10000, 15000, 'без опыта']
