from abc import ABC, abstractmethod

# === Exceptions === 

class TitulacaoProfessorDoutor(Exception):
  pass

class IdadeMinimaProfessor(Exception):
  pass

class CursoObrigatorio(Exception):
  pass

class IdadeMinimaAluno(Exception):
  pass

class CPFExistente(Exception):
  pass

class Pessoa(ABC):
  def __init__(self, nome, endereco, idade, cpf):
    self.__nome = nome
    self.__endereco = endereco
    self.__idade = idade
    self.__cpf = cpf

  def getNome(self):
    return self.__nome

  def getEndereco(self):
    return self.__endereco
      
  def getIdade(self):
    return self.__idade
  
  def getCPF(self):
    return self.__cpf

  @abstractmethod
  def printDescricao(self):
    pass

class Aluno(Pessoa):
  def __init__(self, nome, endereco, idade,cpf, curso):
    super().__init__(nome, endereco, idade,cpf)
    self.__curso = curso

  def getCurso(self):
    return self.__curso

  def printDescricao(self):
    print(f"Nome: {self.getNome()}")
    print(f"Endereco: {self.getEndereco()}")
    print(f"Idade: {self.getIdade()}")
    print(f"Curso: {self.getCurso()}")

class Professor(Pessoa):
  def __init__(self, nome, endereco, idade,cpf, titulacao):
    super().__init__(nome, endereco, idade,cpf)
    self.__titulacao = titulacao

  def getTitulacao(self):
    return self.__titulacao

  def printDescricao(self):
    print(f"Nome: {self.getNome()}")
    print(f"Endereco: {self.getEndereco()}")
    print(f"Idade: {self.getIdade()}")
    print(f"Titulacao: {self.getTitulacao()}")

listaPessoas = [
  Aluno('Aluno 1','Centro, 001',33,'231.111.433-12','SIN'),            # Certo
  Aluno('Aluno 2','Centro, 002',44,'542.111.434-32','CCO'),            # Certo
  Professor('Professor 1','Centro, 003',22,'443.323.321-43','Mestre'), # Titulacao errada
  Aluno('Aluno 4','Centro, 004',66,'546.675.434-32','ECA'),            # Curso errado
  Aluno('Aluno 5','Centro, 005',44,'546.675.434-32','SIN'),            # Certo
  Professor('Professor 2','Centro, 006',30,'123.324.545-40','Doutor'), # Certo
  Professor('Professor 3','Centro, 007',24,'838.333.222-11','Doutor'), # Idade errada
  Aluno('Aluno 8','Centro, 008',16,'111.312.112-44','SIN')             # Idade errada
]

cadastro = []

for pessoa in listaPessoas:
  try:
    if isinstance(pessoa,Professor):
      if pessoa.getTitulacao() != 'Doutor':
        raise TitulacaoProfessorDoutor
      if pessoa.getIdade() < 30:
        raise IdadeMinimaProfessor

    elif isinstance(pessoa,Aluno):
      if pessoa.getIdade() < 18:
        raise IdadeMinimaAluno
      if str(pessoa.getCurso()) not in ['SIN', 'CCO']:
        raise CursoObrigatorio
                    
    for pessoaCadastrar in cadastro:
      if pessoaCadastrar.getCPF() in pessoa.getCPF():
        raise CPFExistente
              
    cadastro.append(pessoa)

  except TitulacaoProfessorDoutor:
    print("\nTodo professor deve possuir titulação de doutor" )
    pessoa.printDescricao()
    print()
  except IdadeMinimaProfessor:
    print("\nTodo professor deve ter ao menos 30 anos de idade")
    pessoa.printDescricao()
    print()
  except IdadeMinimaAluno:
    print("\nO aluno deve ter mais de 18 anos")
    pessoa.printDescricao()
    print()
  except CursoObrigatorio:
    print("\nAluno não cursa SIN ou CCO")
    pessoa.printDescricao()
    print()
  except CPFExistente:
    print("\nCPF já cadastrado")
    pessoa.printDescricao()
    print()

print("\n\nCadastro Geral:")

for pessoa in cadastro:
  pessoa.printDescricao()
  print()