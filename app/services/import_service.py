from infrastructure.file_parsers.factory import get_parser
from domain.services.phone_cleaner import clean_numbers
from infrastructure.vcf.vcf_generator import generate_vcf

class ImportContactsService:
    def import_and_generate_vcf(self, file_path: str, tmpdir: str) -> str:
        parser = get_parser(file_path)
        raw_numbers = parser.parse(file_path)
        clean = clean_numbers(raw_numbers)
        vcf_path = generate_vcf(clean, tmpdir)
        return vcf_path