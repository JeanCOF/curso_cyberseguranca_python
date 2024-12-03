x = lambda a : a + 10

print(x(5))


x = lambda a, b : a * b

print(x(5,6))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

#Crie uma função lambda que retorne a soma de dois números.

x = lambda a,b : a + b 

print("1: {}".format(x(4,5)))
#Crie uma função lambda que retorne o quadrado de um número.

x = lambda a : a * a 

print("2: {}".format(x(4)))

#Crie uma função lambda que retorne o triplo de um número.

x = lambda a : a * 3 

print("3: {}".format(x(4)))

#Crie uma função lambda que verifique se um número é par.


par = lambda a: a % 2 == 0


def confere_par(a):
    if par(a):  
        print(f"4: {a}: O número é par")
    else:
        print(f"4: {a}: O número é ímpar")


confere_par(8)  
confere_par(7)  


#Crie uma função lambda que verifique se um número é ímpar.

par = lambda a: a % 2 == 0


def confere_par(a):
    if par(a):  
        print(f"5: {a}: O número é par")
    else:
        print(f"5: {a}: O número é ímpar")


confere_par(8)  
confere_par(7)  

#Crie uma função lambda que calcule o dobro de um número.

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print("6: {}".format(mydoubler(11)))

#Crie uma função lambda que converta uma temperatura em Celsius para Fahrenheit.

celsius_to_fahrenheit = lambda c: (c * 9/5) + 32

print("8: {}".format(celsius_to_fahrenheit(34)))

#Crie uma função lambda que retorne o valor absoluto de um número.

abs_value = lambda x: abs(x)

print("9: {}".format(abs_value(10)))

#Crie uma função lambda que calcule a soma dos quadrados de dois números.

sum_of_squares = lambda x, y: x**2 + y**2

print("10: {}".format(sum_of_squares(5,8)))

#Crie uma função lambda que calcule a média de três números.

average_of_three = lambda x, y, z: (x + y + z) / 3

print("11: {}".format(6,10,78))

#Crie uma função lambda que determine se uma string é maior que 5 caracteres.

is_greater_than_five = lambda s: len(s) > 5

print("12: {}".format(is_greater_than_five("parálelepipedo")))

#Crie uma função lambda que converta uma string para maiúsculas.

to_uppercase = lambda s: s.upper()

print("13: {}".format(to_uppercase("Rodizio")))

#Crie uma função lambda que converta uma string para minúsculas.

to_lowercase = lambda s: s.lower()

print("14: {}".format(to_lowercase("Rodizio")))

#Crie uma função lambda que calcule a raiz quadrada de um número.

sqrt_value = lambda x: x ** 0.5

print("13: {}".format(sqrt_value(848)))

#Crie uma função lambda que retorne a primeira letra de uma palavra.
first_letter = lambda s: s[0] if s else None

print("14: {}".format(first_letter("Rodizio")))

#Crie uma função lambda que inverta uma string.

reverse_string = lambda s: s[::-1]

print("15: {}".format(reverse_string("Rodizio")))

#Crie uma função lambda que calcule o cubo de um número.

cube_value = lambda x: x ** 3

print("16: {}".format(cube_value(9)))

#Crie uma função lambda que adicione 10 a um número.

add_ten = lambda x: x + 10

print("17: {}".format(add_ten(20)))

#Crie uma função lambda que multiplique dois números.

multiply = lambda x, y: x * y

print("18: {}".format(multiply(2,10)))

#Crie uma função lambda que divida dois números.

divide = lambda x, y: x / y if y != 0 else "Erro: Divisão por zero"

print("19: {}".format(divide(10,20)))

#Crie uma função lambda que calcule a diferença entre dois números.

difference = lambda x, y: x - y

print("20: {}".format(difference(453,386)))

#Crie uma função lambda que encontre o maior de dois números.

max_of_two = lambda x, y: x if x > y else y

print("21: {}".format(max_of_two(25,10)))

#Crie uma função lambda que encontre o menor de dois números.

min_of_two = lambda x, y: x if x < y else y

print("22: {}".format(min_of_two(25,10)))

#Crie uma função lambda que calcule a média de uma lista de números.

