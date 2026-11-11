while True:
    try:
        num = int(input('Digite um numero inteiro: '))
    except ValueError:
        print('Apenas números inteiros!')
    
    if num % 5 == 0:
        print('Buzz')
    else:
        print(num)
    
    break
