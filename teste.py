

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def exibir(self):
        # Verifica se o dia é válido (1 a 31)
        if self.dia < 1 or self.dia > 31:
            print("Digite um valor para dia válido (1 a 31)") 
        # Verifica se o mês é válido (1 a 12)
        elif self.mes < 1 or self.mes > 12:
            print("Digite um valor para mês válido (1 a 12)")
        # Verifica se o ano é válido (deve ter 4 dígitos)
        elif self.ano <= 0 or len(str(self.ano)) != 4:
            print("Digite um valor para ano válido (4 dígitos)")
        else:
            print("A data inserida foi {}/{}/{}".format(self.dia, self.mes, self.ano))

# Testando com diferentes valores
data1 = Data(0, 10, 2020)
data2 = Data(10, 0, 2020)
data3 = Data(10, 10, 0)
data4 = Data(10, 10, 2020)

data1.exibir()  # Dia inválido
data2.exibir()  # Mês inválido
data3.exibir()  # Ano inválido
data4.exibir()  # Data válida
