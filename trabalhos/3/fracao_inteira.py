def mdc(m, n):
  while m%n != 0:
    oldm = m
    oldn = n
    m = oldn
    n = oldm%oldn
  return n

class Fracao:
  def __init__(self, num, den):
    self.__num = num        
    self.__den = den     

  def __str__(self):
    return str(self.__num) + "/" + str(self.__den)

  def getNum(self):
    return self.__num

  def getDen(self):
    return self.__den

  def simplifica(self):
    divComum = mdc(self.__num, self.__den)
    self.__num = self.__num // divComum
    self.__den = self.__den // divComum   

  def __add__(self,outraFrac):
    novoNum = self.__num * outraFrac.getDen() + self.__den * outraFrac.getNum()
    novoDen = self.__den * outraFrac.getDen()
    divComum = mdc(novoNum, novoDen)
    return Fracao(novoNum//divComum, novoDen//divComum)        

class FracaoInteira(Fracao):
  def __init__(self, num, den, inteiro = 0):
    super().__init__(num, den)
    self.__int = inteiro
    
  def __str__(self):
    if(not self.getDen() and not self.getNum()):
      return f"{self.__int}" 
    else:
      return f"{self.__int if self.__int else ''} {super().__str__()}" 

  def __add__(self, outraFrac):
    resultSoma = super().__add__(outraFrac)
    parteInteira = resultSoma.getNum() // resultSoma.getDen()
    resto = resultSoma.getNum() % resultSoma.getDen()
    if(resto):
      novoNum = resultSoma.getNum() - (parteInteira * resultSoma.getDen())
      return FracaoInteira(novoNum, resultSoma.getDen(), parteInteira + outraFrac.getInt() + self.getInt())
    else:
      return FracaoInteira(0, 0, parteInteira + outraFrac.getInt() + self.getInt())

  def getInt(self):
    return self.__int
    
if __name__ == "__main__":
  frac1 = FracaoInteira(7, 6) 
  frac2 = FracaoInteira(13, 7)
  frac3 = frac1 + frac2
  print(frac3)
  print()
  frac1 = FracaoInteira (1, 3)
  frac2 = FracaoInteira(2, 3)
  frac3 = frac1 + frac2
  print(frac3)
  print()
  frac1 = FracaoInteira (1, 2, 3)
  frac2 = FracaoInteira(2, 3, 4)
  frac3 = frac1 + frac2
  print(frac3)