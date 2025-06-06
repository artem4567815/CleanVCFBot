from infrastructure.file_parsers.base_parser import BaseParser
from docx import Document



class DocParser(BaseParser):
    def parse(self, file_path: str) -> list[str]:
        """Парсит файл .docx и возвращает список строк (номеров)"""
        doc = Document(file_path)
        return [para.text.strip() for para in doc.paragraphs if para.text.strip()]