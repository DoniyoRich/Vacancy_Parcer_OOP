import json

import requests
from Parser import Parser


class HeadHunterAPI(Parser):
    """ Класс для работы с API HeadHunter. Наследуется от класса Parser. """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'area': '1'}
        self.vacancies = []
        super().__init__(file_worker)

    def _load_vacancies(self, keyword):
        """ Метод получения вакансий с сайта. """
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            print(response, self.params.get('page'))
            if response.status_code == 200:
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)

            else:
                print("Что-то не так с запросом, ошибка:", response.status_code)
            self.params['page'] += 1

    def get_vacancies(self, search):
        # Получение вакансий с hh.ru в формате JSON
        self._load_vacancies(search)
        print(self.vacancies)
        print(len(self.vacancies))

        with open('some_vacs.txt', "w", encoding="utf-8", ) as file_name:
            json.dump(self.vacancies, file_name, ensure_ascii=False, indent=4)
