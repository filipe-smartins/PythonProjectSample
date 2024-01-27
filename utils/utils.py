def capitalized_name(name: str) -> str:
    return name.capitalize()


def upper_name(name: str) -> str:
    return name.upper()


def lower_name(name: str) -> str:
    return name.lower()


def format_number(number: str) -> float:
    number = ''.join([c for c in number if c.isdigit()])
    number = float(number)

    return number
