class BombaCombustivel:
    def __init__(self, tipo_combustivel:str, valor_litro:float, quantidade_combustivel:float):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor:float):
        litros_abastecidos = valor / self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos
        print(f'O valor abastecido foi de R$ {valor:.2f}, a quantidade foi de {litros_abastecidos:.2f} litros')
        print(f'Sobrou na bomba {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel}')

    def abastecer_por_litros(self, litros_abastecidos:float):
        valor = litros_abastecidos * self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos
        print(f'O valor abastecido foi de R$ {valor:.2f}, a quantidade foi de {litros_abastecidos:.2f} litros')
        print(f'Sobrou na bomba {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel}')

    def alterar_valor_combustivel(self, novo_valor):
        self.valor_litro = novo_valor
        return novo_valor


    def quantidade_combustivel(self):
        return




bomba = BombaCombustivel('gasolina', 5.50, 200.00)
bomba.abastecer_por_valor(float(input('Informe o valor para abastecer: R$ ')))
print('')
bomba.abastecer_por_litros(float(input('Informe a quantidade de litros para abastacer: ')))
print('')
bomba.alterar_valor_combustivel(float(input('Informe o novo valor do combustivel: R$ ')))
print('')
bomba.abastecer_por_litros(float(input('Quantidade de litros que gostaria de abastecer: ')))











