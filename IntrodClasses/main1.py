y = int(input("Qual sua idade?: "))
if(y>=18):
  print("você já pode tirar a carteira de habilitação")
elif (y<=17) and (y>=12):
  print("você é só um adolescente")
else:
  print("você é uma criança")