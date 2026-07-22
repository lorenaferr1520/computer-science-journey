# decimal to binary

number = 35 # 100011
binary_list = list()
binary_number = ''

while True:
    rest = int(number % 2)
    
    number = number // 2
    
    binary_list.append(rest)
    print(binary_list)
    
    if number == 0:
        break
    
for item in reversed(binary_list):
    print(item)
    binary_number += str(item)

print(binary_number)
print('End')