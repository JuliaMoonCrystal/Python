def caixa_eletronico():
    cedulas = [100, 50, 20, 10, 5, 2]

    try:
        valor = int(input("Digite o valor do saque: "))

        if valor <= 0:
            print("Erro: O valor deve ser positivo.")
        elif valor % 2 != 0:
            print("Erro: O valor deve ser múltiplo de 2.")
        else:
            print("Cédulas entregues:")

            for cedula in cedulas:
                quantidade = valor // cedula
                if quantidade > 0:
                    print(f"{quantidade} cédulas de R$ {cedula}")
                    valor = valor % cedula

    except ValueError:
        print("Erro: Digite um valor numérico válido.")


caixa_eletronico()