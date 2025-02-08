from abc import ABC, abstractmethod


class VacancyOperations(ABC):
    """ Абстрактный класс реализации операций фильтрации, сортировки, удаления вакансий. """

    @abstractmethod
    def filter_vacancies(self, vacancies: list[dict], keyword: str) -> list[dict]:
        """ Метод фильтрации вакансий по ключевому слову. """
        pass

    @abstractmethod
    def sort_vacancies(self, vacancies: list[dict], keyword: str, sort_type: bool = False) -> list[dict]:
        """ Метод сортировки вакансий по заданному полю с учетом заданного направления сортировки. """
        pass

    @abstractmethod
    def delete_vacancies(self, vacancies: list[dict], vac_id: str) -> list[dict]:
        pass
