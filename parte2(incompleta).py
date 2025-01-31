#Falta fazer: review, historico, selecionar cadeira e promoções
cinemas={
    "Centerplex": {
        "Movies":["1-High School Musical","2-De Volta Para O Futuro","3-Elvis"],
        "seat": {"1-High School Musical": ["A1","A2","A3","A4","A5"], "2-De Volta Para O Futuro": ["B1","B2","B3"],"3-Elvis": ["C1","C2","C3","C4"]},
        },
    "Cinesystem":{
        "Movies":["1-High School Musical","2-Mamma Mia","3-Grease"],
        "seat": {"1-High School Musical": ["A1","A2","A3","A4","A5"], "2-Mamma Mia": ["B1","B2","B3","B4","B5"],"3-Grease": ["C1","C2","C3","C4","C5"]},
        },
    "Kinoplex":{
        "Movies":["1-Elvis","2-O Rei Do Show","3-Mamma Mia"],
        "seat": {"1-Elvis": ["A1","A2","A3","A4"], "2-O Rei Do Show": ["B1","B2","B3","B4","B5"],"3-Mamma Mia": ["C1","C2","C3","C4"]},
        }
}

def payment(total_tickets):
    total_value=total_tickets*20.00
    print("Estamos quase lá!!!\nPara realizar o pagamento, faça um pix para essa chave: 82999706005")
    print(f"Valor final: R${total_value}")



def choosing_seat1(chosen):
    print("Assentos disponíveis:")
    if chosen==1:
        for seat in cinemas["Centerplex"]["seat"]["1-High School Musical"]:
            print(seat)
        print("VALOR INGRESSO: R$20.00")
        total_tickets=int(input("Quantos ingressos vai querer? "))
        if total_tickets<1 or total_tickets>5:
            print("A quantidade de ingressos escolhidos extrapola ou é inferior à quantidade de assentos! Por favor escolha novamente.")
            choosing_seat1()
        else:
            payment(total_tickets)
        
    elif chosen==2:
        for seat in cinemas["Centerplex"]["seat"]["2-De Volta Para O Futuro"]:
            print(seat)
        print("VALOR INGRESSO: R$20.00")
        total_tickets=int(input("Quantos ingressos vai querer? "))
        if total_tickets<1 or total_tickets>3:
            print("A quantidade de ingressos escolhidos extrapola ou é inferior à quantidade de assentos! Por favor escolha novamente.")
            choosing_seat1(chosen)
        else:
            payment(total_tickets)

    elif chosen==3:
        for seat in cinemas["Centerplex"]["seat"]["3-Elvis"]:
            print(seat)
        print("VALOR INGRESSO: R$20.00")
        total_tickets=int(input("Quantos ingressos vai querer? "))
        if total_tickets<1 or total_tickets>4:
            print("A quantidade de ingressos escolhidos extrapola ou é inferior à quantidade de assentos! Por favor escolha novamente.")
            choosing_seat1(chosen)
        else:
            payment(total_tickets)
    else:
        print("Opção inválida. Selecione novamente.")
        choosing_seat1(chosen)

    
def choosing_seat2(chosen):
    print("Assentos disponíveis:")
    if chosen==1:
        for seat in cinemas["Cinesystem"]["seat"]["1-High School Musical"]:
            print(seat)
        print("VALOR INGRESSO: R$20.00")
        total_tickets=int(input("Quantos ingressos vai querer? "))
        if total_tickets<1 or total_tickets>5:
            print("A quantidade de ingressos escolhidos extrapola ou é inferior à quantidade de assentos! Por favor escolha novamente.")
            choosing_seat2(chosen)
        else:
            payment(total_tickets)
        
    elif chosen==2:
        for seat in cinemas["Cinesystem"]["seat"]["2-Mamma Mia"]:
            print(seat)
        print("VALOR INGRESSO: R$20.00")
        total_tickets=int(input("Quantos ingressos vai querer? "))
        if total_tickets<1 or total_tickets>5:
            print("A quantidade de ingressos escolhidos extrapola ou é inferior à quantidade de assentos! Por favor escolha novamente.")
            choosing_seat2(chosen)
        else:
            payment(total_tickets)

    elif chosen==3:
        for seat in cinemas["Cinesystem"]["seat"]["3-Grease"]:
            print(seat)
        print("VALOR INGRESSO: R$20.00")
        total_tickets=int(input("Quantos ingressos vai querer? "))
        if total_tickets<1 or total_tickets>5:
            print("A quantidade de ingressos escolhidos extrapola ou é inferior à quantidade de assentos! Por favor escolha novamente.")
            choosing_seat2(chosen)
        else:
            payment(total_tickets)
    else:
        print("Opção inválida. Selecione novamente.")
        choosing_seat2(chosen)

