usuario = str(input("Insira seu nome de usuário: "))
senha = str(input("Insira sua senha: "))
while usuario==senha:
    print("ERRO (o nome de usuário não pode ser igual a senha)")
    usuario = str(input("Insira seu nome de usuário: "))
    senha = str(input("Insira sua senha: "))
print("Dados salvos")
