from contas import ContaPoupanca, ContaCorrente
from pessoa import Cliente

class Banco:
    def __init__(
        self,
        agencias=None,
        clientes=None,
        contas=None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
    
    
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False
    
    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False
    
    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False
    
    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta in cliente.contas:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False
    
    def autenticar(self, cliente, conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'
    
if __name__ == '__main__':     
    cliente1 = Cliente('João', 20)
    cliente2 = Cliente('Jenilson', 35)
    cp1 = ContaPoupanca('000','0', 10)
    cp2 = ContaPoupanca('001','0', 50)
    cp3 = ContaPoupanca('002','0', 40)
    cc1 = ContaCorrente('000','1', 100)
    cliente1.criar_conta(cp1, cp2)
    cliente2.criar_conta(cp3, cc1)
    banco = Banco()
    banco.agencias.extend([cp1.agencia, cp2.agencia, cp3.agencia, cc1.agencia])
    banco.clientes.extend([cliente1,cliente2])
    banco.contas.extend([cp1, cp2, cp3, cc1])

    if banco.autenticar(cliente1, cp1):
        cp1.sacar(10)
        cliente1.dados_contas()