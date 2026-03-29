import random

def pedra_papel_tesoura():
    opcoes = ["pedra", "papel", "tesoura"]

    escolha_computador = random.choice(opcoes)
    escolha_usuario = input("Escolha: pedra, papel ou tesoura? ").lower()

    if escolha_usuario not in opcoes:
        print("Escolha inválida! Tente novamente")
        return pedra_papel_tesoura()

    print(f"Computador escolheu: {escolha_computador}")

    if escolha_usuario == escolha_computador:
        print("Empate!")
        return pedra_papel_tesoura()
    elif (
            (escolha_usuario == "pedra" and escolha_computador == "tesoura") or
            (escolha_usuario == "papel" and escolha_computador == "pedra") or
            (escolha_usuario == "tesoura" and escolha_computador == "papel")
    ):
        print("Você venceu!")
    else:
        print("Você perdeu!")

pedra_papel_tesoura()