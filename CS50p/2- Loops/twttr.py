vogais = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

texto = str(input(":  "))
resultado = ""

for caractere in texto:
    if caractere not in vogais:
        resultado += caractere

print(resultado)
