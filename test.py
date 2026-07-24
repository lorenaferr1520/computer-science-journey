# Angle
import math

while True: # input with validation
    try:
        cat_o = float(input('Opposite leg: '))
        cat_a = float(input('Adjacent leg: '))
    
    except ValueError:
            print('{colours["red"]}Enter a valid number.{colours["reset"]}')
            continue
    
    if cat_o <= 0 or cat_a <= 0:
            print("{colours['red']}The cathetus must be greater than 0.{colours['reset']}")
            continue
    
    rad_angle = math.atan(cat_o / cat_a)
    deg_angle = math.degrees(rad_angle)
    
    print(f'The angle is: {deg_angle:.1f}°')
    break