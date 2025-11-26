# 7) Sistema Bancário Para registrar uma TransacaoBancaria (como uma transferência), é necessário ter uma Conta de origem e uma Conta de destino. 
# As contas existem independentemente das transações e uma transação simplesmente as utiliza para realizar sua operação. 
# Implemente as classes TransacaoBancaria e Conta, aplicando o relacionamento correto entre elas.

class Conta:
    def __init__(self, numero_conta, titular, saldo=0.0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado na conta {self.numero_conta}.\n")
        else:
            print("Valor de depósito inválido.\n")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado da conta {self.numero_conta}.\n")
        else:
            print("Saldo insuficiente ou valor inválido.\n")

    def __str__(self):
        return f"Conta {self.numero_conta} - Titular: {self.titular} - Saldo: R${self.saldo:.2f}"


class TransacaoBancaria:
    def __init__(self, conta_origem, conta_destino, valor):
        self.conta_origem = conta_origem
        self.conta_destino = conta_destino
        self.valor = valor

    def executar(self):
        if self.valor <= 0:
            print("Valor inválido para transferência.\n")
            return

        if self.conta_origem.saldo >= self.valor:
            self.conta_origem.sacar(self.valor)
            self.conta_destino.depositar(self.valor)
            print(f"Transferência de R${self.valor:.2f} realizada com sucesso.\n")
        else:
            print("Saldo insuficiente para realizar a transferência.\n")


conta1 = Conta(1843, "Vitor", 1500.00)
conta2 = Conta(1238, "José", 893.95)

transacao = TransacaoBancaria(conta1, conta2, 150)
transacao.executar()

print(conta1)
print()
print(conta2)
