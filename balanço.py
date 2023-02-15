
def get_valor_total(nome_categoria):
    valor_total = 0
    while True:
        valor = float(input(f"Insira o valor da {nome_categoria}: "))
        valor_total += valor
        mais_valores = input(f"Deseja inserir outro valor de {nome_categoria}? \n1:SIM\n2:NÃO ")
        if mais_valores.lower() == "1":
            print("Valores atuais:")
            print(f"{nome_categoria}: {valor_total}")
        elif mais_valores.lower() == "2":
            print(f"{nome_categoria} totais: {valor_total}")
            return valor_total
        else:
            print("Resposta inválida. Tente novamente.")

ativos = get_valor_total("Ativo")
passivos = get_valor_total("Passivo")
receitas = get_valor_total("Receita")
despesas = get_valor_total("Despesa")

patrimonio_liquido = ativos - passivos
resultado = receitas - despesas

print("\nBalanço Patrimonial")
print("Ativos: R$", ativos)
print("Passivos: R$", passivos)
print("Patrimônio Líquido: R$", patrimonio_liquido)
print("Resultado do Exercício")

if resultado > 0:
    print("Lucro: R$", resultado)
else:
    print("Prejuízo: R$", resultado)
