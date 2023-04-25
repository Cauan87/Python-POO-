class Pessoa:
  def __init__(self,nome,cpf):
    self.nome = nome
    self.cpf = cpf
    self.velocidade = 0
  def correr(self,velocidade):
    self.velocidade = velocidade
    
class Pessoa2(Pessoa):
  def __init__(self,nome,cpf):
    Pessoa.__init__(self, nome, cpf)

p1 = Pessoa("Cauan",123)
p2 = Pessoa2("Junior",321)
p1.correr(22.5)
p2.correr(21.1)

print((p1.nome),"correu,","E sua velocidade é de:","",(p1.velocidade),"km/h")
print((p2.nome),"correu,","E sua velocidade é de:","",(p2.velocidade),"km/h")