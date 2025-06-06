import os

def generate_vcf(numbers: list[str], tmpdir: str) -> str:
    filename = os.path.join(tmpdir, "contacts.vcf")
    with open(filename, "w", encoding="utf-8") as f:
        for i, num in enumerate(numbers, 1):
            f.write(
                f"BEGIN:VCARD\nVERSION:3.0\nFN:Contact {i}\nTEL;TYPE=CELL:{num}\nEND:VCARD\n"
            )
    return filename