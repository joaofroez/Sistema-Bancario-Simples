from contas import ContaPoupanca, ContaCorrente

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None :
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, valor):
        self._idade = valor

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None :
        super().__init__( nome, idade)
        self.contas = []
    
    def criar_conta(self, *contas):
        for conta in contas:
            self.contas.append(conta)
    def dados_contas(self):
        print(f'Contas do Cliente {self.nome}')
        for dados in self.contas:
            if dados.__class__.__name__ == 'ContaPoupanca':
                print(f'Agência: {dados.agencia} Número: {dados.conta} Saldo: R${dados.saldo}')
            else:
                print(f'Agência: {dados.agencia} Número: {dados.conta} Saldo: R${dados.saldo}\
 Limite: {dados.limite}')

cp1 = ContaPoupanca('000', '0', 50)
cc1 = ContaCorrente('001', '0', 542)
cliente1 = Cliente('João', 25)
cliente1.criar_conta(cp1, cc1)
cliente1.dados_contas()
