coca_cola = 50
total = 0

while total < coca_cola:
    moedas_inseridas = int(input("insert coin: "))

    if moedas_inseridas in [5, 10, 25]:
        total += moedas_inseridas
    # Se a moeda for inválida, total não aumenta

    # Sempre imprime quanto falta se total < 50
    if total < coca_cola:
        print(f"Amount Due: {coca_cola - total}")

# Ao final, imprime o troco (0 se não houver)
print("Change owed:", total - coca_cola)





