def desconto(num, por):
    return num * (por / 100)

 
    
print('Bem-Vindo a Loja da Lorena Ferreira')
valor_produto = float(input('Entre com o valor do produto: '))
quantidade = int(input('Entre com a quantidade do produto: '))
valor_total = valor_produto * quantidade

if valor_total < 2500:
    # desconto de 0%
    valor_com_desco = valor_total

elif 2500 <= valor_total < 6000:
    # desconto 4%
    valor_com_desco = valor_total - desconto(valor_total, 4)

elif 6000 <= valor_total < 10000:
    # desconto 7%
    valor_com_desco = valor_total - desconto(valor_total, 7)

else:
    # desconto de 11%
    valor_com_desco = valor_total - desconto(valor_total, 11)

print(f'''O valor SEM desconto: R${valor_total:.2f}
O valor COM desconto: R${valor_com_desco:.2f}''')
    
    