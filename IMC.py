nome = "Idelcio"
altura = 1.79
peso = 7

imc = (peso)/(altura**2)

print("{}".format(imc))
if(imc<=18.4):
    print('"Abaixo do peso"')
elif(imc>=18.5 and imc<=24.9):
    print("Peso ideal")
elif(imc>=25 and imc<=29.9):
    print("Acima do peso")
elif(imc>=30 and imc<=34.9):
    print("Obesidade grau 1")
elif(imc>=35 and imc <=39.9):
    print("Obesidade severa")
else:
    print("Obesidade mórbida")