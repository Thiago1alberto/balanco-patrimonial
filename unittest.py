import unittest
from decimal import Decimal
from balanço import Balanço

class TestBalanco(unittest.TestCase):
    def test_valor_total(self):
        # Testa se a função get_valor_total retorna o valor correto para uma entrada específica
        self.assertEqual(Balanço.get_valor_total("Ativo", ["1","2"],"[10,20]"), Decimal("30"))


    def test_calcular_patrimonio_liquido(self):
        # Testa se a função calcula_patrimonio_liquido retorna o valor correto
        ativos = Decimal("100")
        passivos = Decimal("50")
        self.assertEqual(Balanço.calcula_patrimonio_liquido(ativos, passivos), Decimal("50"))


    def test_calcular_resultado_exercicio(self):
        # Testa se a função calcula_resultado_exercicio retorna o valor correto
        receitas = Decimal("500")
        despesas = Decimal("400")
        self.assertEqual(Balanço.calcula_resultado_exercicio(receitas, despesas), Decimal("100"))


if __name__ == '__main__':
    unittest.main()
