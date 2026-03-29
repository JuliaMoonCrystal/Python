def somar(num1, num2):
    return num1 + num2


def subtrair(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError
    return num1 / num2


def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Escolha a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        if operacao == "+":
            resultado = somar(num1, num2)
        elif operacao == "-":
            resultado = subtrair(num1, num2)
        elif operacao == "*":
            resultado = multiplicar(num1, num2)
        elif operacao == "/":
            resultado = dividir(num1, num2)
        else:
            print("Operação inválida!")
            return

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")


calculadora()