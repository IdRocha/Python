#Interpolação de Strings
#s = String
# D e d = inteiros
# f = float
# x e X = Hexadecimal 

nome = input("DIgite o nome: ")

preco = float(input("Digite o valor em R$: "))

variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)