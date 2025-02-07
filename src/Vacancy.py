class Vacancy:
    """ Класс для работы с вакансиями. """

    __name: str  # название вакансии
    __alt_url: str  # ссылка на вакансию
    __salary_from: int | float  # зарплата "от"
    __salary_to: int | float  # зарплата "до"
    __salary_max: int | float  # зарплата максимальная
    __experience: str  # требуемый опыт

    def __init__(self, name, area, alt_url, salary_from, salary_to, experience) -> None:
        """ Конструктор класса. Предусмотрена валидация значения зарплаты. """
        self.__name = name
        self.__area = area
        self.__alt_url = alt_url
        try:
            # если зарплата указана, то инициализируем переменную
            if isinstance(salary_from, int | float):
                self.__salary_from = salary_from
        except TypeError:
            # иначе выставляем значение в 0
            self.__salary_from = 0
        try:
            # если зарплата указана, то инициализируем переменную
            if isinstance(salary_to, int | float):
                self.__salary_to = salary_to
        except TypeError:
            # иначе выставляем значение в 0
            self.__salary_to = 0
        self.__salary_max = max(self.__salary_from, self.__salary_to)
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

    # @staticmethod
    def cast_to_object_list(self, vacancies):
        vac_objects = []
        for vacancy in vacancies:
            name = vacancy['name']
            area = vacancy['area']['name']
            alt_url = vacancy['alternate_url']
            salary_from = vacancy['salary']['from']  # !!!!
            salary_to = vacancy['salary']['to']  # !!!!
            experience = vacancy['experience']['id']
            vac_objects.append(self.__init__(name, area, alt_url, salary_from, salary_to, experience))
