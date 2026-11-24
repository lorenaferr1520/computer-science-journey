camelCase = input("digite o seu nome em camelCase:  ")
resultado = ""

for i, letra in enumerate(camelCase):
    if letra.isupper() and i != 0:
            resultado = resultado + "_" + letra.lower()
    else:
        resultado = resultado + letra

resultado = resultado.lower()

print(resultado)

