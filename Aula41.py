entrada = input("[E]ntrar ou [S]air: ")
senha_digitada = input("Digite a senha: ")
senha_permitida = '123456'

if((entrada == 'E'or 'e') and senha_digitada == senha_permitida):
    print("Entrar")
elif(entrada == 'S' or 's'):
    print("Sair")
else:
    print("Opção invalida")