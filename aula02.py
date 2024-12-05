


#EX1

class Conta_bancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo_inicial = saldo_inicial  
    
    def informacoes(self):
        print("Conta: Sr/Sra {}, seu saldo atual é de R${}".format(self.titular, self.saldo_inicial))

    def depositar(self, valor):  
        if valor > 0:  # Verifica se o valor é positivo
            self.saldo_inicial += valor
            print(f"Você depositou R${valor}. Seu saldo atual é de R${self.saldo_inicial}.")
        else:
            print("Valor inválido para depósito.")
    
    def sacar(self, valor):  
        if valor > self.saldo_inicial:  # Verifica se o valor do saque é maior que o saldo
            print("Impossível sacar esse valor pois o saldo é insuficiente.")
        elif valor > 0:
            self.saldo_inicial -= valor
            print(f"Saque de R${valor} realizado com sucesso. Seu saldo atual é de R${self.saldo_inicial}.")
        else:
            print("Valor inválido para saque.")

# Criando objetos da classe Conta_bancaria
conta1 = Conta_bancaria("Joaquin", 200)
conta2 = Conta_bancaria("Juliana", 0)

# Interagindo com os objetos
conta1.informacoes()
conta1.depositar(90)
conta1.sacar(280)

conta2.informacoes()
conta2.depositar(50)
conta2.sacar(60)
conta2.sacar(50)

