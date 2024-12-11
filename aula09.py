from abc import ABC, abstractmethod
#Parte 1: Entendendo o Polimorfismo
#1. Explique com suas palavras o que é polimorfismo.

#2. Crie duas classes vazias chamadas Animal e Veiculo.
class Animal:
    def mover(self):
        pass  # Método vazio

class Veiculo:
    def mover(self):
        pass  # Método vazio

#3. Adicione um método chamado mover() em ambas as classes, mas sem implementar nada dentro deles.

#4. Crie dois objetos, um de cada classe, e chame o método mover() de ambos.
animal = Animal()
veiculo = Veiculo()
#5. Explique o que acontece ao tentar chamar o método mover() sem implementá-lo. 

# O método 'mover' é chamado, mas como ele está vazio (pass), nada de efetivo ocorre.

# Parte 2: Polimorfismo com Métodos

#6. Crie uma classe chamada Cachorro com um método falar() que imprime "Au au!".
class Cachorro:
    def falar(self):
        print("Au au!")

#7. Crie outra classe chamada Gato com o método falar() que imprime "Miau!".
class Gato:
    def falar(self):
        print("Miau!")

#8. Crie objetos para ambas as classes e chame o método falar() de cada um.
cachorro = Cachorro()
gato = Gato()

#9. O que acontece quando dois objetos diferentes possuem métodos com o mesmo nome?

# O polimorfismo permite que objetos de diferentes classes respondam de maneira diferente ao mesmo nome de método.
# O método falar() tem comportamentos diferentes dependendo da classe do objeto.

#10.Implemente uma classe Papagaio com o método falar() que imprime "Olá!" e repita o processo.

class Papagaio:
    def falar(self):
        print("Olá!")

Papagaio = Papagaio()

#Parte 3: Uso de Polimorfismo com Funções

#11.Escreva uma função chamada chamar_fala(objeto) que chama o método falar() do objeto recebido.

def chamar_fala(objeto):
    objeto.falar()  # Chama o método falar() do objeto

#12.Use a função chamar_fala() com um objeto de cada uma das classes Cachorro, Gato e Papagaio.
chamar_fala(cachorro)  # "Au au!"
chamar_fala(gato)  # "Miau!"
chamar_fala(Papagaio) # "Olá"

#13.O que acontece se você passar um objeto sem o método falar() para a função?

#ocorre um erro (AttributeError).

#14.Modifique a função chamar_fala() para verificar se o método existe antes de chamá-lo.
def chamar_fala(objeto):
    if hasattr(objeto, 'falar'):
        objeto.falar()
    else:
        print("Este objeto não pode falar.")
#15.Adicione uma classe Carro sem o método falar() e teste a função chamar_fala() com ela.

class Carro:
    pass

carro = Carro()
chamar_fala(carro)  # "Este objeto não pode falar."

#Parte 4: Polimorfismo com Herança

#16.Crie uma classe base chamada Animal com um método falar() vazio (usando pass).

class Animal:
    def falar(self):
        pass  # Método vazio

#17.Faça as classes Cachorro, Gato e Papagaio herdarem de Animal e sobrescrevam o método falar().

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")

class Papagaio(Animal):
    def falar(self):
        print("Olá!")
#18.Crie uma lista contendo objetos de cada classe e itere sobre ela chamando o método falar().

animais = [Cachorro(), Gato(), Papagaio()]

for animal in animais:
    animal.falar() 

#19.Explique como a herança facilita a implementação do polimorfismo nesse exemplo.

#Herança facilita a implementação de polimorfismo, pois todas as classes filhas podem sobrescrever o método 'falar' da classe base 'Animal'.

#20.Adicione outra classe chamada Peixe que também herda de Animal, mas com um método falar() que imprime "Peixes não falam".

class Peixe(Animal):
    def falar(self):
        print("Peixes não falam")


peixe = Peixe()
peixe.falar()  

#Parte 5: Polimorfismo com Interfaces

#21.Crie uma classe abstrata chamada Forma com um método abstrato area().

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

#22.Implemente as classes Retangulo e Circulo que herdam de Forma e implementam o método area().

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

#23.Crie um objeto de cada classe e chame o método area() para calcular a área.

retangulo = Retangulo(5, 3)
circulo = Circulo(4)

print(retangulo.area())  
print(circulo.area())  

#24.Explique o que acontece se você tentar instanciar a classe Forma.

#A classe Forma não pode ser instanciada diretamente, pois é abstrata.

#25.Adicione outra classe chamada Triangulo e implemente o método area().
class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

triangulo = Triangulo(6, 4)
print(triangulo.area())  

#Parte 6: Polimorfismo com Sobrecarga (Overloading Simulado)


