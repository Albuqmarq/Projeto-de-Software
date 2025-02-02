
cinemas = {
    "Centerplex": {
        "Movies": ["1-High School Musical", "2-De Volta Para O Futuro", "3-Elvis"],
        "seat": {
            "1-High School Musical": ["A1", "A2", "A3", "A4", "A5"],
            "2-De Volta Para O Futuro": ["B1", "B2", "B3"],
            "3-Elvis": ["C1", "C2", "C3", "C4"]
        }
    },
    "Cinesystem": {
        "Movies": ["1-High School Musical", "2-Mamma Mia", "3-Grease"],
        "seat": {
            "1-High School Musical": ["A1", "A2", "A3", "A4", "A5"],
            "2-Mamma Mia": ["B1", "B2", "B3", "B4", "B5"],
            "3-Grease": ["C1", "C2", "C3", "C4", "C5"]
        }
    },
    "Kinoplex": {
        "Movies": ["1-Elvis", "2-O Rei Do Show", "3-Mamma Mia"],
        "seat": {
            "1-Elvis": ["A1", "A2", "A3", "A4"],
            "2-O Rei Do Show": ["B1", "B2", "B3", "B4", "B5"],
            "3-Mamma Mia": ["C1", "C2", "C3", "C4"]
        }
    }
}

account = {}

def finalizacion(total_tickets):
    while True:
        try:
            last_choice = int(input("O pagamento foi finalizado?\n1-SIM\n2-NÃO\n"))
            if last_choice == 1:
                print("Sua compra foi realizada com sucesso!")
                break
            elif last_choice == 2:
                print("Por favor, volte e finalize o pagamento.")
                payment(total_tickets)
                break
            else:
                print("Opção inválida. Digite 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def payment(total_tickets):
    while True:
        try:
            has_cupom = int(input("Possui cupom?\n1-SIM\n2-NÃO\n"))
            if has_cupom == 1:
                cupom = input("Digite seu cupom: ")
                if cupom == '10CONTO':
                    print("Cupom válido!")
                    total_value = (total_tickets * 20.00) * 0.9
                else:
                    print("Cupom inválido! Tente novamente.")
                    try_again = int(input("Deseja tentar outro cupom?\n1-SIM\n2-NÃO\n"))
                    if try_again == 2:
                        total_value = total_tickets * 20.00
                    break
            elif has_cupom == 2:
                total_value = total_tickets * 20.00
            else:
                print("Opção inválida. Digite 1 ou 2.")
                continue

            print("Estamos quase lá!!!\nPara realizar o pagamento, faça um PIX para essa chave: 82999706005")
            print(f"Valor final: R${total_value:.2f}")
            finalizacion(total_tickets)
            break
        except ValueError:
            print("Entrada inválida. Digite um número.")

def choose_seats(cinema_name, movie_index):
    cinema=cinemas[cinema_name]
    movie_key=cinema["Movies"][movie_index - 1]
    seats=cinema["seat"][movie_key]

    print(f"Assentos disponíveis:")
    for seat in seats:
        print(seat)

    while True:
        try:
            total_tickets=int(input("Quantos ingressos vai querer? "))
            max_seats=len(seats)

            if 1<=total_tickets<=max_seats:
                chosen_seats=[]
                for i in range(total_tickets):
                    while True:
                        seat_choice = input(f"Escolha o assento {i+1}: ").strip().upper()
                        if seat_choice in seats:
                            chosen_seats.append(seat_choice)
                            seats.remove(seat_choice) 
                            break
                        else:
                            print("Assento indisponível ou inválido. Escolha outro.")
                print(f"Assentos escolhidos: {', '.join(chosen_seats)}")
                payment(total_tickets)
                break
            else:
                print(f"A quantidade de ingressos deve ser entre 1 e {max_seats}. Por favor, escolha novamente.")
        except ValueError:
            print("Entrada inválida.")

def available_cinemas():
    print("Não perca a oportunidade! Use o cupom '10CONTO' para ganhar 10% de desconto!!")
    while True:
        try:
            cinemas_option = int(input("Qual cinema gostaria de ir?\n1-Centerplex\n2-Cinesystem\n3-Kinoplex\n"))
            if cinemas_option in [1, 2, 3]:
                cinema_name=list(cinemas.keys())[cinemas_option-1]
                cinema=cinemas[cinema_name]

                print("Filmes disponíveis:")
                for movie in cinema["Movies"]:
                    print(movie)

                while True:
                    try:
                        chosen=int(input("Escolha o filme que deseja ver: "))
                        if 1<=chosen<=len(cinema["Movies"]):
                            print("Boa escolha!")
                            choose_seats(cinema_name, chosen)
                            break
                        else:
                            print("Opção inválida. Tente novamente.")
                    except ValueError:
                        print("Entrada inválida.")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def review():
    movie=input("Digite qual filme deseja avaliar: ")
    review_text=input(f"Digite sua avaliação sobre {movie}:\n")
    while True:
        try:
            rating = int(input("Qual sua nota de 0 a 10:\n"))
            if 0<=rating<=10:
                print("Obrigado pela sua avaliação!\nAgora o que deseja fazer?\n")
                menu()
                break
            else:
                print("Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida.")

def menu():
    while True:
        try:
            choose=int(input("1-Ver cinemas\n2-Avaliar filmes\n"))
            if choose==1:
                available_cinemas()
                break
            elif choose==2:
                review()
                break
            else:
                print("Escolha indisponível. Por favor, escolha novamente.")
        except ValueError:
            print("Entrada inválida.")

def create_account():
    name=input("Digite seu nome: ")
    email=input("Digite seu E-mail: ")
    password=input("Digite sua senha: ")

    if email in account:
        print("Conta já existente.")
        create_account()
    else:
        account[email] = {"name": name, "password": password}
        print(f"Usuário {name} criado com sucesso!")
        menu()

def login():
    email = input("Digite seu E-mail: ")
    password = input("Digite sua senha: ")

    if email in account and account[email]["password"] == password:
        print(f"Bem-vindo, {account[email]['name']}!")
        menu()
    else:
        print("E-mail ou senha incorretos. Tente novamente.")
        initial_choice()

def initial_choice():
    while True:
        try:
            choose = int(input("Digite o número do que deseja fazer:\n1-Login\n2-Criar Conta\n"))
            if choose==1:
                login()
                break
            elif choose==2:
                create_account()
                break
            else:
                print("Número inválido! Por favor, digite novamente.")
        except ValueError:
            print("Entrada inválida.")


initial_choice()
