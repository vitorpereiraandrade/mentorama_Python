class ContaCorrente:

    def __init__(self,numero_conta, nome_correntista,saldo=0):
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def deposito(self,valor_deposito):
        self.saldo += valor_deposito
        return self.saldo

    def saque(self,valor_saque):
        self.saldo -= valor_saque
        return self.saldo

conta = ContaCorrente(25789,'Vitor Andrade')

print (f'O saldo do numero da conta {conta.numero_conta}, em nome de {conta.nome_correntista} é : R$ {conta.saldo}')

conta.deposito(100)
print (f'O saldo do numero da conta {conta.numero_conta}, em nome de {conta.nome_correntista} é : R$ {conta.saldo}')

conta.saque(38)
print (f'O saldo do numero da conta {conta.numero_conta}, em nome de {conta.nome_correntista} é : R$ {conta.saldo}')





