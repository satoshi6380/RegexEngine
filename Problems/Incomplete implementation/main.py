def startswith_capital_counter(names):

    return sum(1 for name in names if str.isupper(name[0]))
