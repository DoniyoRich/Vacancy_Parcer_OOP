from abc import ABC, abstractmethod


class FileSaver(ABC):

    @abstractmethod
    def save_to_file(self, vacancy):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass
