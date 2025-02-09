from abc import ABC, abstractmethod


class VacancyOperations(ABC):
    """ Абстрактный класс реализации операций фильтрации, сортировки, удаления вакансий. """

    @abstractmethod
    def filter_vacancies(self) -> None:
        """ Метод фильтрации вакансий по ключевому слову. """
        pass

    @abstractmethod
    def sort_vacancies(self) -> None:
        """ Метод сортировки вакансий по заданному полю с учетом заданного направления сортировки. """
        pass

    @abstractmethod
    def get_top_N(self) -> None:
        """ Метод возвращает топ N вакансий по уровню зарплат. """
        pass

    @abstractmethod
    def delete_vacancies(self) -> None:
        pass
