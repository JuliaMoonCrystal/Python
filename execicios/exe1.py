valor_conta = float(input("Digite o valor da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta: "))
gorjeta = (porcentagem_gorjeta / 100) * valor_conta
total_a_pagar = valor_conta + gorjeta
print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")