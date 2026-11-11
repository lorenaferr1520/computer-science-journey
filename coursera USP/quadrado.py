lado = float(input("Digite o valor correspondente ao lado de um quadrado: "))

perimetro = lado * 4
area = lado ** 2

if perimetro.is_integer():
    perimetro = int(perimetro)
if area.is_integer():
    area = int(area)

print(f"perímetro: {perimetro} - área: {area}")