from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    @abstractmethod
    def _sacar(self, valor): ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPOSITO {valor})')
    
    def sacar(self, valor):
        return self._sacar(valor)
    
    def detalhes(self, msg=''):
        print(f'O seu saldo é R${self.saldo:.2f} {msg}')
        print('--')

class ContaPoupanca(Conta):
    def _sacar(self, valor):
        if valor == self.saldo or valor < self.saldo:
            self.saldo -= valor
            self.detalhes(f'| SAQUE REALIZADO: R${valor}')
            return self.saldo
        
        print('Não foi possivel realizar o saque.')
        self.detalhes(f'| SAQUE NEGADO: R${valor}')
    

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def _sacar(self, valor):
        if valor == self.saldo or valor < self.saldo:
            self.saldo -= valor
            self.detalhes(f'| SAQUE REALIZADO: R${valor} | LIMITE DISPONÍVEL {self.limite}')
            return self.saldo
        if valor > self.saldo:
            if (self.saldo - valor) < -self.limite:
                print('Limite insuficiente para o saque.')
            else:
                self.saldo -= valor
                self.detalhes(f'| SAQUE REALIZADO: R${valor} | LIMITE DISPONÍVEL {self.limite+self.saldo}')
                return self.saldo 
        
        print(f'Não foi possivel realizar o saque. LIMITE DISPONÍVEL {self.limite+self.saldo}')
        self.detalhes(f'| SAQUE NEGADO: R${valor}')

if __name__ == '__main__':
    cp1 = ContaPoupanca('000','001')
    cc1 = ContaCorrente('111', '002', 200 , 100)
    cc1.sacar(98)
    cc1.sacar(2)
    cc1.sacar(150)
    cc1.sacar(5)






