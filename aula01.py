#Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar este ano 
#inserção de dados
import datetime
ano = int(input("Digite seu ano de nascimento: "))
#importação da data atual
ano_atual=datetime.datetime.now().year
idade=ano_atual-ano
#verificação da idade
if (idade>=16):
    print("Você pode votar esse ano")
else:
    print("Você ainda não pode votar")
#Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha válida é o número 1234. Devem ser impressas as seguintes mensagens: 

#ACESSO PERMITIDO caso a senha seja válida. 
#ACESSO NEGADO caso a senha seja inválida. 

senha=int(input("DIGITE A SENHA: "))

while senha != 1234:
    print("Senha Inválida")
    senha=int(input("DIGITE A SENHA: "))
print("Acesso permitido")


#As maçãs custam R$0,30 cada se forem compradas menos do que uma dúzia, e R$0,#25 se forem compradas pelo menos doze. Escreva um programa que leia o número #de maçãs compradas, calcule e escreva o valor total da compra.
import locale

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
macas= float(input("Digite a quantidade de maças compradas: "))

if (macas>=12):
    macas=locale.currency(macas*0.25)
    print("O total a pagar é {}".format(macas))
else:
    macas=locale.currency(macas*0.30)
    print("O total a pagar é {}".format(macas))

#Escrever um algoritmo que lê 5 valores para a, um de cada vez, e conta quantos #destes valores são negativos, escrevendo esta informação. 
neg = 0
lista = []  

for i in range(5):
    num = int(input("Digite um valor: "))
    if num < 0:
        neg += 1  # Conta os números negativos
    lista.append(num)  # Adiciona o número à lista, seja negativo ou não

print("A lista é {} e possui {} números negativos".format(lista, neg))

#Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são #múltiplos de três e que se encontram no conjunto dos números de 1 até 500. 
num=0
for i in range(1,501):
    if  i % 2 !=0 and i % 3 ==0:
        num+= i
        print(num)

#Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200 

num=0
for i in range(1,201):
    if i % 2 !=0:
        num= i
        print(num)

#Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.

num = int(input("Digite um numero: "))

for i in range(1,11):
    res= num * i
    print(res)

#Validação de senha: Escreva um programa que peça ao usuário para digitar uma senha até que ele acerte usando um loop while. Senha 123 

senha=int(input("DIGITE A SENHA: "))

while senha != 123:
    print("Senha Inválida")
    senha=int(input("DIGITE A SENHA: "))
print("Acesso permitido")

#Elabore um programa que mostre todos os números múltiplos de 5 de 100 até 0. 

num=0
for i in range(101,0,-1):
    if i % 5 ==0:
        num= i
        print(num)

#Encontre o menor número em uma lista de números. 

print("lista: {}".format(lista_num))
print("O menor elemento é : {}".format(min(lista_num)))

 #Ordene uma lista de números em ordem crescente. 

lista_aleatoria=[1,789,43,674,-10,63,-100,90,2,4,6,-2,-3]
print("Lista : {}".format(lista_aleatoria))
print("Lista ordenada: {}".format(sorted(lista_aleatoria)))

# Ordene uma lista de números em ordem decrescente.

print("Lista : {}".format(lista_aleatoria))
print("Lista ordenada decrescente: {}".format(sorted(lista_aleatoria,reverse=True)))

#Inverta a ordem dos elementos em uma lista. 

print("Lista: {}".format(lista_num))
# Inverte a lista
lista_num.reverse()
# Imprime a lista invertida
print("Lista invertida: {}".format(lista_num))

 #Crie uma cópia de uma lista. 

copia= lista_num.copy()
print("lista: {}".format(lista_num))
print("Cópia da lista : {}".format(copia))

 ##Verifique se um valor específico está presente em um dicionário. 
dicio2={"nome":"jean","bairro":"leporace","cidade":"franca"}
print("verificação se leporace está no dicionário")
print("leporace" in dicio2.values())
#Conte quantos pares chave-valor um dicionário possui. 
print("Quantidade de elementos no dicionário")
print(len(dicio2))
#Copie um dicionário para outro. 
dicio3= dicio2
print(dicio3)
#Limpe todos os itens de um dicionário
dicio3.clear()
print(dicio3)