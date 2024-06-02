nome = input("Digite seu nome: ")
tamanho_nome = len(nome)

if tamanho_nome >1:
    if tamanho_nome <=4:
        print(f'O nome {nome} é curto')
    elif tamanho_nome >=5 and tamanho_nome <=6:
        print(f'O nome {nome} é médio')
    else:
        print(f'O nome {nome} é longo')
else:
    print('Tamanho inválido')   