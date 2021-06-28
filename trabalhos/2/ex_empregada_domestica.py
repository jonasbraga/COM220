from abc import ABC, abstractmethod

class EmpDomestica(ABC):
  def __init__(self, nome, telefone):
    self.__nome = nome
    self.__telefone = telefone

  def getNome(self):
    return self.__nome

  def getTelefone(self):
    return self.__telefone

  def setNome(self, nome):
    self.__nome = nome

  def setTelefone(self, telefone):
    self.__telefone = telefone

  @abstractmethod
  def getSalario(self):
    pass

class EmpHorista(EmpDomestica):
  def __init__(self, nome, telefone, valorPorHora, horasTrabalhadas):
    super().__init__(nome, telefone)
    self.__horasTrabalhadas = horasTrabalhadas
    self.__valorPorHora = valorPorHora

  def getSalario(self):
    return self.__valorPorHora * self.__horasTrabalhadas

class EmpDiarista(EmpDomestica):
  def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
    super().__init__(nome, telefone)
    self.__diasTrabalhados = diasTrabalhados
    self.__valorPorDia = valorPorDia

  def getSalario(self):
    return self.__valorPorDia * self.__diasTrabalhados

class EmpMensalista(EmpDomestica):
  def __init__(self, nome, telefone, valorMensal):
    super().__init__(nome, telefone)
    self.__valorMensal = valorMensal

  def getSalario(self):
    return self.__valorMensal


if __name__ == "__main__":
  empregadas = [
    EmpHorista('Carolina', '(18)94516-5416', 10, 160),
    EmpDiarista('Karen', '(35)92863-8321', 20, 55),
    EmpMensalista('Rafaela', '(12)95463-3485', 1000)
  ]
  
  menorSalario = empregadas[0].getSalario()

  for empregada in empregadas:
    print('\nNome: {}'.format(empregada.getNome()))
    print('Salário: R${:.2f}'.format(empregada.getSalario()))
    
    if(empregada.getSalario() < menorSalario):
      menorSalario = empregada.getSalario()
      menorSalarioTel = empregada.getTelefone()
      menorSalarioNome = empregada.getNome()

  print('\nA empregada que possui o salário mais baixo é a {} sendo R${:.2f} por mês. Telefone: {}.'.format(
    menorSalarioNome, float(menorSalario), menorSalarioTel))