while True:
    try:
        num = int(input('Digite um numero inteiro: '))
    except ValueError:
        print('Apenas números inteiros!')
    
    if num % 3 == 0:
        print('Fizz')
    else:
        print(num)
    
    break
