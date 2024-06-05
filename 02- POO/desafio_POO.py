from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
            self.endereco = endereco
            self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
         self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Conta:
    def __init__(self, cliente, saldo, nro, agencia, histotico):
        super().__init__(cliente)
        self.saldo = saldo
        self.nro = nro
        self.agencia = agencia
        self.histotico = histotico

    def saldo(self):
         return self.saldo
    
    def nova_conta(self, cliente: Cliente, numero: int):
         return self.Conta()
    
    
