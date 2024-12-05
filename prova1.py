import datetime
#Avaliação
#1. Converta um horário para o formato de string (ex: "HH:MM:SS").
print("EX 1--------------------------")
data_str = "12-12-03"

data_objeto = datetime.datetime.strptime(data_str, '%H-%M-%S')
print(data_objeto.time())

#2. Adicione 5 dias à data atual.
print("EX 2--------------------------")
data = datetime.datetime.now()
nova_data = data + datetime.timedelta(days=5)
print(nova_data)
#3. Subtraia 10 dias da data atual.
print("EX 3--------------------------")
nova_data = data + datetime.timedelta(days=-10)
print(nova_data)
#4. Adicione 3 horas ao horário atual.
print("EX 4--------------------------")
nova_data = data + datetime.timedelta(hours=3)
print(nova_data)
#5. Subtraia 30 minutos do horário atual.
print("EX 5--------------------------")
nova_data = data + datetime.timedelta(minutes=-30)
print(nova_data)
#6. Converta uma string de data "2024-12-03" em um objeto datetime.
print("EX 6--------------------------")
data_str = "2024-12-03"

data_objeto = datetime.datetime.strptime(data_str, '%Y-%m-%d')
print(data_objeto)
#7. Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano 
print("EX 7--------------------------")
#inserção de dados
ano = int(input("Digite seu ano de nascimento: "))
#importação da data atual
ano_atual=datetime.datetime.now().year
idade=ano_atual-ano
#verificação da idade
if (idade>=16):
    print("Você pode votar esse ano")
else:
    print("Você ainda não pode votar")

#8. Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. Devem ser impressas as seguintes mensagens: 
#ACESSO PERMITIDO caso a senha seja válida. 
#ACESSO NEGADO caso a senha seja inválida.
print("EX 8--------------------------")
senha=int(input("DIGITE A SENHA: "))

while senha != 1234:
    print("Senha Inválida")
    senha=int(input("DIGITE A SENHA: "))
print("Acesso permitido")

#9. As maçãs custam R$0,30 cada se forem compradas menos do que uma dúzia, e R$0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra
print("EX 9--------------------------")

import locale

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
macas= float(input("Digite a quantidade de maças compradas: "))

if (macas>=12):
    macas=locale.currency(macas*0.25)
    print("O total a pagar é {}".format(macas))
else:
    macas=locale.currency(macas*0.30)
    print("O total a pagar é {}".format(macas))

#10.Escrever um algoritmo que lê 5 valores para a, um de cada vez, e conta quantos destes valores são negativos, escrevendo esta informação. 
print("EX 10--------------------------")
neg = 0
lista = []  

for i in range(5):
    num = int(input("Digite um valor: "))
    if num < 0:
        neg += 1  # Conta os números negativos
    lista.append(num)  # Adiciona o número à lista, seja negativo ou não

print("A lista é {} e possui {} números negativos".format(lista, neg))

#11.Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500.

print("EX 11--------------------------")
soma = 0  
for i in range(1, 501):  
    if i % 2 != 0 and i % 3 == 0:  # Verifica se o número é ímpar e múltiplo de 3
        soma += i  

print("Soma dos números ímpares múltiplos de 3 de 1 até 500:", soma)

#12.Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200 
print("EX 12--------------------------")
num=0
for i in range(1,201):
    if i % 2 !=0:
        num= i
        print(num)

#13.Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.
print("EX 13--------------------------")
num = int(input("Digite um numero: "))

for i in range(1,11):
    res= num * i
    print(res)

#14.Validação de senha: Escreva um programa que peça ao usuário para digitar uma senha até que ele acerte usando um loop while. Senha 123 
print("EX 14--------------------------")
senha=int(input("DIGITE A SENHA: "))

while senha != 123:
    print("Senha Inválida")
    senha=int(input("DIGITE A SENHA: "))
print("Acesso permitido")

#15. Criar uma classe Carro
  #- Crie uma classe chamada Carro com atributos como modelo, cor, ano. Adicione métodos para exibir as informações sobre o carro e um método para acelerar.
print("EX 15--------------------------")
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


#16. Classe Livro
   #- Crie uma classe Livro com atributos título, autor e ano publicação. Adicione um método para exibir as informações do livro e outro para verificar se o livro foi publicado após 2000.
print("EX 16--------------------------")
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

#17. Classe Pessoa
   #- Crie uma classe Pessoa  com atributos como nome, idade e e-mail. Adicione métodos para exibir as informações da pessoa e verificar se a pessoa é maior de idade.

print("EX 17--------------------------")
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

#18. Conta Bancária
   #- Crie uma classe ContaBancaria que tenha métodos como depositar, sacar e consultar saldo. Crie um método para verificar se o saldo da conta é negativo.
print("EX 18--------------------------")
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

#19. Calculadora
   #- Crie uma classe Calculadora com métodos para as operações básicas: somar, subtrair, multiplicar e dividir.
print("EX 19--------------------------")
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


import numpy as np

#20. Crie um array 1D com os números de 1 a 10.
print("EX 20--------------------------")
array1 = np.arange(10)
print(array1)

#21.  Crie um array 2D 1 a 6.
print("EX 21--------------------------")
array2 = np.random.randint(1, 7, size=(2, 32, 3))
print(array2)

#22. Crie um array preenchido apenas com zeros,
print("EX 22--------------------------")
array3 = np.zeros((3, 33, 3))
print(array3)

#23. Crie um objeto iterável a partir de uma lista [1, 2, 3, 4] e imprima o primeiro item usando next.
print("EX 23--------------------------")
seq= [1,2,3,4,5]

myit= iter(seq)

print(next(myit))

#24. Use iter para criar um iterador para a lista [10, 20, 30] e imprima todos os elementos usando um loop for.
print("EX 24--------------------------")
class Mynumbers:
    def __init__(self):
        self.a = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= 100:
            x = self.a
            self.a += 10
            return x
        else:
            raise StopIteration
        
# Criando a instância da classe
myclass = Mynumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
#25. Faça um iterador a partir de uma lista de frutas ['maçã', 'banana', 'laranja'] e
#imprima o segundo item usando next.

print("EX 25--------------------------")
frutas = ['maçã', 'banana', 'laranja']


myit = iter(frutas)

next(myit)  
segundo_item = next(myit)  

print(segundo_item)

