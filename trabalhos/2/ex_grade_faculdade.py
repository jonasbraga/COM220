class Aluno:
  def __init__(self, nroMatricula, nome, curso):
    self.__nroMatricula = nroMatricula
    self.__nome = nome
    self.__curso = curso
    self.__disciplinas = []

  def getMatricula(self):
    return self.__nroMatricula

  def getNome(self):
    return self.__nome

  def getCurso(self):
    return self.__curso

  def getDisciplinas(self):
    return self.__disciplinas

  def adicionaDisciplina(self, disciplina):
    self.__disciplinas.append(disciplina)

class Curso:
  def __init__(self, nome, grade):
    self.__nome = nome
    self.__grade = grade
    self.__alunos = []
    self.__disciplinas = []

  def getNome(self):
    return self.__nome

  def getGrade(self):
    return self.__grade

  def getAlunos(self):
    return self.__alunos

  def adicionaAlunos(self, aluno):
    self.__alunos.append(aluno)

  def adicionaDisciplina(self, disciplina):
    self.__alunos.append(disciplina)


class Grade:
  def __init__(self, ano):
    self.__ano = ano
    self.__disciplinas = []

  def getAno(self):
    return self.__ano

  def getDisciplinas(self):
    return self.__disciplinas

  def adicionaDisciplinas(self, disciplina):
    self.__disciplinas.append(disciplina)


class Disciplina:
  def __init__(self, codigo, nome, cargaHoraria, grade):
    self.__codigo = codigo
    self.__nome = nome
    self.__cargaHoraria = cargaHoraria
    self.__grade = grade

  def getCodigo(self):
    return self.__codigo

  def getNome(self):
    return self.__nome

  def getCargaHoraria(self):
    return self.__cargaHoraria

  def getGrade(self):
    return self.__grade

class Historico:
  def __init__(self, aluno):
    self.__aluno = aluno

  def getAluno(self):
    return self.__aluno

  def getHistorico(self):
    aluno = self.getAluno()
    print(f"Nome - {aluno.getNome()}")
    print(f"Curso - {aluno.getCurso().getNome()}")

    disciplinasAluno = aluno.getDisciplinas()
    cargaObrigatoria = 0
    cargaEletiva = 0

    for disciplina in disciplinasAluno:
      if(aluno.getCurso().getGrade() == disciplina.getGrade()) : 
        print(f"{disciplina.getNome()} - Obrigatória")
        cargaObrigatoria += disciplina.getCargaHoraria()
      else:
        print(f"{disciplina.getNome()} - Eletiva")
        cargaEletiva += disciplina.getCargaHoraria()

    print(f"Carga horária obrigatória cursada: {cargaObrigatoria}")
    print(f"Carga horária eletiva cursada: {cargaEletiva}")

if __name__ == "__main__":
  grades = [
    Grade(2019),
    Grade(2018)
  ]

  cursos = [
    Curso('SIN', grades[0]),
    Curso('CCO', grades[1])
  ]

  disciplinasGrade2019 = [
    Disciplina(170, 'COM220', 90, grades[0]),
    Disciplina(110, 'COM112', 90, grades[0])
  ]

  disciplinasGrade2018 = [
    Disciplina(170, 'SIN310', 90, grades[1]),
    Disciplina(110, 'COM110', 90, grades[1])
  ]
  grades[0].adicionaDisciplinas(disciplinasGrade2019[0])
  grades[0].adicionaDisciplinas(disciplinasGrade2019[1])
  grades[1].adicionaDisciplinas(disciplinasGrade2018[0])
  grades[1].adicionaDisciplinas(disciplinasGrade2018[1])

  alunos = [
    Aluno(1, 'Jonas', cursos[0]),
    Aluno(2, 'Braga', cursos[1])
  ]

  alunos[0].adicionaDisciplina(disciplinasGrade2019[0])
  alunos[0].adicionaDisciplina(disciplinasGrade2018[0])

  alunos[1].adicionaDisciplina(disciplinasGrade2019[1])
  alunos[1].adicionaDisciplina(disciplinasGrade2018[1])

  historico = Historico(alunos[0])
  historico.getHistorico()