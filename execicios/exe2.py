def validar_cpf(cpf):
    if not cpf.isdigit():
        return "Erro: O CPF deve conter apenas números."
    if len(cpf) != 11:
        return "Erro: O CPF deve ter exatamente 11 dígitos."
    return "CPF válido."


cpf = input("Digite seu CPF: ")
print(validar_cpf(cpf))