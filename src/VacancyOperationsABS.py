from abc import ABC, abstractmethod


class VacancyOperations(ABC):
    """ Абстрактный класс реализации операций фильтрации, сортировки, удаления вакансий. """

    @abstractmethod
    def filter_vacancies(self, vacancies: list[dict], keyword: str) -> list[dict]:
        """ Метод фильтрации вакансий по ключевому слову. """
        pass

    @abstractmethod
    def sort_vacancies(self, vacancies: list[object], keyword: str, sort_type: bool = False) -> list[dict]:
        """ Метод сортировки вакансий по заданному полю с учетом заданного направления сортировки. """
        pass

    @abstractmethod
    def get_top_N(self, vacancies: list[object], salary_amount: int):
        """ Метод возвращает топ N вакансий по уровню зарплат. """
        pass

    @abstractmethod
    def delete_vacancies(self, vacancies: list[object], vac_id: str) -> list[dict]:
        pass
