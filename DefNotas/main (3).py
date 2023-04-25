class Aluno:
  def __init__(self,matricula,nome):
    self.matricula = matricula
    self.nome = nome
    
class Disciplina:
  def __init__(self,nome):
    self.alunos = []
    self.notasn1 = []
    self.notasn2 = []
    self.notasn1js = []
    self.notasn2js = []
    self.nome = nome
  def matricular(self,Aluno):
    self.alunos.append(Aluno)
  def notaN1(self,Aluno):
    self.notasn1.append(Aluno)
  def notaN1js(self,Aluno):
    self.notasn1js.append(Aluno)
  def notaN2(self,Aluno):
    self.notasn2.append(Aluno)
  def notaN2js(self,Aluno):
    self.notasn2js.append(Aluno)
  def listarAlunos(self):
    aux = []
    for x in self.alunos:
      aux.append(x.nome)
    return aux
  def listarNotaN1(self):
    auy = []
    for y in self.notasn1:
      auy.append(y)
    return auy
  def listarNotaN2(self):
    auv = []
    for v in self.notasn2:
      auv.append(v)
    return auv
  def listarNotaN1js(self):
    auy = []
    for y in self.notasn1js:
      auy.append(y)
    return auy
  def listarNotaN2js(self):
    auv = []
    for v in self.notasn2js:
      auv.append(v)
    return auv
  def media(self):
    return (notaN1+notaN2)/2
  
p1 = Aluno(134,"Roberto")
p2 = Aluno(135,"Maria")
d1 = Disciplina("POO")
d2 = Disciplina("JS")
d1.matricular(p1)
d1.matricular(p2)
d2.matricular(p1)
d1.notaN1(float(input("Qual a nota?: ")))
d1.notaN2(float(input("Qual a nota?: ")))
d2.notaN1(float(input("Qual a nota?: ")))
d2.notaN2(float(input("Qual a nota?: ")))
d1.notaN1js(float(input("Qual a nota?: ")))
d1.notaN2js(float(input("Qual a nota?: ")))

print("POO:" , d1.listarAlunos() , "\nJS:" , d2.listarAlunos())
print("")
print("Nota N1 POO:""\n Roberto:",d1.listarNotaN1(),"\n Maria:",d2.listarNotaN1(),"\nNota N2 POO:","\n Roberto:",d1.listarNotaN2(),"\n Maria:",d2.listarNotaN2())
print("")
print("Nota N1 JS:","\n Roberto:",d1.listarNotaN1js(),"\nNota N2 JS:","\n Roberto:",d1.listarNotaN2js())