
#1. Criar uma classe Carro
   #- Crie uma classe chamada Carro com atributos como modelo, cor, ano. Adicione métodos para exibir as informações sobre o carro e um método para acelerar.

class Carro:
    def __init__(self, modelo,cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.velocidade = 0 

    def mostra_informacoes(self):
        print("Carro: {} {} {} - Velocidade: {}Km/h".format(self.cor, self.modelo, self.ano, self.velocidade))

    def acelerar(self, i):
        self.velocidade += i 
        print("Você acelerou. A velocidade atual é {}Km/h".format(self.velocidade))

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print("Você freou. A velocidade atual é {}Km/h".format(self.velocidade))
        else:
            print("O carro já está parado")

# Criando objetos da classe Carro
carro1 = Carro("Gol","prata", 2020)
carro2 = Carro( "C4","preto", 2015)

# Interagindo com os objetos
carro1.mostra_informacoes()
carro1.acelerar(90)
carro1.frear()

carro2.mostra_informacoes()
carro2.acelerar(50)
carro2.frear()


#2. Classe Livro
   #- Crie uma classe  Livro  com atributos título, autor e ano publicação. Adicione um método para exibir as informações do livro e outro para verificar se o livro foi publicado após 2000.

class Livro:
    def __init__(self, titulo, autor, ano_publi):
        self.titulo = titulo
        self.autor = autor
        self.ano_publi= 0

    def mostra_livro(self):
        print("Livro: {} {} {} ".format(self.titulo, self.autor, self.ano_publi))

    def ver_ano_publi(self):
        if self.ano_publi > 2000:
            print("O livro {} foi publicado após os anos 2000".format(self.titulo))
        else:
            print("O livro {} foi publicado antes os anos 2000".format(self.titulo))
        
# Criando objetos da classe Carro
livro1 = Livro("A historia de","Jorgem humor", 2020)
livro2 = Livro("Como fazer um livro", "elizabet go", 1980)

# Interagindo com os objetos
livro1.mostra_livro()
livro2.mostra_livro()

livro1.ver_ano_publi()
livro2.ver_ano_publi()

#3. Classe Pessoa
   #- Crie uma classe  Pessoa  com atributos como nome, idade e email. Adicione métodos para exibir as informações da pessoa e verificar se a pessoa é maior de idade.

class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def mostra_pessoa(self):
        print("Pessoa: {} {} {} ".format(self.nome, self.idade, self.email))

    def ver_ano_nasc(self):
        if self.idade >=18 :
            print("{} já é maior de idade".format(self.nome))
        else:
            print("{} é menor de idade".format(self.nome))
        
# Criando objetos da classe Carro
pessoa1 = Pessoa("Jorge luiz",37,"jorginho@email.com")
pessoa2 = Pessoa("Roberto magalhes", 17, "reberto@emial.com")

# Interagindo com os objetos
pessoa1.mostra_pessoa()
pessoa2.mostra_pessoa()

pessoa1.ver_ano_nasc()
pessoa2.ver_ano_nasc()

#4. Conta Bancária
   #- Crie uma classe ContaBancaria que tenha métodos como depositar, sacar e consultar saldo. Crie um método para verificar se o saldo da conta é negativo.

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

#5. Calculadora
   #- Crie uma classe Calculadora com métodos para as operações básicas: somar, subtrair, multiplicar e dividir.

class Calculadora:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def soma(self):
        self.x = int(input("Digite o 1° valor: "))
        self.y = int(input("Digite o 2° valor: "))
        soma = self.x + self.y
        return soma

    def subtracao(self):
        self.x = int(input("Digite o 1° valor: "))
        self.y = int(input("Digite o 2° valor: "))
        sub = self.x - self.y
        return sub

    def multiplicacao(self):
        self.x = int(input("Digite o 1° valor: "))
        self.y = int(input("Digite o 2° valor: "))
        mult = self.x * self.y
        return mult

    def divisao(self):
        self.x = int(input("Digite o 1° valor: "))
        self.y = int(input("Digite o 2° valor: "))
        if self.y == 0:
            return "Erro: Divisão por zero!"
        div = self.x / self.y
        return div


calc1 = Calculadora(0, 0)


resultado_soma = calc1.soma()
print(f"O resultado da soma é: {resultado_soma}")

#6. Classe Funcionários 
   #- Crie uma classe  Funcionário  com atributos como nome, cargo, salario. Adicione métodos para aumentar o salário e exibir as informações do funcionário.

class Funcionario:
    def __init__(self,nome,cargo,salario):
        self.nome= nome
        self.cargo= cargo
        self.salario= salario
    
    def exibir(self):
        print("O funcionario {} do cargo: {} recebe {}R$".format(self.nome,self.cargo,self.salario))

    def aumento(self,i):
        self.salario += i
        print("O funcionario {} recebeu um aumento para {}R$".format(self.nome, self.salario))


funcio1= Funcionario("Jorge", " operador de máquinas", 1200)
funcio2= Funcionario("Raquel", "Supervisora", 2000)

funcio1.exibir()
funcio1.aumento(200)
funcio1.exibir()

#7. Classe Aluno
   #- Crie uma classe Aluno com atributos nome, matrícula, notas (lista de notas). Adicione métodos para calcular a média das notas e verificar se o aluno foi aprovado.

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def exibir(self):
        # Calculando a média dentro do método exibir
        if len(self.notas) > 0:
            media = sum(self.notas) / len(self.notas)
            print("O aluno {} matrícula N°: {} tem média: {:.2f}".format(self.nome, self.matricula, media))
        else:
            print("O aluno {} matrícula N°: {} ainda não possui notas lançadas.".format(self.nome, self.matricula))

    def lancar_notas(self):
        num_notas = int(input("Digite a quantidade de notas que quer lançar: "))
        if num_notas <= 0:
            print("O número de notas deve ser maior que 0")
            return  # Saída antecipada do método
        else:
            for i in range(num_notas):
                nota = float(input(f"Informe a nota {i+1}: "))
                self.notas.append(nota)

# Criando um aluno
aluno1 = Aluno("Ruan", 1)

aluno1.exibir()
# Lançando notas
aluno1.lancar_notas()

# Exibindo informações do aluno
aluno1.exibir()

#8. Classe Retangulo
   #- Crie uma classe Retangulo com atributos de largura e altura. Adicione métodos para calcular área e perímetro.

class Retangulo:
    def __init__(self,larg,alt):
        self.larg= larg
        self.alt= alt

    def calc_area(self):
        area= self.larg * self.alt
        return print("A área é de {}".format(area))
    
    def calc_peri(self):
        peri= (self.larg*2)+(self.alt*2)
        return print("O perimetro é {}".format(peri))

retangulo1= Retangulo(20,30)

retangulo1.calc_area()
retangulo1.calc_peri()

#9. Classe Data
   #- Crie uma classe Data com atributos dia, mês e ano. Crie métodos para verificar se a data é válida e para exibir a data no formato "DD/MM/AAAA".

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

#10. Classe  Quadrado 
   #- Crie uma classe Quadrado com um atributo lado. Adicione métodos para calcular a área e o perímetro do quadrado.

class Quadrado:
    def __init__(self,lado):
        self.lado= lado

    def calc_area_qua(self):
        area= self.lado **2 
        return print("A área é de {}".format(area))
    
    def calc_peri_qua(self):
        peri= self.lado * 4 
        return print("O perimetro é {}".format(peri))

qua1= Quadrado(20)

qua1.calc_area_qua()
qua1.calc_peri_qua()

#11. Classe Produto
   #- Crie uma classe de produtos com atributos como nome, preço, quantidade. Adicione um método que retorna o valor total de um produto (preço * quantidade).

class Produto:
    def __init__(self,produtos):
        self.produtos = []
    

    def criar_prod(self,nome,preco,quant):
        if any(produto['nome']== nome for produto in self.produtos):
            print("O produto {} já existe".format(nome))
        else:
            novo_produto= {'nome':nome,'preco':preco,'quant':quant}

            self.produtos.append(novo_produto)
            print("Produto {} criado com sucesso".format(nome))

    def exibir(self):
        if not self.produtos:
            print("Nenhum produto encontrado")
            return
        else:
            print("porodutos registrados: ")
            for produto in self.produtos:
                print("Nome: {} Preço: {} Quantidade: {} Valor total: {}".format(produto['nome'],produto['preco'],produto['quant'],(int(produto['preco'])*int(produto['quant']))))
        

estoque=Produto(1)
estoque.criar_prod("Camisa",29.99,10)
estoque.criar_prod("Calça",79.99,20)
estoque.criar_prod("Camisa",29.99,50)

estoque.exibir()

#12. Classe PessoaJuridica
   #- Crie uma classe Pessoa Jurídica com atributos  de razão social ,  CNPJ ,  telefone . Adicione métodos para validar o CNPJ e exibir as informações da empresa.

#13. Classe  Endereco 
   #- Crie uma classe  Endereço  com atributos de rua ,  número ,  bairro ,  cidade ,  cep . Adicione métodos para exibir o endereço completo e verificar se o endereço é válido.

#14. Classe ContaPoupanca
  # - Crie uma classe  ContaPoupanca  com atributos  número conta ,  saldo  e  taxa de juros . Adicione métodos para depositar, sacar e aplicar juros no saldo.

#15. Classe  Livro Digital 
   #- Crie uma classe  Livro Digital  com atributos  título ,  autor ,  data publicação ,  formato  (PDF, EPUB). Adicione um método que exibe as informações do livro.

#16. Classe  Temperatura 
   #- Crie uma classe  Temperatura  com atributos  graus celsius  e adicione métodos para converter a temperatura para Fahrenheit e Kelvin.

#17. Classe  Bicicleta 
   #- Crie uma classe  Bicicleta  com atributos  modelo ,  cor ,  velocidade máxima . Adicione métodos para aumentar e diminuir a velocidade.

#18. Classe  Cachorro 
   #- Crie uma classe  Cachorro  com atributos como nome ,  raça ,  idade  e um método para o cachorro latir.

#19. Classe  NotaFiscal 
   #- Crie uma classe  NotaFiscal  com atributos  número ,  descrição ,  valor total  e  data emitida . Adicione um método para exibir as informações da nota fiscal.

#20. Classe  Transporte 
   #- Crie uma classe  Transporte  com atributos  tipo  (carro, bicicleta, avião),  velocidade máxima é um método para exibir as informações do transporte.

#21. Classe  Produto Com Desconto 
   #- Crie uma classe  Produto Desconto  com atributos  nome ,  preço ,  desconto  (em percentual). Adicione um método para calcular o preço com desconto.

#22. Classe  Livro  com Contagem de Páginas
   #- Crie uma classe  Livro  com atributos  título ,  autor ,  páginas . Adicione métodos para exibir as informações do livro e para calcular o número de páginas restantes.


#23. Classe  Conta
   #- Crie uma classe  Conta  com atributos de saldo  e  limite . Adicione métodos para realizar depósitos, saques e verificar se o saldo é suficiente para um saque.

#24. Classe  Pessoa  com Atributos Privados
   #- Crie uma classe  Pessoa  com atributos privados  nome ,  idade  e  email . Adicione métodos para acessar e modificar esses atributos.

#25. Classe  Aluno  com Presença
   #- Crie uma classe  Aluno  com atributos  nome ,  matrícula ,  presença  (lista de presenças). Adicione um método para calcular a porcentagem de presenças e verificar se o aluno atingiu a quantidade mínima de presença.

#26. Classe  Veiculo 
   #- Crie uma classe  Veículo  com atributos  modelo ,  cor ,  ano ,  placa . Adicione um método para exibir as informações do veículo.

#27. Classe  Desconto 
   #- Crie uma classe  Desconto  com atributos  valor  e  percentual . Adicione um método para aplicar o desconto sobre o valor e retornar o preço final.

#28. Classe  Produto Com Estoque 
  # - Crie uma classe  Produto Estoque  com atributos como nome ,  preço ,  quantidade em estoque . Adicione métodos para atualizar a quantidade no estoque e calcular o valor total de estoque.

#29. Classe  Gorjeta 
   #- Crie uma classe  gorjeta  com atributos  valor conta ,  percentual . Adicione um método para calcular o valor da gorjeta.

#30. Classe  CartaoCredito
#- Crie uma classe  Cartao Credito  com atributos  numero cartão ,  limite ,  saldo devedor . Adicione métodos para realizar compras e calcular o saldo devedor.


