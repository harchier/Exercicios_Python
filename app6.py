# Calcular a area do circulo a partir do raio
from math import pi
raio = float(input("Digite o valor do raio do circulo em cm: "))

area_circulo = pi * (raio**2)

print(f"A area do círculo é {area_circulo} cm^2")