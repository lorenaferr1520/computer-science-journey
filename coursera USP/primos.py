def e_primo(k):
  if k < 2:
    return False
  f = 2
  while f * f <= k:
    if k % f == 0:
      return False
    f += 1
  return True


def n_primos(n):
  contador = 0
  i = 2
  while i <= n:
    if e_primo(i):
      contador += 1
    i += 1
  return contador