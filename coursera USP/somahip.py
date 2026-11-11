def e_hipotenusa(h):
  i = 1
  while i < h:
    j = 1
    while j < h:
      if h**2 == i**2 + j**2:
        return True
      j += 1
    i += 1
  return False


def soma_hipotenusas(n):
  soma = 0
  h = 1
  while h <= n:
    if e_hipotenusa(h):
      soma += h
    h += 1
  return soma