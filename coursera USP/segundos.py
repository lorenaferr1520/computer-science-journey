segundos_totais = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos_totais // 86400
resto_dias = segundos_totais % 86400

horas = resto_dias // 3600
resto_horas = resto_dias % 3600

minutos = resto_horas // 60
segundos = resto_horas % 60

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")