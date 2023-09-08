# Cálculo de salário
salario_hora = float(input("Digite o quanto você ganha por hora: "))
horas_dia = float(input("Digite quantas horas você trabalha por dia:"))
dias_trabalhados = int(input("Digite quantos dias você trabalhou no mês:"))

salario_bruto = salario_hora * horas_dia * dias_trabalhados

imposto_renda = salario_bruto * 0.11

#a) Salario Bruto

print(f"O salario bruto é igual a R$ {salario_bruto:.2f}")

inss = salario_bruto * 0.08

#b) Quanto pagou ao INSS

print(f"Você pagou R$ {inss:.2f} ao INSS")

#c) Quanto pagou ao sindicato

sindicato = salario_bruto * 0.05

print(f"Você pagou R$ {sindicato:.2f} ao sindicato")

#d) O salario líquido

salario_liquido = (salario_bruto - imposto_renda) - inss - sindicato

#print(f"O salario liquido é de R$ {salario_liquido}")
print("----------------------------------")
print(f"+Salario bruto: R$ {salario_bruto:.2f}\n-IR (11%): R$ {imposto_renda:.2f}\n-INSS (8%): R$ {inss:.2f}\n-Sindicato (5%): R$ {sindicato:.2f}\n=Salario líquido: R$ {salario_liquido:.2f}")