n = int(input('Informe o valor final: '))
soma = 0
cont = 0
for c in range(1, n+1, 2):
    if c %3 ==0:
        soma = soma+c
        cont = cont+1
print('A soma dos {} valores é {} '.format(cont,soma))
