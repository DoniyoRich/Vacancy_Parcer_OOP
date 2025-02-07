from src.FileSaver import FileSaver
import pandas as pd



class ExcelSaver(FileSaver):
    """ Класс ... """

    def save_to_file(self, vacancy):
        df = pd.DataFrame(vacancy)
        df.to_excel('file.xlsx', index=False)

    def add_vacancy(self, vacancy):
        pass

    def delete_vacancy(self, vacancy):
        pass
