import requests

from src.ParserABS import Parser


class HeadHunterAPI(Parser):
    """ Класс для работы с API сайта hh.ru. Наследуется от класса Parser. """
    __slots__ = ('url', 'headers', 'params', 'vacancies', 'search', 'file_worker')

    def __init__(self, search: str, file_worker: str = 'vacancies_api.json') -> None:
        self.url = 'https://api.hh.ru/vacancies'
        self.headers: dict = {'User-Agent': 'HH-User-Agent'}
        self.params: dict = {'text': '', 'page': 0, 'per_page': 100, 'host': 'hh.ru'}
        self.vacancies: list[dict] = []
        self.search = search
        self.file_worker = file_worker

    def _load_vacancies(self) -> None:
        """ Метод получения вакансий с сайта. """
        self.params['text'] = self.search
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
            else:
                print("  Что-то пошло не так с запросом, ошибка:", response.status_code)
            self.params['page'] += 1
            print("\rЗагружаю вакансии с сайта hh.ru. Завершено:", str(self.params['page'] * 100 // 20) + "%",
                  end="")

    def get_vacancies(self) -> None:
        """
        Доступный метод получения вакансий с hh.ru в формате JSON.
        Вызывает инкапсулированный метод _load_vacancies(self) для обращения к API сайта hh.ru
        и загрузки вакансий
        """
        self._load_vacancies()
