# Trazer a média dos números inseridos em uma lista

numbersList = []

while True:
  num = int(input("Digite um número: "))
  if num == 0:
    break
  numbersList.append(num)

totalSum = 0

for number in numbersList:
  print(number)
  totalSum += number

media = totalSum / len(numbersList)

print("A média dos números digitados é: " + str(media))