import json

from src.FileSaverABS import FileSaver


class JSONSaver(FileSaver):
    """ Класс работы с файлами JSON. Реализован метод сохранения списка вакансий в файл. """

    def save_to_file(self, vacancy: list[dict], filename: str = 'vacancies') -> None:
        """
        Метод сохраняет полученный список вакансий в файл формата JSON.
        """
        with open(filename + ".json", "a", encoding="utf-8") as file:
            json.dump(vacancy, file, ensure_ascii=False, indent=4)
