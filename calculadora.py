def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b


def divisao_inteira(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a // b


def resto(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a % b


def potencia(a, b):
    return a**b


OPERACOES = {
    "1": ("Soma (+)", soma),
    "2": ("Subtracao (-)", subtracao),
    "3": ("Multiplicacao (*)", multiplicacao),
    "4": ("Divisao (/)", divisao),
    "5": ("Divisão inteira (//)", divisao_inteira),
    "6": ("Resto da divisão (%)", resto),
    "7": ("Potência (**)", potencia),
}


def menu():
    print("\n--- Calculadora ---")
    for key, (nome, _) in OPERACOES.items():
        print(f"  {key}. {nome}")
    print("  0. Sair")


def ler_numero(prompt):
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Digite um número válido.")


def main():
    print("Calculadora simples - escolha a operacao e dois numeros.")
    while True:
        menu()
        opcao = input("Opção: ").strip()
        if opcao == "0":
            print("Até logo!")
            break
        if opcao not in OPERACOES:
            print("Opção inválida.")
            continue
        nome, func = OPERACOES[opcao]
        a = ler_numero("Primeiro número: ")
        b = ler_numero("Segundo número: ")
        try:
            resultado = func(a, b)
            print(f"\n{nome}: {a} e {b} -> {resultado}")
        except ValueError as e:
            print(f"\nErro: {e}")


if __name__ == "__main__":
    main()
