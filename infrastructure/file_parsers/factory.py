from infrastructure.file_parsers.base_parser import BaseParser

from infrastructure.file_parsers.doc_parser import DocParser
from infrastructure.file_parsers.txt_parser import TxtParser
from infrastructure.file_parsers.xlsx_parser import XlsxParser


def get_parser(file_path: str) -> BaseParser:
    """Возвращает соответствующий парсер в зависимости от расширения файла"""

    if file_path.endswith('.xlsx'):
        return XlsxParser()
    elif file_path.endswith('.txt'):
        return TxtParser()
    elif file_path.endswith('.docx') or file_path.endswith('.doc'):
        return DocParser()
    else:
        raise ValueError(f"Unsupported file type: {file_path}")