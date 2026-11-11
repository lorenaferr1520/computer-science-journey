def ePrimo(k):
    if k < 2:
        return False
    i = 2
    while i * i <= k:
        if k % i == 0:
            return False
        i += 1
    return True

def maior_primo(n):
    for k in range(n, 1, -1):
        if ePrimo(k):
            return k