from infrastructure.file_parsers.base_parser import BaseParser
import pandas as pd

class XlsxParser(BaseParser):
    def parse(self, file_path: str) -> list[str]:
        """Парсит файл Excel и возвращает список строк (номеров)"""
        df = pd.read_excel(file_path, engine='openpyxl')
        return df.iloc[:, 0].dropna().astype(str).tolist()
