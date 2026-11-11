texto = input("Digite um número inteiro: ")

tem_adjacente = False
i = 0

while i < len(texto) - 1:
    if texto[i] == texto[i + 1]:
        tem_adjacente = True
        break
    i += 1

if tem_adjacente:
    print("sim")
else:
    print("não")