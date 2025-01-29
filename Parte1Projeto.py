conta={}

def usuario_novo():
    nome=input('Digite seu nome: ')
    cpf=int(input("Digite seu CPF: "))
    if cpf in conta:
        print("CPF já cadastrado")
    else:
        conta[cpf]={'nome': nome}
        print(f'seja bem-vindo, {nome}')

def conta_existente():
    cpf= input('Digite seu CPF: ')
    if cpf in conta:
        print(f'Seja bem-vindo de volta, {conta[cpf][nome]}!')
        return cpf
    else:
        print("Usuário não cadastrado.")
        return None



escolha=int(input('Escolha qual opção deseja fazer:\n1-Criar conta\n2-Login\n3-Crítica\n'))


if escolha == 1:
    usuario_novo() 
elif escolha==2:

    conta_existente()
elif escolha==3:
    input("Filme: ")
    input("Crítica sobre o filme: ")
    print('Obrigado pela sua crítica!')
