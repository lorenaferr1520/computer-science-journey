# colours dict
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

# title
print(f'''{colours["green"]}=====================================
       BINARY DECIMAL CONVERTER
====================================={colours["reset"]}''')

# def menu
def menu():
    print('''
[1] DECIMAL => BINARY
[2] BINARY => DECIMAL
[3] EXIT
=====================================
''')
def line():
    print('=====================================')

# def decimal to binary
def decimal_to_binary(number):

    binary_list = list()
    binary_number = ''
    
    if number == 0: # especial case: number 0
        return '0'

    while True: # Number converter
        rest = int(number % 2)
        number = number // 2
        binary_list.append(rest)
    
        if number == 0:
            break
    
    for item in reversed(binary_list):
        binary_number += str(item)
    
    return binary_number

# menu
while True:
    menu()
    try:
        answer = int(input('Answer: '))
    
    except ValueError:
        print('Select a valid answer.')
        continue
    
    if answer == 3:
        break
    
    elif answer == 1:
        try:
            num = int(input("Decimal Number: "))
        except ValueError:
            print("Enter a valid decimal number.")
            continue
        
        print(f'{num} in decimal is {decimal_to_binary(num)}')
        line()

    elif answer == 2:
        try:
            num = int(input("Decimal Number: "))
        except ValueError:
            print("Enter a valid decimal number.")
            continue
        print()
    
    else:
        print('Select a valid answer.')

print(f'''{colours["yellow"]}End 
  __
<(o )___
 ( ._> /
  `---'   quak

{colours["reset"]}''')
