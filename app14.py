# Controle rendimento peixe

peso = float(input("Digite o peso de peixe em kg: "))
excesso = peso - 50

if excesso > 0:
    multa = 4 * excesso
    print(f"O valor da multa é {multa} R$.")
else:
    print(f"Não há multa a ser paga.")