while True:
    try:
        num1 = int(input('Digite um numero inteiro: '))
        num2 = int(input('Digite o segundo numero inteiro: '))
        num3 = int(input('Digite o terceiro numero inteiro: '))
        
    except ValueError:
        print('Apenas números inteiros!')
    
    if num1 < num2 < num3:
        print('crescente')
    else:
        print('não está em ordem crescente')
        
    break
