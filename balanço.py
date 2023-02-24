from decimal import Decimal, InvalidOperation

class BalancoPatrimonial:
    CATEGORIA_ATIVO = "ativo"
    CATEGORIA_PASSIVO = "passivo"
    CATEGORIA_PATRIMONIO_LIQUIDO = "patrimônio líquido"

    def __init__(self):
        self.ativos = Decimal('0')
        self.passivos = Decimal('0')
        self.patrimonio_liquido = Decimal('0')
        self.descricoes = {'ativos': [], 'passivos': [], 'patrimonio_liquido': []}
        
    def get_valor_total(self, nome_categoria):
        itens = []
        valor_total = Decimal('0')
        while True:
            descricao = input(f"Insira a descrição do item de {nome_categoria}: ")
            valor_str = input(f"Insira o valor do item de {nome_categoria} '{descricao}': ")
            try:
                valor = Decimal(valor_str)
            except InvalidOperation:
                print("Valor inválido. Tente novamente.\n")
                continue

            itens.append((descricao, valor))
            valor_total += valor
            print(f"\n{descricao} adicionado com sucesso!\n")
            
            mais_itens = input(f"Deseja inserir outro item de {nome_categoria}?\n1: SIM\n2: NÃO\n> ")
            if mais_itens.lower() == "1":
                continue
            elif mais_itens.lower() == "2":
                print(f"\n{nome_categoria.title()} totais: {valor_total}\n")
                if nome_categoria.lower() == "ativo":
                    self.ativos = valor_total
                elif nome_categoria.lower() == "passivo":
                    self.passivos = valor_total
                elif nome_categoria.lower() == "patrimônio líquido":
                    self.patrimonio_liquido = valor_total
                return itens, valor_total
            else:
                print("Resposta inválida. Tente novamente.\n")
            
    def calcular_balanco(self):
        if self.ativos == self.passivos + self.patrimonio_liquido:
            print("O balanço bateu! Ativo = Passivo + Patrimônio Líquido")
        else:
            print("O balanço não bateu! Verifique seus valores.")
        
        print("\nBalanço Patrimonial")
        print(f"Ativos: R$ {self.ativos:.2f}")
        print(f"Passivos: R$ {self.passivos:.2f}")
        print(f"Patrimônio Líquido: R$ {self.patrimonio_liquido:.2f}")
        
        grau_endividamento = self.passivos / self.patrimonio_liquido
        print(f"Grau de endividamento: {grau_endividamento:.2f}")

bp = BalancoPatrimonial()
bp.get_valor_total("Ativo")
bp.get_valor_total("Passivo")
bp.get_valor_total("Patrimônio Líquido")
bp.calcular_balanco()