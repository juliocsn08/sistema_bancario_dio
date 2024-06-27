import textwrap

def menu():
    menu_text = """
    =================== MENU ===================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato da Conta
    [4]\tCriar novo Usuário
    [5]\tCriar nova Conta
    [6]\tListar contas
    [0]\tSair

    => """
    return input(textwrap.dedent(menu_text))

def depositar(saldo, valor, extrato):
    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"
    print(f"\n========= Depósito realizado com sucesso! =========\n"
          f"Esse é o novo saldo disponível: {saldo:.2f}\n")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, saques_realizados, limite_saques):
    if valor <= 0:
        print("Operação falhou, valor informado é inválido")
    elif valor > limite:
        print(f"\nOperação falhou! Você ultrapassou o limite de R${limite}")
    elif saques_realizados >= limite_saques:
        print(f"\nOperação falhou! Você excedeu o limite de {limite_saques} saques")
    elif valor > saldo:
        print(f"\nOperação falhou, seu saldo de R${saldo:.2f} não é suficiente para realizar a operação!")
    else:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        saques_realizados += 1
        print(f"\n========= Saque realizado com sucesso! =========\n"
              f"Esse é o novo saldo disponível: {saldo:.2f}\n")
    
    return saldo, extrato, saques_realizados

def exibir_extrato(saldo, extrato):
    print("\n================ Extrato ================")
    if not extrato:
        print("\nNenhuma transação realizada")
    else:
        print(extrato)
    print(f"\nSaldo:\tR$ {saldo:.2f}\n")
    print("=========================================")
    
    
def verificar_cpf(usuarios, novo_cpf):
    for usuario in usuarios:
        if usuario["cpf"] == novo_cpf:
            return True
    return False

def criar_usuario(usuarios,novo_cpf):
    nome=input("Informe seu Nome completo: \t")
    data_nascimento = input("Informe sua data de nascimento\t")
    endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado)")
    usuarios.append({"nome":nome,"cpf": novo_cpf, "data_nascimento":data_nascimento, "endereco":endereco})
    print("\n=== Conta criada com sucesso! ===")
    
def filtrar_usuario(cpf,usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None
    

def criar_conta(agencia,numero_conta, usuarios,contas):
    cpf = input("Informe seu CPF")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        contas.append({"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario})
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("CPF não existe em nosso sistema, por favor, crie um usuário antes de criar sua conta corrente")
        
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" *100)
        print(textwrap.dedent(linha))

def main():
    limite_saques = 3
    limite = 2000
    agencia = "0001"
    saldo = 0
    extrato = ""
    saques_realizados = 0 
    usuarios = []
    contas = []
    
    while True:
        opcao = int(menu())

        if opcao == 0:
            print("Encerrando programa...")
            break
        elif opcao == 1:
            valor = float(input("Qual seria o valor do depósito? "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == 2:
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, saques_realizados = sacar(saldo, valor, extrato, limite, saques_realizados, limite_saques)
        elif opcao == 3:
            exibir_extrato(saldo, extrato)
        elif opcao == 4:
            novo_cpf = input("Informe seu CPF(apenas numeros):")
            verificador = verificar_cpf(usuarios, novo_cpf)
            if verificador:
                print("CPF já existe no sistema")
            else:
                criar_usuario(usuarios,novo_cpf)
        elif opcao == 5:
            numero_conta=len(contas)+1
            criar_conta(agencia,numero_conta, usuarios, contas)
        elif opcao == 6:
            listar_contas (contas)
        elif opcao == 0:
            break
                
        else:
            print("Opção inválida. Por favor, escolha uma opção válida do menu.")

if __name__ == "__main__":
    main()

