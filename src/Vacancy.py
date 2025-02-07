class Vacancy:
    """ Класс для работы с вакансиями. """
    __slots__ = (
        '__id', '__name', '__area', '__alt_url', '__salary_from', '__salary_to', '__salary_max', '__experience')

    __id: str  # уникальный номер вакансии
    __name: str  # название вакансии
    __area: str  # регион
    __alt_url: str  # ссылка на вакансию
    __salary_from: int  # зарплата "от"
    __salary_to: int  # зарплата "до"
    __salary_max: int | str  # зарплата максимальная
    __experience: str  # требуемый опыт

    def __init__(self, id_, name, area, alt_url, salary_from, salary_to, experience) -> None:
        """ Конструктор класса. Предусмотрена валидация значения зарплаты. """
        self.__id = id_
        self.__name = name
        self.__area = area
        self.__alt_url = alt_url
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__salary_max = int(max(self.__salary_from, self.__salary_to))
        self.__experience = experience

    def __lt__(self, other):
        """ Магический метод 'меньше' """
        return self.__salary_max < other.__salary_max

    def __eq__(self, other):
        """ Магический метод 'равно' """
        return self.__salary_max == other.__salary_max

    def __gt__(self, other):
        """ Магический метод 'больше' """
        return self.__salary_max > other.__salary_max

    def __str__(self):
        curr = 'руб.'
        if not self.__salary_max:
            self.__salary_max = 'не указана'
            curr = ''
        return f'ID: {self.__id}, должность: {self.__name}, регион: {self.__area}, зарплата: {self.__salary_max} {curr}, требуемый опыт: {self.__experience}, ссылка на вакансию: {self.__alt_url}'

    def cast_to_object_list(self, vacancies: list[dict]):
        pass
