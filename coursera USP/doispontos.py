# dois pontos
from math import sqrt

numx1 = int(input('X do primeiro: '))
numy1 = int(input('Y do primeiro: '))

numx2 = int(input('X do segundo: '))
numy2 = int(input('Y do segundo: '))

if sqrt(((numx2 - numx1)**2) - ((numy2 - numy1)**2)) > 10:
    print('longe')
else:
    print('perto')

