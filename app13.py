# Cálculo do peso ideal (homem e mulher)

altura = float(input("Digite sua altura em metros: "))
sexo = str(input("Digite seu sexo(m/f):"))
sexo = sexo.strip()

if sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é {peso_ideal}")
elif sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {peso_ideal}")
else:
    print("Você digitou o valor de sexo de forma incorreta \nDigite m ou f ")