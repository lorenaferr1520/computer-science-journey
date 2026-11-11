
while True:
    try:
        num = int(input('Digite um numero inteiro: '))
    except ValueError:
        print('Apenas números inteiros!')
    
    if num % 2 == 0:
        print('par')
    else:
        print('impar')
    
    break
