def number_of_frogs(year):
    return 2 * (number_of_frogs(year - 1) - 50) if year > 1 else 120
