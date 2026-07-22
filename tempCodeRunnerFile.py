
# def decimal to binary
def decimal_to_binary(number):

    binary_list = list()
    binary_number = ''
    
    if number == 0: # especial case: number 0
        return '0'

    while True: # number conventer
        rest = int(number % 2)
        number = number // 2
        binary_list.append(rest)
    
        if number == 0:
            break
    
    for item in reversed(binary_list):
        binary_number += str(item)
    
    return binary_number
