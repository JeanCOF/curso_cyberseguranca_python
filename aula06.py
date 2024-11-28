lista = [1,2,3,4]
iterador = iter(lista)
print(next(iterador)) 
print(next(iterador)) 
print(iterador.__next__()) 
print(iterador.__next__()) 
next(iterador)


for elemento in lista:
    print(lista)

#for elemento in iteravel:

objeto_iteravel = iter(iteravel) 
# Loop infinito
while True:
    try:
        # obtém o novo item
        elemento = next(objeto_iteravel)
        # faz algo com o elemento
    except StopIteration:
    # Se o StopIteration ocorrer, break no loop
    break   


import random
class RandomIterable:
    def __iter__(self):
        return self
    def __next__(self):
        if random.choice(["go", "go", "stop"]) == "stop":
            raise StopIteration  # finaliza o iterador
        return 1
for x in RandomIterable():
    print(x)
# 1
# 1
# 1