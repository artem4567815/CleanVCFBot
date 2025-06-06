import phonenumbers
import string



def normalize_phone(raw: str) -> str | None:
    """Преобразовать строку в формат +7XXXXXXXXXX или None, если невалиден"""
    digits = ''.join(str(raw) if raw[0] != '+' else raw[1:])
    
    out = ""
    for x in digits:
        if x.isdigit():
            out += x
    digits = out

    if len(digits) == 11 and digits.startswith('8'):
        digits = '7' + digits[1:]
    elif len(digits) == 10:
        digits = '7' + digits
    elif len(digits) == 11 and digits.startswith('7'):
        pass
    else:
        return None

    try:
        pn = phonenumbers.parse('+' + digits, None)
        if phonenumbers.is_valid_number(pn):
            return phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.E164)
    except Exception:
        return None
    return None