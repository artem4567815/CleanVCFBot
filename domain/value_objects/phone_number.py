from domain.services.phone_format import normalize_phone

class PhoneNumber:
    def __init__(self, raw: str):
        self.raw = raw
        self.number = normalize_phone(raw)

    def is_valid(self):
        return self.number is not None

    def __str__(self):
        return self.number or ""

    def __eq__(self, other):
        return isinstance(other, PhoneNumber) and self.number == other.number

    def __hash__(self):
        return hash(self.number)