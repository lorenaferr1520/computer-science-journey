expression = input("expression: ")

x, y, z = expression.split(" ")

new_x = float(x)
new_z = float(z)

if y == "+":
    resultado = new_x + new_z

elif y == "-":
    resultado = new_x - new_z

elif y == "*":
    resultado = new_x * new_z

elif y == "/":
    resultado = new_x / new_z

print(f"{resultado:.1f}")




