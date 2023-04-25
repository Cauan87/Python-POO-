class Pessoa:
  def __init__(self,falar,andar):
    self.falar = falar
    self.andar = andar
class Filha:
  def __init__(self,falar,andar):
    self.conhecimentos = ["Andar","Falar"]
    self.falar = falar
    self.andar = andar
  def aprender(self,Filha):
    self.conhecimentos.append(Filha)
  def listarConhecimento(self):
    aux = []
    for x in self.conhecimentos:
      aux.append(x)
    return aux

p1 = Filha("Andar","Falar")
p1.aprender("Correr")
p1.aprender("Pular")
p1.aprender("Dançar")

print(p1.listarConhecimento())