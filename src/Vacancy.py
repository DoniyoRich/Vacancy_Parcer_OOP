class Vacancy:
    """
    Класс для работы с вакансиями.
    Создает объект Вакансия с некоторыми полями, выбранными из JSON ответа от API hh.ru.
    Магические методы реализуют операции сравнения объектов Вакансия по уровню максимальной зарплаты.
    """
    __slots__ = (
        '__id', '__name', '__area', '__alt_url', '__salary_from', '__salary_to', '__salary_max', '__experience')

    __id: int  # уникальный номер вакансии
    __name: str  # название вакансии
    __area: str  # регион
    __alt_url: str  # ссылка на вакансию
    __salary_from: int  # зарплата "от"
    __salary_to: int  # зарплата "до"
    __salary_max: int  # зарплата максимальная (берется максимум от зарплат ОТ и ДО
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

    @property
    def id_num(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def area(self) -> str:
        return self.__area

    @property
    def alt_url(self) -> str:
        """ Возвращает ссылку на вакансию. """
        return self.__alt_url

    @property
    def salary(self) -> int | str:
        """ Возвращает значение зарплаты. """
        return self.__salary_max

    @property
    def experience(self) -> str:
        """ Возвращает требуемый опыт. """
        return self.__experience

    def __lt__(self, other) -> bool:
        """ Магический метод сравнивает уровень зарплат по критерию 'меньше'. """
        return self.salary < other.salary

    def __eq__(self, other) -> bool:
        """ Магический метод сравнивает уровень зарплат по критерию 'равно'. """
        return self.salary == other.salary

    def __gt__(self, other) -> bool:
        """ Магический метод сравнивает уровень зарплат по критерию 'больше'. """
        return self.salary > other.salary

    def __str__(self) -> str:
        curr = 'руб.'
        salary_amount = self.salary
        if not self.salary:
            salary_amount = 'не указана'
            curr = ''
        return f'ID: {self.id_num}, должность: {self.name}, регион: {self.area}, зарплата: {salary_amount} {curr}, требуемый опыт: {self.experience}, ссылка на вакансию: {self.alt_url}'

    @staticmethod
    def cast_to_object_list(vacancies: list[dict]) -> list[object]:
        """ Метод преобразования набора данных из JSON в список объектов. """
        vacancies_objects = []
        for ind, vacancy in enumerate(vacancies):
            id_ = int(vacancy['id'])
            name = vacancy['name']
            area = vacancy['area']['name']
            alt_url = vacancy['alternate_url']
            salary_from = __class__.__validate_salary(vacancy, 'from')
            salary_to = __class__.__validate_salary(vacancy, 'to')
            experience = vacancy['experience']['name']
            vacancies_objects.append(__class__(id_, name, area, alt_url, salary_from, salary_to, experience))

        return vacancies_objects

    @classmethod
    def __validate_salary(cls, vacancy: dict, param_to_check: str) -> float:
        """ Метод проверяет на валидность значения полей. """
        try:
            salary_ = float(vacancy['salary'][param_to_check])
        except Exception:
            salary_ = 0
        return salary_
