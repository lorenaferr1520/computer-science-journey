# binary to decimal 

binary = '101101'
decimal = 0


binary = binary[::-1]
for i, digit in enumerate(binary):
    if digit == "1":
        decimal += 2**i

print(decimal)