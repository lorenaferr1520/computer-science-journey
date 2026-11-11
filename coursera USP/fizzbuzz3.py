while True:
    try:
        num = int(input('Digite um numero inteiro: '))
    except ValueError:
        print('Apenas números inteiros!')
    
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    else:
        print(num)
    
    break
