class Animal:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
    def mover():
        
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def mover():
        
        
class Cachorro:
    def __init__(self, raça, tamanho):
        self.raça = raça
        self.tamanho = tamanho
    def falar():
        print('Au, au')
        
class Gato:
    def __init__(self, raça, cor):
        def.raça = raça
        def.cor = cor
    def falar()    :
        print('Miau')
        
class Papagaio:
    def __init__(self, )
    
        






class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()