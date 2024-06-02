
nome = input('Digite o nome: ')
tamanho = len(nome)

i = 0
nova_str =''

while i < len(nome):
    letra = nome[i]
    nova_str += f'*{letra}'
    i += 1
nova_str += '*'
print(nova_str)

