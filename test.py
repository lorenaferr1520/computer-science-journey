# cathetus
import math

cat_x = float(input('Cathetus x: '))
hip = float(input('Hypotenuse: '))

cat_y = math.sqrt((hip**2) - (cat_x**2))

print(cat_y)