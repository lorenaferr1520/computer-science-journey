def maximo(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c