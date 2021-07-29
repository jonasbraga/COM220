import tkinter as tk
from tkinter import messagebox
import os
import pickle

class Curso:
  def __init__(self, nome, grade):
    self.__nome = nome
    self.__grade = grade

  def getNome(self):
    return self.__nome
  
  def getGrade(self):
    return self.__grade

class LimAddCurso(tk.Toplevel):
  def __init__(self, control):
    tk.Toplevel.__init__(self)
    self.title("Curso")
    self.control = control

    self.frameGrade = tk.Frame(self)
    self.frameBotao = tk.Frame(self)
    self.frameNomeCurso = tk.Frame(self)
    self.frameNomeCurso.pack()
    self.frameGrade.pack()
    self.frameBotao.pack()
  
    self.labelNome = tk.Label(self.frameNomeCurso,text="Nome: ")
    self.labelNome.pack(side="left")  
    self.inputNome = tk.Entry(self.frameNomeCurso, width=20)
    self.inputNome.pack(side="left")             
    self.labelGrades = tk.Label(self.frameGrade,text="Grade: ")
    self.labelGrades.pack(side="left")  
    self.inputGrade = tk.Entry(self.frameGrade, width=20)
    self.inputGrade.pack(side="left")  

    self.botaoFechar = tk.Button(self.frameBotao ,text="Concluído")      
    self.botaoFechar.pack(side="left")
    self.botaoFechar.bind("<Button>", control.fechar)
    self.botaoCriar = tk.Button(self.frameBotao ,text="Criar curso")      
    self.botaoCriar.pack(side="left")
    self.botaoCriar.bind("<Button>", control.criaCurso) 

  def exibeJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

class LimExibeCurso():
  def __init__(self, str):
    messagebox.showinfo('Lista de cursos', str)
  
class CtrlCurso():
  def __init__(self, controlPrincipal):
    if not os.path.isfile("curso.pickle"):
      self.lista_cursos = []
    else:
      with open("curso.pickle", "rb") as f:
        self.lista_cursos = pickle.load(f)

    self.ctrlPrincipal = controlPrincipal

  def salvaCurso(self):
    if len(self.lista_cursos) != 0:
      with open("curso.pickle", "wb") as f:
        pickle.dump(self.lista_cursos, f)

  def inserirCurso(self):
    self.limiteIns = LimAddCurso(self)

  def verifCurso(self, nome_curso): 
    for curso in self.lista_cursos:
      if curso.getNome() == nome_curso:
        return True
    return False

  def verifGrade(self, anoGrade):
    for grade in self.ctrlPrincipal.ctrlGrade.getGrades():
      if grade.getAno() == anoGrade:
        return True
    return False

  def verifGradeDisponivel(self, anoGrade):    
    for curso in self.lista_cursos:
      if curso.getGrade().getAno() == anoGrade:
        return True
    return False

  def criaCurso(self, event):
    gradeSelecionada = self.limiteIns.inputGrade.get()
    grade = self.ctrlPrincipal.ctrlGrade.getGrade(gradeSelecionada)
    nome = self.limiteIns.inputNome.get()

    if self.verifCurso(nome):       
      self.limiteIns.exibeJanela('Erro', 'Curso já existente com este nome')
    else:          
      if len(nome) == 0 or len(gradeSelecionada) == 0:
        self.limiteIns.exibeJanela('Erro', 'Todos os campos devem ser preenchidos')
      else:
        if not self.verifGrade(gradeSelecionada):
          self.limiteIns.exibeJanela('Erro', 'Grade inválida')
        else:
          if self.verifGradeDisponivel(gradeSelecionada):
            self.limiteIns.exibeJanela('Erro', 'Grade já utilizada')
          else:
            curso = Curso(nome, grade)
            self.lista_cursos.append(curso)
            self.limiteIns.exibeJanela('Sucesso', 'Curso criado com sucesso')
            self.limiteIns.inputGrade.delete(0, len(self.limiteIns.inputGrade.get()))                        
            self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
          
  def getCurso(self, nome):
    cursoRet = None
    for curso in self.lista_cursos:
      if curso.getNome() == nome:
        cursoRet = curso
    return cursoRet

  def getCursos(self):
    return self.lista_cursos

  def mostrarCursos(self):
    mensagem = 'Curso / Grade\n'
    for curso in self.lista_cursos:
      mensagem += '\n' + curso.getNome() + " " + curso.getGrade().getAno()
    self.limiteIns = LimExibeCurso(mensagem)

  def fechar(self, event):
    self.limiteIns.destroy()