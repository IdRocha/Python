primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

if(primeiro_valor > segundo_valor):
    print("O primeiro valor, ", primeiro_valor, "é maior do que o segundo valor, ", segundo_valor)
elif(primeiro_valor == segundo_valor):
    print("Os valores são iguais.")
else:
    print("O segundo valor, ", segundo_valor, "é maior do que o primeiro valor, ", primeiro_valor)