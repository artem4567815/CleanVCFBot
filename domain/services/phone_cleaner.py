from domain.value_objects.phone_number import PhoneNumber

def clean_numbers(raw_numbers: list[str]) -> list[str]:
    """Вернуть уникальные и валидные номера в формате +7XXXXXXXXXX"""
    numbers = [PhoneNumber(raw) for raw in raw_numbers]
    valid = {str(num) for num in numbers if num.is_valid()}
    return sorted(valid)