import json

import requests
from Parser import Parser


class HeadHunterAPI(Parser):
    """ Класс для работы с API HeadHunter. Наследуется от класса Parser. """
    __slots__ = ('url', 'headers', 'params', 'vacancies', 'search')

    def __init__(self, file_worker, search):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'host': 'hh.ru'}
        self.vacancies = []
        self.search = search
        super().__init__(file_worker)

    def _load_vacancies(self):
        """ Метод получения вакансий с сайта. """
        self.params['text'] = self.search
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)

            else:
                print("\nЧто-то не так с запросом, ошибка:", response.status_code)
            self.params['page'] += 1
            print("\rЗагружаю вакансии с сайта hh.ru. Завершено:", str(self.params['page'] * 100 // 20) + "%",
                  end="")
        print('\n\n')

    def get_vacancies(self):
        # Получение вакансий с hh.ru в формате JSON
        self._load_vacancies()

        with open(self.file_worker, "a", encoding="utf-8", ) as file_name:
            json.dump(self.vacancies, file_name, ensure_ascii=False, indent=4)
