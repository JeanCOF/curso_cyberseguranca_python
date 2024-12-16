#Avaliação Final.

# Parte 1: Entendendo o Polimorfismo
#1. Explique com suas palavras o que é polimorfismo.

# è um conceito de P.O.O em python que permite que objetos diferemte sejam tratados de forma uniforme.

#2. Crie duas classes vazias chamadas Pessoa e Objeto.
class Pessoa:
    pass

class Objeto:
    pass
#3. Adicione um método chamado executar() em ambas as classes, mas sem implementar nada dentro deles.
class Pessoa:
    def executar(self):   
        pass

class Objeto:
    def executar(self):  
        pass

#4. Crie dois objetos, um de cada classe, e chame o método executar() de ambos.

joao= Pessoa()
cadeira= Objeto()

#5. Explique o que acontece ao tentar chamar o método executar() sem implementá-lo.

#nada acontece, pois o método foi declarado, mas não implementado em ambas as classes.

# Parte 2: Polimorfismo com Métodos

#6. Crie uma classe chamada Leão com um método falar() que imprime "Rugido!".

class Leao:
    def falar(self):
        print("Rugido!")

#7. Crie outra classe chamada Lobo com o método falar() que imprime "Uivo!".

class Lobo:
    def falar(self):
        print("Uivo")

#8. Crie objetos para ambas as classes e chame o método falar() de cada um.

mufasa= Leao()
lobo_guara= Lobo()

def chamar_fala(objeto):
    objeto.falar()

chamar_fala(mufasa)
chamar_fala(lobo_guara)

#9. O que acontece quando dois objetos diferentes possuem métodos com o mesmo nome?

#o Python utiliza o conceito de polimorfismo. Isso significa que, embora os métodos tenham o mesmo nome, eles podem ter comportamentos diferentes dependendo do tipo de objeto que os chama.

#10. Implemente uma classe Arara com o método falar() que imprime "Bom dia!" e repita o processo.

class Arara:
    def falar(self):
        print("Bom dia")

blue= Arara()

chamar_fala(blue)

# Parte 3: Uso de Polimorfismo com Funções

#11. Escreva uma função chamada executar_acao(objeto) que chama o método falar() do objeto recebido.


#def chamar_fala(objeto):
    #objeto.falar()

#12. Use a função executar_acao() com um objeto de cada uma das classes Leão, Lobo e Arara.

#executado acima

#13. O que acontece se você passar um objeto sem o método falar() para a função?

#o Python gerará um erro do tipo AttributeError, informando que o objeto não tem o atributo

#14. Modifique a função executar_acao() para verificar se o método existe antes de chamá-lo.

#retorna True se o objeto tem o método especificado e False caso contrário.

#15. Adicione uma classe Bicicleta sem o método falar() e teste a função executar_acao() com ela.

class Bicicleta:
    pass

kaloi=Bicicleta

#chamar_fala(kaloi)

#AttributeError: type object 'Bicicleta' has no attribute 'falar'


# Parte 4: Polimorfismo com Herança

#16. Crie uma classe base chamada Veiculo com um método mover() vazio (usando pass).

class Veiculo:
    def mover(self):
        pass

#17. Faça as classes Carro, Moto e Caminhão herdarem de Veiculo e sobrescrevam o método mover().

class Carro(Veiculo):
    def mover(self):
        print("Movendo o carro")

class Moto(Veiculo):
    def mover(self):
        print("Movendo a moto")

class Caminhao(Veiculo):
    def mover(self):
        print("Movendo o caminhão")

#18. Crie uma lista contendo objetos de cada classe e itere sobre ela chamando o método mover().

fusca=Carro()
hornet=Moto()
escania=Caminhao()


veiculos = [fusca, hornet, escania]

for veiculo in veiculos:
    veiculo.mover() 

#19. Explique como a herança facilita a implementação do polimorfismo nesse exemplo.

#A herança facilita a implementação do polimorfismo no exemplo porque a classe Carro, Moto e Caminhao herdam de uma classe base comum, a classe Veiculo

#20. Adicione outra classe chamada Patinete que também herda de Veiculo, mas com um método mover() que imprime "Patinetes deslizam".

class Patinete(Veiculo):
    def mover(self):
        print("Patinetes deslizam")

# Parte 5: Polimorfismo com Interfaces
from abc import ABC, abstractmethod

#21. Crie uma classe abstrata chamada Figura com um método abstrato perimetro().

class Forma(ABC):
    @abstractmethod
    def perimetro(self):
        pass

#22. Implemente as classes Quadrado e TrianguloEquilatero que herdam de Figura e implementam o método perimetro().

class Quadrado(Forma):
    def __init__(self,lado):
        self.lado = lado
    def perimetro(self):
        return self.lado * 4

class TrianguloEquilatero(Forma):
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return self.lado * 3

#23. Crie um objeto de cada classe e chame o método perimetro() para calcular o perímetro.

quadrado1=Quadrado(10)
trinagulo1=TrianguloEquilatero(5)

print(quadrado1.perimetro())
print(trinagulo1.perimetro())

#24. Explique o que acontece se você tentar instanciar a classe Figura.

#A classe Figura é uma classe abstrata, o que significa que ela não pode ser instanciada diretamente.

#25. Adicione outra classe chamada Circulo e implemente o método perimetro().

import math

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def perimetro(self):
        return 2 * math.pi * self.raio

circulo1=Circulo(7)
print(circulo1.perimetro())