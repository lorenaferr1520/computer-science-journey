# title
print('''=====================================
       BINARY DECIMAL CONVERTER
=====================================''')
# colours (dict)
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

# def menu
def menu():
    print('''
[1] DECIMAL => BINARY
[2] BINARY => DECIMAL
[3] EXIT
=====================================
''')

# menu
while True:
    menu()
    answer = int(input('Answer: '))