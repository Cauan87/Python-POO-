class Quadrado:
  def __init__(self,lado):
    self.lado = lado

  def CalcArea(self):
    areaq = self.lado * self.lado
    return areaq
r1 = Quadrado(2)
r2 = Quadrado(6)  
print('A area do r1 é:',r1.CalcArea())
print('A area do r2 é:',r2.CalcArea())