from abc import ABC, abstractmethod

class BaseParser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> list[str]:
        """Парсит файл и возвращает список строк (номеров)"""
        pass