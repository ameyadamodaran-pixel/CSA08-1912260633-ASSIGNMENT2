# Q3 - Vehicle Registration Number Validator
# No regular expressions are used.

def normalise(text):
    """Remove spaces and hyphens and convert to uppercase."""
    return text.replace(" ", "").replace("-", "").upper()


def is_valid(reg):
    """Format: 2 letters + 2 digits + 1/2 letters + 4 digits."""
    if len(reg) not in (9, 10):
        return False
    if not reg[0:2].isalpha():
        return False
    if not reg[2:4].isdigit():
        return False
    if len(reg) == 9:
        series = reg[4:5]
        number = reg[5:9]
    else:
        series = reg[4:6]
        number = reg[6:10]
    return series.isalpha() and number.isdigit()


def format_receipt(reg):
    if not is_valid(reg):
        return "INVALID"
    if len(reg) == 9:
        return f"{reg[:2]} {reg[2:4]} {reg[4:5]} {reg[5:]}"
    return f"{reg[:2]} {reg[2:4]} {reg[4:6]} {reg[6:]}"


samples = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "KL-07-C-4567",
    "MH 12 XY 9876",
]
for raw in samples:
    reg = normalise(raw)
    print(f"{raw:<18} -> {reg:<12} {format_receipt(reg)}")

print("\nSLICING CHECK")
print("9 characters: s[-4:] =", "TN09AB1234"[:9][-4:])
print("9 characters: s[4:-4] =", "TN09AB1234"[:9][4:-4])
print("10 characters: s[-4:] =", "TN09AB1234"[-4:])
print("10 characters: s[4:-4] =", "TN09AB1234"[4:-4])
