# Tangent

while True:
        try:
                cat_o = float(input('Opposite leg: '))
                cat_a = float(input('Adjacent leg: '))

        
        except ValueError:
                print('{colours["red"]}Enter a valid number.{colours["reset"]}')
                continue
                           
        if cat_a <= 0 or cat_o <= 0:
                print("{colours['red']}The cathetus must be greater than 0.{colours['reset']}")
                continue
        
        tan = cat_o / cat_a
        print(f'The tangent is {tan}')
        break
