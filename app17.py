# Quantidade de tinta a ser comprada
import math

area = float(input("Digite a area a ser pintada em m^2 : "))
litros = area / 6
print(f"Você precisará de {litros} L de tinta.")
if litros <= 3.6:
    print("Você precisará de um galão.\nO valor é de 25 reais.")
elif (litros > 3.6) and (litros <= 7.2):
    print("Você precisará de dois galões.\nO valor é de 50 reais")
elif (litros >  7.2) and (litros <= 10.8):
    print("Você precisa de três galões.\nO valor é de 75 reais")
elif (litros > 10.8) and (litros <= 18):
    print("Você precisa de uma lata de tinta.\nO valor é 80 reais") 
else:
    n_latas = litros // 18
    resto = litros % 18
    n_galoes = resto / 3.6
    n_galoes = math.ceil(n_galoes) 
    t_litros = (n_latas * 18) + (n_galoes * 3.6)
    sobra = t_litros - litros
    folga = litros * 0.1
    if sobra < (folga):
        n_galoes = (n_galoes + 1)
    custo_t = (n_latas * 80) + (n_galoes * 25)
    print(f"Sobrará {sobra:.2f} L.")
    print(f"Você pecisará de {n_latas} latas e {n_galoes} galões.\nO custo total ficará de R${custo_t}")
    
    