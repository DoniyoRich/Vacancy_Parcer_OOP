import json

from src.FileSaver import FileSaver


class JSONSaver(FileSaver):
    """ Класс ... """

    def save_to_file(self, vacancy: list[dict]):
        with open('file', 'w', encoding='utf-8') as file:
            json.dump(vacancy, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):
        pass

    def delete_vacancy(self, vacancy):
        pass