def choosing_seat3(chosen):
    print("Assentos disponíveis:")
    if chosen==1:
        for seat in cinemas["Kinoplex"]["seat"]["1-Elvis"]:
            print(seat)
        print("VALOR INGRESSO: R$20.00")
        total_tickets=int(input("Quantos ingressos vai querer? "))
        if total_tickets<1 or total_tickets>4:
            print("A quantidade de ingressos escolhidos extrapola ou é inferior à quantidade de assentos! Por favor escolha novamente.")
            choosing_seat3(chosen)
        else:
            payment(total_tickets)
        
    elif chosen==2:
        for seat in cinemas["Kinoplex"]["seat"]["2-O Rei Do Show"]:
            print(seat)
        print("VALOR INGRESSO: R$20.00")
        total_tickets=int(input("Quantos ingressos vai querer? "))
        if total_tickets<1 or total_tickets>5:
            print("A quantidade de ingressos escolhidos extrapola ou é inferior à quantidade de assentos! Por favor escolha novamente.")
            choosing_seat3(chosen)
        else:
            payment(total_tickets)

    elif chosen==3:
        for seat in cinemas["Kinoplex"]["seat"]["3-Mamma Mia"]:
            print(seat)
        print("VALOR INGRESSO: R$20.00")
        total_tickets=int(input("Quantos ingressos vai querer? "))
        if total_tickets<1 or total_tickets>4:
            print("A quantidade de ingressos escolhidos extrapola ou é inferior à quantidade de assentos! Por favor escolha novamente.")
            choosing_seat3(chosen)
        else:
            payment(total_tickets)
    else:
        print("Opção inválida. Selecione novamente.")
        choosing_seat3(chosen)



def available_cinemas():
    cinemas_option=int(input("Qual cinema gostaria de ir?\n1-Centerplex\n2-Cinesystem\n3-Kinoplex\n"))
    print("Filmes disponíveis:\n")
    if cinemas_option==1:
        for movie in cinemas["Centerplex"]["Movies"]:
            print(movie)
        chosen=int(input())
        print("Boa esolha!")
        choosing_seat1(chosen)

    elif cinemas_option==2:
        for movie in cinemas["Cinesystem"]["Movies"]:
            print(movie)
        chosen=int(input())
        print("Ótima esolha!")
        choosing_seat2(chosen)

    elif cinemas_option==3:
        for movie in cinemas["Kinoplex"]["Movies"]:
            print(movie)
        chosen=int(input())
        print("Incrível esolha!")
        choosing_seat3(chosen)



account={}
def Creat_account():
    name = input("Digite seu nome: ")
    email = input("Digite seu E-mail: ")
    password = input("Digite sua senha: ")
    if email in account:
        print("Conta já existente.")
        Creat_account()
    else:
        account[email]={"name": name}
        print(f"Usuário {name} criado com sucesso!")
        available_cinemas()


def login():
    email = input("Digite seu E-mail: ")
    password = input("Digite sua senha: ")
    if email in account:
        available_cinemas()
    else:
        print("Essa conta não existe! Por favor crie uma.")
        Creat_account()

def initial_choice ():
    choose= int(input("Digite o número do que deseja fazer:\n1-Login\n2-Criar Conta\n"))
    if choose == 1:
        login()
    elif choose == 2:
        Creat_account()
    else:
        print("Número inválido! Por favor digite novamente.")
        initial_choice()


initial_choice()