average_list = lambda lst: sum(lst) / len(lst) if lst else 0

lista = [1,2,3,4,5]

print("23: {}".format(average_list(lista)))

#Crie uma função lambda que calcule o fatorial de um número.

factorial = lambda x: 1 if x == 0 else x * factorial(x-1)

print("24: {}".format(factorial(6)))

#Crie uma função lambda que calcule a área de um círculo (π * r²).

area_of_circle = lambda r: 3.14159 * r ** 2

print("25: {}".format(area_of_circle(20)))

#Crie uma função lambda que calcule a área de um triângulo (base * altura / 2).

area_of_triangle = lambda b, h: (b * h) / 2

print("26: {}".format(area_of_triangle(10,20)))

#Crie uma função lambda que calcule a área de um retângulo (base * altura).

area_of_rectangle = lambda b, h: b * h

print("27: {}".format(5,30))

#crie uma função lambda que calcule o perímetro de um quadrado (4 * lado).

perimeter_of_square = lambda l: 4 * l

print("28: {}".format(perimeter_of_square(8)))

#Crie uma função lambda que calcule o perímetro de um retângulo (2 * (base + altura)).

perimeter_of_rectangle = lambda b, h: 2 * (b + h)

print("29: {}".format(20,30))

#Crie uma função lambda que retorne o maior valor entre três números.

max_of_three = lambda x, y, z: max(x, y, z)

print("30: {}".format(max_of_three(10,20,30)))

#Crie uma função lambda que retorne o menor valor entre três números.

min_of_three = lambda x, y, z: min(x, y, z)

print("31: {}".format(min_of_three(10,20,30)))

#Crie uma função lambda que calcule a soma de todos os elementos de uma lista.
sum_list = lambda lst: sum(lst)

#Crie uma função lambda que calcule a multiplicação de todos os elementos de uma lista.
multiply_list = lambda lst: 1 if not lst else lst[0] * multiply_list(lst[1:])

#Crie uma função lambda que calcule a média de uma lista de números.
average_of_list = lambda lst: sum(lst) / len(lst) if lst else 0

#Crie uma função lambda que calcule o valor de 10 elevado a um número.
power_of_10 = lambda x: 10 ** x

#Crie uma função lambda que encontre o comprimento de uma string.
length_of_string = lambda s: len(s)

#Crie uma função lambda que verifique se uma string é um palíndromo.
is_palindrome = lambda s: s == s[::-1]

#Crie uma função lambda que transforme uma lista de números em uma lista de quadrados.
squares_list = lambda lst: [x**2 for x in lst]

#Crie uma função lambda que remova todos os números negativos de uma lista.
remove_negatives = lambda lst: [x for x in lst if x >= 0]

#Crie uma função lambda que remova todas as strings vazias de uma lista.
remove_empty_strings = lambda lst: [x for x in lst if x]

#Crie uma função lambda que conte o número de vogais em uma string.
count_vowels = lambda s: sum(1 for c in s if c in 'aeiouAEIOU')

#Crie uma função lambda que calcule o valor de uma potência (base^exponente).
power = lambda base, exp: base ** exp

#rie uma função lambda que retorne True se um número for positivo e False caso contrário.
is_positive = lambda x: x > 0

#Crie uma função lambda que transforme uma lista de números em uma lista de seus valores absolutos.
absolute_list = lambda lst: [abs(x) for x in lst]

#Crie uma função lambda que calcule a soma de uma lista de números, mas ignore os números negativos.
sum_without_negatives = lambda lst: sum(x for x in lst if x >= 0)

#Crie uma função lambda que verifique se um número é múltiplo de 3.
is_multiple_of_three = lambda x: x % 3 == 0

#Crie uma função lambda que converta uma string de número em um número inteiro.
str_to_int = lambda s: int(s)

#Crie uma função lambda que calcule o número de caracteres em uma lista de strings.
count_chars_in_list = lambda lst: sum(len(s) for s in lst)

#Crie uma função lambda que transforme todos os números de uma lista em seu valor ao quadrado.
square_numbers_in_list = lambda lst: [x**2 for x in lst]
