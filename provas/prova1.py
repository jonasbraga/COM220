from abc import ABC, abstractmethod

class Funcionario(ABC):
  def __init__(self, codigo, nome):
    self.__codigo = codigo
    self.__nome = nome
    self.__pontoMensalFunc = []
    self.__bonusPontualidade = 0

  def getBonusPontualidade(self):
    return self.__bonusPontualidade

  def setBonusPontualidade(self, bonusPontualidade):
    self.__bonusPontualidade = bonusPontualidade

  def getNome(self):
    return self.__nome

  def getCodigo(self):
    return self.__codigo

  def adicionaPonto(self, mes, ano, faltas, atrasos):
    self.__pontoMensalFunc.append(PontoFunc(mes, ano, faltas, atrasos))
    return True

  def lancaFaltas(self, mes, ano, faltas):
    ponto = self._getPonto(mes, ano)
    ponto.lancaFaltas(faltas)

  def lancaAtrasos(self, mes, ano, atrasos):
    ponto = self._getPonto(mes, ano)
    ponto.lancaAtrasos(atrasos)

  def imprimeFolha(self, mes, ano):
    print("Código: {}".format(self.getCodigo()))
    print("Nome: {}".format(self.getNome()))
    print("Salário: {:.2f}".format(self.calculaSalario(mes, ano)))
    print("Bônus: {:.2f}".format(self.calculaBonus(mes, ano)))

  def _getPonto(self, mes, ano):
    for ponto in self.__pontoMensalFunc:
      if ponto.getMes() == mes and ponto.getAno() == ano :
        return ponto
    return False
    
  @abstractmethod
  def calculaSalario(self, mes, ano):
    pass

  @abstractmethod
  def calculaBonus(self, mes, ano):
    pass

class PontoFunc():
  def __init__(self, mes, ano, nroFaltas, nroAtrasos):    
    self.__mes = mes
    self.__ano = ano
    self.__nroFaltas = nroFaltas
    self.__nroAtrasos = nroAtrasos
    
  def getMes(self):
    return self.__mes

  def getAno(self):
    return self.__ano

  def getNroFaltas(self):
    return self.__nroFaltas

  def getNroAtrasos(self):
    return self.__nroAtrasos

  def lancaFaltas(self, nroFaltas):
    self.__nroFaltas = nroFaltas

  def lancaAtrasos(self, nroAtrasos):
    self.__nroAtrasos = nroAtrasos

class Professor(Funcionario):
  def __init__(self, codigo, nome, titulacao, salarioHora, nroAulas):
    super().__init__(codigo, nome)
    self.__salarioHora = salarioHora
    self.__titulacao = titulacao
    self.__nroAulas = nroAulas
    self.setBonusPontualidade(10)
    
  def getTitulacao(self):
    return self.__titulacao

  def getSalarioHora(self):
    return self.__salarioHora

  def getNroAulas(self):
    return self.__nroAulas

  def calculaSalario(self, mes, ano):
    return self.getSalarioHora() * self.getNroAulas() - self.getSalarioHora() * self._getPonto(mes, ano).getNroFaltas()
      
  def calculaBonus(self, mes, ano):
    if self._getPonto(mes, ano).getNroAtrasos() >= self.getBonusPontualidade() : 
      return 0
    return self.calculaSalario(mes, ano) * ((self.getBonusPontualidade() - self._getPonto(mes, ano).getNroAtrasos())/ 100)

class TecAdmin(Funcionario):
  def __init__(self, codigo, nome, funcao, salarioMensal):
    super().__init__(codigo, nome)
    self.__funcao = funcao
    self.__salarioMensal = salarioMensal
    self.setBonusPontualidade(8)

  def getFuncao(self):
    return self.__funcao

  def getSalarioMensal(self):
    return self.__salarioMensal
      
  def calculaSalario(self, mes, ano):
    return self.getSalarioMensal() - (self.getSalarioMensal() / 30) * self._getPonto(mes, ano).getNroFaltas()
      
  def calculaBonus(self, mes, ano):
    if self._getPonto(mes, ano).getNroAtrasos() >= self.getBonusPontualidade() : 
      return 0
    return self.calculaSalario(mes, ano) * ((self.getBonusPontualidade() - self._getPonto(mes, ano).getNroAtrasos())/ 100)

if __name__ == "__main__":
  funcionarios = []
  prof = Professor(1, "Joao", "Doutor", 45.35, 32)
  prof.adicionaPonto(4, 2021, 0, 0)
  prof.lancaFaltas(4, 2021, 2)
  prof.lancaAtrasos(4, 2021, 3)
  funcionarios.append(prof)
  tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
  tec.adicionaPonto(4, 2021, 0, 0)
  tec.lancaFaltas(4, 2021, 3)
  tec.lancaAtrasos(4, 2021, 4)
  funcionarios.append(tec)
  for func in funcionarios:
    func.imprimeFolha(4, 2021)
    print()