from infrastructure.file_parsers.base_parser import BaseParser

class TxtParser(BaseParser):
    def parse(self, file_path: str) -> list[str]:
        """Парсит файл .txt и возвращает список строк (номеров)"""
        with open(file_path, encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]