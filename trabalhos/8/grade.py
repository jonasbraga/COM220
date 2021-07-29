import tkinter as tk
from tkinter import messagebox
import pickle
import os

class Grade:
  def __init__(self, ano, disciplinas):
    self.__ano = ano
    self.__disciplinas = disciplinas

  def getAno(self):
    return self.__ano
  
  def getDisciplinas(self):
    return self.__disciplinas

class LimInsereGrades(tk.Toplevel):
  def __init__(self, control):
    tk.Toplevel.__init__(self)
    self.title("Grade")
    self.control = control
    self.frameAno = tk.Frame(self)
    self.frameDisc = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameAno.pack()
    self.frameDisc.pack()
    self.frameButton.pack()
    self.labelDisc = tk.Label(self.frameDisc,text="Escolha a disciplina: ")
    self.labelDisc.pack(side="left") 
    self.inputDisc = tk.Entry(self.frameDisc, width=20)
    self.inputDisc.pack(side="left")
    self.labelAno = tk.Label(self.frameAno, text="Ano: ")
    self.labelAno.pack(side="left")
    self.inputAno = tk.Entry(self.frameAno, width=20)
    self.inputAno.pack(side="left")
    self.buttonInsere = tk.Button(self.frameButton, text="Inserir disciplina")      
    self.buttonInsere.pack(side="left")
    self.buttonInsere.bind("<Button>", control.insereDisciplinas)
    self.buttonCria = tk.Button(self.frameButton, text="Cria grade")      
    self.buttonCria.pack(side="left")
    self.buttonCria.bind("<Button>", control.criaGrade)
    self.buttonCria = tk.Button(self.frameButton, text="Concluído")      
    self.buttonCria.pack(side="left")
    self.buttonCria.bind("<Button>", control.fechar)  

  def exibeJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

class LimExibeGrades():
  def __init__(self, str):
    self.message = tk.Tk()
    self.message.title('Lista de Grades')
    self.frame1 = tk.Frame(self.message)
    self.frame1.pack()
    self.frame2 = tk.Frame(self.message)
    self.frame2.pack()

    self.label = tk.Label(self.frame1, text = str)
    self.label.pack()

    self.botao = tk.Button(self.frame2, text = 'Ok', command = lambda: self.message.destroy())
    self.botao.pack()

class CtrlGrade():
  def __init__(self, controlPrincipal):
    if not os.path.isfile("grade.pickle"):
      self.lista_grades = []
    else:
      with open("grade.pickle", "rb") as f:
        self.lista_grades = pickle.load(f)
    self.ctrlPrincipal = controlPrincipal
    self.disciplinasGrade = []

  def getGrades(self):
    return self.lista_grades

  def salvaGrades(self):
    if len(self.lista_grades) != 0:
        with open("grade.pickle", "wb") as f:
            pickle.dump(self.lista_grades, f)

  def verifGrade(self, ano):
    for grade in self.lista_grades:
      if grade.getAno() == ano:
        return True
    return False

  def verificaDisciplina(self, codigo_disciplina):
    listaDisciplinas = self.ctrlPrincipal.ctrlDisciplina.getDisciplinas()
    for disciplina in listaDisciplinas:
      if disciplina.getCodigo() == codigo_disciplina:
        return True
    return False

  def criaGrade(self, event):
    ano = self.limiteIns.inputAno.get()
    if self.verifGrade(ano):
      self.limiteIns.exibeJanela('Erro', 'Já existe uma grade com esse ano')
    else:
      if len(ano) == 0 or len(self.disciplinasGrade) == 0:
        self.limiteIns.exibeJanela('Erro', 'Todos os campos devem ser preenchidos')
      else:
        grade = Grade(ano, self.disciplinasGrade)
        self.limiteIns.exibeJanela('Sucesso', 'Grade criada com sucesso')
        self.lista_grades.append(grade)
        self.limiteIns.inputDisc.delete(0, len(self.limiteIns.inputDisc.get()))
        self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))
  
  def getGrade(self, gradeAno):
    grade = None
    for g in self.lista_grades:
      if g.getAno() == gradeAno:
        grade = g
    return grade

  def inserirGrade(self):
    self.disciplinasGrade = []
    self.limiteIns = LimInsereGrades(self)

  def insereDisciplinas(self, event):
    cod_disciplina = self.limiteIns.inputDisc.get()
    if len(cod_disciplina) == 0:
      self.limiteIns.exibeJanela('Erro', 'O campo de disciplina deve ser preenchido')
    else:
      if not self.verificaDisciplina(cod_disciplina):
        self.limiteIns.exibeJanela('Erro', 'Código de disciplina inválido')
      else:
        disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(cod_disciplina)
        self.disciplinasGrade.append(disciplina)
        self.limiteIns.exibeJanela('Sucesso', 'Disciplina inserida')
        self.limiteIns.inputDisc.delete(0, len(self.limiteIns.inputDisc.get()))

  def mostrarGrades(self):
    mensagem = ''
      
    for grade in self.lista_grades:
      mensagem += f"Ano da grade: {grade.getAno()}\n"
      for disciplina in grade.getDisciplinas():
        mensagem += f"\n{disciplina.getCodigo()} - {disciplina.getNome()} - {disciplina.getCargaHoraria()}"
      mensagem += '\n================================================\n\n'
    self.limiteIns = LimExibeGrades(mensagem)
  
  def fechar(self, event):
    self.limiteIns.destroy()