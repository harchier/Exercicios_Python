# Salario total mensal

valor_hora = float(input("Quanto você ganha por hora(R$)?"))
num_horas = int(input("Quantas horas você trabalha por dia?"))
dias_trab = int(input("Quantos dias você trabalhou esse mês?"))

salario = valor_hora * num_horas * dias_trab

print(f"O seu salario esse mês será de {salario} R$")