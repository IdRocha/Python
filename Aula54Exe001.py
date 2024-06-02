numero_str = input("Digite um número inteiro: ")

try:
    numero_int = int(numero_str)
    if(numero_int %2 ==0):
        print(f'O número {numero_int} é PAR!!!')
    else:
        print(f'O número {numero_int} é ÍMPAR!!!')
except:
    print("O valor digitado não é um número inteiro.")