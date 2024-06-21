menu = """

    [1] - Depositar
    [2] - Sacar
    [3]-  Exibir saldo
    [0] - Sair

=> """


valor_disponivel = float(2500)
limite_saque = 3
quantidade_saque = 0
nome=input("Por favor, me informe seu nome para continuarmos o atendimento: ")


while True:

    acao=int(input(f"Olá {nome}, no que podemos ajudar?{menu}"))

    if acao == 1:
        valor_deposito = float(input("Informe o valor do deposito? "))
        valor_disponivel += valor_deposito
        print (f"Este é o novo valor disponivel: {valor_disponivel:.2f}\n")
    elif acao == 2:
        if quantidade_saque < limite_saque:
            valor_saque = float(input("Qual o valor que deseja sacar? "))
            if valor_saque <= valor_disponivel:
                valor_disponivel -= valor_saque
                print(f"Saque Realizado!! Valor disponível é de:{valor_disponivel:.2f}\n")
                quantidade_saque += 1
            else:
                print(f"Você não possui saldo suficiente para realizar o saque, valor disponível é de {valor_disponivel:.2f}")
        else:
            print(f"Atividade suspeita: limite de {limite_saque} saques atingidos, aguarde até amanhã ou solicite com o suporte o desbloqueio da função para o dia de hoje")
            break
    elif acao ==3:
        print(f"Valor disponível é de {valor_disponivel:.2f}\n")
    elif acao ==0:
        print(f"Estamos a disposição caso necessite, tenha um ótimo dia")
        print("Fechando o programa...")
        break
    else:
        print("Opção inválida, Por favor, escolhe uma opção válida.")