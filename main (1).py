class Posto():
  def __init__(self,nome):
    self.nome = nome
  def vacinar(self, pessoa, vacina):
    if vacina.nome not in pessoa.aplicadas:
      pessoa.aplicadas.append(vacina.nome)
  
class Pessoa():
  def __init__(self,nome):
    self.nome = nome
    self.aplicadas = []
  def ir (self):
    print(f'{self.nome} Foi ao posto')

class Vacina():
  def __init__(self,nome):
    self.nome = nome

p1 = Pessoa('Pedro')
p2 = Pessoa('Junior')
posto = Posto('frotinha')
p1.ir()
posto.vacinar(p1, Vacina('Sarampo'))
v1 = Vacina('Sarampo')
v2 = Vacina('Gripe')
p2.ir()
posto.vacinar(p2, Vacina('Gripe'))
posto.vacinar(p2, Vacina('Sarampo'))

print(p1.aplicadas)
print(p2.aplicadas)