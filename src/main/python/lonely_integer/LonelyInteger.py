def lonelyinteger(a):
    set_from_input = set(a)
    return sum(set_from_input) * 2 - sum(a)
