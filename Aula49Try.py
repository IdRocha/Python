numero_str = input("Vou dobrar o numero que você digitar: ")

try:
    print('STR', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'O dobro do numero {numero_str} é {numero_float*2}')
except:
    print('Isso não é um número!')