#26.Crie uma classe chamada Calculadora com um método chamado somar().
class Calculadora:
    def somar(self, a, b, c=0):  
        return a + b + c

#27.Faça o método somar() aceitar dois números como parâmetros e retornar a soma deles.

calc = Calculadora()
print(calc.somar(2, 3))  
print(calc.somar(2, 3, 4))

#28.Modifique o método somar() para aceitar três números e somá-los, usando argumentos padrão.

#29.Teste o método somar() com dois e três argumentos.

#30.O Python permite sobrecarga verdadeira? Explique. 

#O Python não suporta sobrecarga de métodos de forma verdadeira como outras linguagens. Mas podemos simular sobrecarga usando argumentos padrão ou *args.

# Parte 7: Polimorfismo com Sobrescrita (Overriding)

#31.Crie uma classe chamada Forma com um método desenhar() que imprime "Desenhando uma forma".

class Forma:
    def desenhar(self):
        print("Desenhando uma forma")

#32.Crie uma classe Circulo que sobrescreve o método desenhar() para imprimir "Desenhando um círculo".

class Circulo(Forma):
    def desenhar(self):
        print("Desenhando um círculo")

#33.Crie um objeto de Circulo e chame o método desenhar().

circulo = Circulo()
circulo.desenhar()

#34.Adicione outra classe chamada Quadrado que também sobrescreve o método desenhar().

class Quadrado(Forma):
    def desenhar(self):
        print("Desenhando um quadrado")

#35.Explique a diferença entre sobrescrita de métodos e sobrecarga. Parte 8: Polimorfismo com Coleções

#A sobrecarga envolve múltiplos méstods com o mesmo nome mas com assinaturas diferentes

#36.Crie uma lista com objetos de Cachorro, Gato, Papagaio e Peixe.

animais = [Cachorro(),Gato(),Papagaio(),Peixe()]

#37.Itere sobre a lista chamando o método falar() para cada objeto.

for animal in animais:
    animal.falar()

#38.Explique como o polimorfismo facilita o uso de coleções de objetos diferentes.

#O polimorfismo permite adicionar objetos diferentes em uma coleção sem se preocupar com o tipo específico do objeto

#39.Adicione um novo objeto de classe Carro à lista e tente iterar novamente.

onix=Carro()

#animais = [Cachorro(),Gato(),Papagaio(),Peixe(),onix()]
#for animal in animais:
    #animal.falar()

#40.Explique por que é importante validar os métodos antes de chamá-los. Parte 9: Praticando o Polimorfismo

#É importante validar métodos antes de chamá-los, pois nem todos os objetos na lista terão o mesmo comportamento ou métodos.

#41.Implemente um sistema de pagamento com uma classe base Pagamento e classes específicas como Credito e Debito.

class Pagamento:
    def processar_pagamento(self):
        pass 

#42.Faça cada classe implementar um método processar_pagamento() de forma diferente.

class Credito(Pagamento):
    def processar_pagamento(self):
        print("Pagamento processado via Crédito")

class Debito(Pagamento):
    def processar_pagamento(self):
        print("Pagamento processado via Débito")

#43.Crie uma lista de objetos de pagamento e processe cada um iterativamente.

pagamentos = [Credito(), Debito()]

for pagamento in pagamentos:
    pagamento.processar_pagamento()

#44.Adicione uma classe Pix e implemente o método processar_pagamento().

class Pix(Pagamento):
    def processar_pagamento(self):
        print("Pagamento processado via pix")

#45.Explique por que o polimorfismo torna o sistema mais extensível. 

#O polimorfismo torna o sistema mais extensível, pois podemos adicionar novos métodos de pagamento sem modificar o código existente.

# Parte 10: Desafios Finais

#46.Crie um sistema de transporte com uma classe base Transporte e subclasses como Carro, Bicicleta e Trem.

class Transporte:
    def acelerar(self):
        pas
#47.Adicione métodos como acelerar() e frear() para cada classe e implemente-os de maneira diferente.

class Carro(Transporte):
    def acelerar(self):
        print("Carro acelerando")

class Bicicleta(Transporte):
    def acelerar(self):
        print("Bicicleta acelerando")

class Trem(Transporte):
    def acelerar(self):
        print("Trem acelerando")
#48.Crie uma função que aceita objetos de Transporte e chama seus métodos.

def testar_transporte(transporte):
    transporte.acelerar()
#49.Adicione uma nova classe chamada Aviao ao sistema e integre-a sem alterar a função.
class Aviao(Transporte):
    def acelerar(self):
        print("Avião acelerando")

#50.Explique como o polimorfismo ajuda na manutenção e escalabilidade de programas complexos. 

#O polimorfismo facilita a manutenção e escalabilidade, pois podemos adicionar novos tipos de transporte sem modificar as funções ou o código existente.