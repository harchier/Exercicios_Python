# Quantidade de latas de tinta
import math
comprimento = (float(input("Digite o valor do comprimento da parede em m: ")))
altura = float(input("Digite o valor da altura da parede em m: "))

area = comprimento * altura

n_lata = area / 54
n_lata = math.ceil(n_lata)
valor = n_lata * 80
print(f"O numero de latas que será utilizado é {n_lata}\nO valor total será de {valor:.2f}" )
