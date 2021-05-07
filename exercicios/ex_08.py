# Ler nome e altura de n pessoas, informando os dados da mais alta e também da mais baixa

people = int(input("Quantas pessoas você deseja cadastrar: "))

i = 0
names = []
heights = []

while i < people:
  i = i + 1
  print(str(i) + "º")
  names.append(input("Qual o nome da " + str(i) + "º pessoa: "))
  heights.append(int(input("Qual a altura da " + str(i) + "º pessoa: ")))

print("\nA maior pessoa é: {} com {}cm".format(names[heights.index(max(heights))], max(heights)))

print("A menor pessoa é: {} com {}cm".format(names[heights.index(min(heights))], min(heights)))
