import numpy as np

"""array = np.array([[1,2,3],[4,5,6]], int)

print(array)


array1 = np.arange(5)

array2 = np.arange(5,10)

print(array1)

print(array2)

print(array1+array2)

print(array1*2)

print(array1<array2)

print(array1>2)

print((array1>2) | (array1<5))

array = np.array([[1,2,3],[4,5,6],[7,8,8]])

print(array)
print(array[1, :])"""


"""1-10: Criação e propriedades básicas de arrays
1. Crie um array 1D com os números de 1 a 10.
2. Crie um array 2D 2×32 \times 3 com números de 1 a 6.
3. Crie um array preenchido apenas com zeros, de tamanho 3×33 \times 3.
4. Crie um array preenchido apenas com uns, de tamanho 2×52 \times 5.
5. Crie um array de números inteiros aleatórios entre 0 e 100, com 4 elementos.
6. Verifique o número de dimensões de um array 1D e de um array 2D.
7. Descubra o formato (shape) de um array 4×24 \times 2.
8. Crie um array com 10 números espaçados uniformemente entre 0 e 1.
9. Transforme um array de 1D para 2D (exemplo: 10 elementos para 2×52 \times 5).
10. Crie um array com os números pares de 2 a 20.

11-20: Manipulação de arrays
11. Inverta os elementos de um array 1D.
12. Crie um array de números de 1 a 9 e reorganize-o em uma matriz 3×33 \times 3.
13. Acesse o elemento da terceira linha e segunda coluna em uma matriz 3×33 \times 3.
14. Acesse todos os elementos da segunda coluna de uma matriz 3×33 \times 3.
15. Substitua todos os números maiores que 5 por 0 em um array 3×33 \times 3.
16. Adicione dois arrays 1D1D de mesmo tamanho.
17. Multiplique dois arrays 2D2D de mesmo tamanho (elemento a elemento).
18. Divida cada elemento de um array 1D1D por 2.
19. Crie um array 1D1D e calcule a soma de todos os seus elementos.
20. Encontre o maior e o menor valor em um array 2D2D."""

#1

array1 = np.arange(10)
print(array1)

#2

array2 = np.random.randint(1, 7, size=(2, 32, 3))
print(array2)

#3

array3 = np.zeros((3, 33, 3))
print(array3)

#4
array4 = np.random.randint(1, 2 , size=(2, 52, 5))
print(array4)

#5

array5 = np.random.randint(0, 100, size=(4))
print(array5)

#6

print("O numero de dimensoes do array 3 é : {}".format(array3.shape))
print("O numero de dimensoes do array 5 é : {}".format(array5.shape))

#7

array7 = np.random.randint(1, 7, size=(4, 24, 2))
print("O formato do array é:{}".format(array7.shape))

#8
array8 = np.linspace(0, 1, 10)
print(array8)

#9
array_1d = np.arange(10)  # array com números de 0 a 9
# Transformar o array 1D para 2D com forma 2x5
array_2d = array_1d.reshape(2, 5)
print(array_2d)

#10
array10 = np.arange(0, 11,2)
print(array10)

#11
print("array : {}".format(array10))
print("array invertido: {}".format(array10[::-1]))

#12
