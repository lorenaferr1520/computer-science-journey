# right triangule calculator
import math 
colours = {
    # Reset
    'reset': '\033[m',

    # Cores
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m'
}

def menu():
    print('''
[0] EXIT
[1] HYPOTENUSE
[2] CATHETUS / LEG
[3] AREA
[4] ANGLE
[5] SINE
[6] COSINE
[7] TANGENT
''')

while True:
    menu()
    try:
        answer = int(input("Answer: "))
    except ValueError:
        print(f'{colours["red"]}Select a valid answer.{colours["reset"]}')
        continue
    
    if answer > 7 or answer < 0:
        print(f'{colours["red"]}Select a valid answer.{colours["reset"]}')
        continue
    
    elif answer == 0: # EXIT (break while loop)
        break
    
    elif answer == 1:
        
        try: 
            cat_a = float(input('Cathetus A: '))
            cat_b = float(input('Cathetus B: '))
        except ValueError:
            print(f'{colours["red"]}Enter a valid number.{colours["reset"]}')
            continue
        
        hip = math.sqrt((cat_a**2) + (cat_b**2))

        print(f'The hypotenuse of {cat_a} and {cat_b} is: {hip:.1f}')
    
    elif answer == 2:
        
        try:
            cat_x = float(input('Cathetus x: '))
            hip = float(input('Hypotenuse: '))
        except ValueError:
            print(f'{colours["red"]}Enter a valid number.{colours["reset"]}')
            continue
        
        if hip > 0 and cat_x > 0 and hip > cat_x:
            cat_y = math.sqrt((hip**2) - (cat_x**2))
            
            print(f'The leg corresponding to a hypotenuse of {hip} and a leg of {cat_x} is: {cat_y:.1f}')
        
        else:
            if hip > 0:
                print(f"{colours['red']}The hypotenuse must be greater than 0.{colours['reset']}")
            elif cat_x < 0:
                print(f"{colours['red']}The cathetus must be greater than 0.{colours['reset']}")
            else:
                print(f"{colours['red']}The hypotenuse must be greater than the cathetus.{colours['reset']}")
            
            continue
            
        
