from decimal import Decimal, InvalidOperation

def get_valor_total(nome_categoria):
    valor_total = Decimal('0')
    while True:
        try:
            valor = Decimal(input(f"Insira o valor da {nome_categoria}: "))
        except InvalidOperation:
            print("Valor inválido. Tente novamente.\n")
            continue
        valor_total += valor
        print("\n\033[32mInserido com sucesso!\033[0m\n")
        mais_valores = input(f"Deseja inserir outro valor de {nome_categoria}?\n1: SIM\n2: NÃO\n> ")
        if mais_valores.lower() == "1":
            print(f"\nValores atuais de {nome_categoria}: {valor_total}\n")
        elif mais_valores.lower() == "2":
            print(f"\n{nome_categoria.title()} totais: {valor_total}\n")
            return valor_total
        else:
            print("Resposta inválida. Tente novamente.\n")

ativos = get_valor_total("Ativo")
passivos = get_valor_total("Passivo")
patrimonio_liquido = get_valor_total("patrimonio liquido")


patrimonio_liquido

print("\nBalanço Patrimonial")
print(f"Ativos: R$ {ativos:.2f}")
print(f"Passivos: R$ {passivos:.2f}")
print(f"Patrimônio Líquido: R$ {patrimonio_liquido:.2f}")

