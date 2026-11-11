num = int(input("Digite um número: "))

if num > 1 and not any(num % i == 0 for i in range(2, int(num**0.5) + 1)):
    print("primo")
else:
    print("não primo")