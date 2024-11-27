"""mytuple= ("apple","banana", "cherry")

myit= iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr= "banana"

myit= iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

class Mynumbers:
    def __init__(self):
        self.a = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

# Criando a instância da classe
myclass = Mynumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)"""


"""Iteração com listas e iter
1. Crie um objeto iterável a partir de uma lista [1, 2, 3, 4] e imprima o primeiro item usando
next.
2. Use iter para criar um iterador para a lista [10, 20, 30] e imprima todos os elementos
usando um loop for.
3. Faça um iterador a partir de uma lista de frutas ['maçã', 'banana', 'laranja'] e
imprima o segundo item usando next.

Iteração com strings
4. Crie um iterador para a string "Python" e imprima o primeiro caractere usando next.
5. Use iter para transformar "abcd" em um iterador e percorra todos os caracteres com next.
6. Imprima todos os caracteres de "exemplo" usando um loop while e iter.

Iteração com dicionários
7. Crie um iterador a partir das chaves de um dicionário {'a': 1, 'b': 2, 'c': 3} e
imprima as chaves.
8. Use iter para criar um iterador a partir dos valores de um dicionário e imprima-os usando next.
9. Faça um iterador para os itens de um dicionário e imprima os pares (chave, valor) usando
um loop while.

Iteração com tuplas
10. Transforme a tupla (1, 2, 3) em um iterador e imprima os elementos usando um loop for.
11. Crie um iterador a partir da tupla ('a', 'b', 'c') e use next para acessar o terceiro
elemento.
12. Use iter em uma tupla vazia () e mostre o que acontece ao tentar usar next."""
#1

seq= [1,2,3,4,5]

myit= iter(seq)

print(next(myit))

#2

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

#3

frutas = ['maçã', 'banana', 'laranja']


myit = iter(frutas)

next(myit)  
segundo_item = next(myit)  

print(segundo_item)

#4

mystr= "Python"

myit= iter(mystr)

print(next(myit))

#5

mystr= "ABCD"

myit= iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#6

mystr= "exemplo"

myit= iter(mystr)

while myit:
    try:
        print(next(myit))
    except StopIteration:

        print("ENCERRADO")
        break

#7

dicionario = {'a': 1, 'b': 2, 'c': 3}


iterador = iter(dicionario)

print(next(iterador))
print(next(iterador))  
print(next(iterador)) 

#8

dicionario = {'a': 1, 'b': 2, 'c': 3}

iterador = iter(dicionario)

print(dicionario[next(iterador)])  
print(dicionario[next(iterador)])  
print(dicionario[next(iterador)])  

#9

dicionario = {'a': 1, 'b': 2, 'c': 3}

iterador = iter(dicionario.items())

while True:
    try:
        chave, valor = next(iterador)
        print(chave, valor)
    except StopIteration:
        print("ENCERRADO")
        break

#10

tupla = (1, 2, 3)


iterador = iter(tupla)


for elemento in iterador:
    print(elemento)

#11


tupla = ('a', 'b', 'c')

iterador = iter(tupla)

next(iterador)  
next(iterador)  
terceiro_elemento = next(iterador)  
print(terceiro_elemento)

#12
tupla_vazia = ()

iterador = iter(tupla_vazia)

try:
    print(next(iterador))
except StopIteration:
    print("Não há elementos na tupla vazia.")
