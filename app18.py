# Cálculo estimado de tempo de um arquivo.
tamanho = float(input("Digite o tamanho do arquivo(MB): "))
velocidade = float(input("Digite a velocidade da internet(mbps): "))

tamanho_bit = tamanho * 8
tempo_seg = tamanho_bit / velocidade
tempo_min = tempo_seg // 60
resto_seg = tempo_seg % 60
tempo_hora = tempo_min // 60
resto_min = tempo_hora % 60
if tempo_seg < 60:
    print(f"O arquivo demorará {tempo_seg} s para terminar o download.")
elif (tempo_seg >= 60) and (tempo_seg < 3600):   
    print(f"O arquivo demorará {tempo_min} min e {resto_seg} s para terminar o download.")
else:
    print(f"O arquivo demorará {tempo_hora}h, {resto_min} min e {resto_seg} s para terminar o download. ")
