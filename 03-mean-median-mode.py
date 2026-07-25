# Mean, Median and Mode
colours = {
    # Reset
    'reset': '\033[m',
    # Cores
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    # Estilos
    'bold': '\033[1m',
    'underline': '\033[4m',
    'reverse': '\033[7m'
}

objects = []
summation = 0
answer = 4

def showobjects(numbers: list):
        return ("-".join(map(str, numbers)))

# menu
while True:
    try:
        answer = int(input('''=========================
[1] Mean
[2] Median
[3] Mode

[0] Exit
=========================
answer: '''))
    
    except ValueError:
        print(f'{colours["red"]}Enter a valid option.{colours["reset"]}')
        continue
    
    if answer > 3 or answer < 0:
        print(f'{colours["red"]}Enter a valid option.{colours["reset"]}')
        continue
    elif answer == 0: # Exit
        break    
    else:
        while True:
            number = float(input('Number: '))
            objects.append(number)
            
            if len(objects) <= 1:
                continue
            else:
                while True:
                    add = float(input('''=========================
Add more numbers?
[1] YES
[2] NO
=========================
answer: '''))
                    if add < 1 or add > 2 :
                        print(f'{colours["red"]}Enter a valid option.{colours["reset"]}')
                    else: 
                        break

            if add == 1:
                continue
            else:
                break
             
    if answer == 1: # Mean
        for i in objects:
            summation += i
            Mean = summation / len(objects)
        
        print(f'the average of {showobjects(objects)} is {summation:.1f}')
    
    elif answer == 2:
        print()


print('''End 
  __
<(o )___
 ( ._> /
  `---'   quak

      ''')