palavra = input('Digite uma palavra:  ')
inversa = palavra[::-1]

if palavra == inversa:
    print(f'A palavra {palavra} é um Palindromo.')
else:
    print(f'A palavra {palavra} não é um palindromo.')
