from abc import ABC, abstractmethod


class Parser(ABC):
    """ Абстрактный класс для работы с HeadHunterAPI. """

    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def _load_vacancies(self):
        """ Абстрактный метод загрузки вакансий с сайта. """
        pass

    @abstractmethod
    def get_vacancies(self):
        """ Абстрактный метод получения вакансий с сайта. """
        pass
