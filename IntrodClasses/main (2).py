class Casinha:
  def __init__(self,nome):
    self.nome = nome
  def receber(self,Animal):
    print(f'{Animal.nome} entrou na casinha...')
    
class Animal():
  def __init__(self, nome):
    self.nome = nome;
  def comer(self):
    print("animal comendo...")

class Gato(Animal):
  def __init__(self,nome,raça):
    super().__init__(nome)
  def comer(self):
    print("gato comendo...")
  def barulho(self):
    print('gato berrando...')
    
a1 = Animal('tigre')
a1.comer()
casa = Casinha('casinha')
gato = Gato('Kuro','angora')
gato.comer()
gato.barulho()
casa.receber(gato)