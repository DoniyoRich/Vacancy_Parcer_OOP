from abc import ABC, abstractmethod


class Parser(ABC):
    """ Абстрактный класс для работы с API сайта hh.ru. """

    @abstractmethod
    def _load_vacancies(self) -> None:
        """ Абстрактный инкапсулированный метод загрузки вакансий с сайта. """
        pass

    @abstractmethod
    def get_vacancies(self) -> None:
        """ Абстрактный метод получения вакансий с сайта. """
        pass
