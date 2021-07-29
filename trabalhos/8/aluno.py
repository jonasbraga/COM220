import tkinter as tk
from tkinter import messagebox
import pickle
import os

class Aluno:
  def __init__(self, matriculaAluno, nome, curso):
    self.__matriculaAluno = matriculaAluno
    self.__nome = nome
    self.__curso = curso

  def getMatriculaAluno(self):
    return self.__matriculaAluno
  
  def getNome(self):
    return self.__nome

  def getCurso(self):
    return self.__curso

class LimInsereAlunos(tk.Toplevel):
  def __init__(self, control):
    tk.Toplevel.__init__(self)
    self.title("Aluno")
    self.control = control

    self.frameMatricula = tk.Frame(self)
    self.frameBotao = tk.Frame(self)
    self.frameCurso = tk.Frame(self)
    self.frameNomeAluno = tk.Frame(self)
    
    self.frameMatricula.pack()
    self.frameNomeAluno.pack()
    self.frameCurso.pack()
    self.frameBotao.pack()
  
    self.labelMatricula = tk.Label(self.frameMatricula,text="Matrícula: ")
    self.labelMatricula.pack(side="left")
    self.inputMatricula = tk.Entry(self.frameMatricula, width=20)
    self.inputMatricula.pack(side="left")

    self.labelNome = tk.Label(self.frameNomeAluno,text="Nome: ")
    self.labelNome.pack(side="left")  
    self.inputNome = tk.Entry(self.frameNomeAluno, width=20)
    self.inputNome.pack(side="left") 

    self.labelCurso = tk.Label(self.frameCurso,text="Curso: ")
    self.labelCurso.pack(side="left")
    self.inputCurso = tk.Entry(self.frameCurso, width=20)
    self.inputCurso.pack(side="left") 

    self.buttonSubmit = tk.Button(self.frameBotao ,text="Adicionar")      
    self.buttonSubmit.pack(side="left")
    self.buttonSubmit.bind("<Button>", control.criaAluno)

    self.buttonFecha = tk.Button(self.frameBotao ,text="Concluído")      
    self.buttonFecha.pack(side="left")
    self.buttonFecha.bind("<Button>", control.fechar)

  def exibeJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

class LimExibeAlunos():
  def __init__(self, str):
    messagebox.showinfo('Lista de alunos', str)

class CtrlAluno():     
  def __init__(self, controlPrincipal):
    if not os.path.isfile("aluno.pickle"):
      self.listaAlunos = []
    else:
      with open("aluno.pickle", "rb") as f:
        self.listaAlunos = pickle.load(f)
    
    self.ctrlPrincipal = controlPrincipal

  def salvaAlunos(self):
    if len(self.listaAlunos) != 0:
      with open("aluno.pickle", "wb") as f:
        pickle.dump(self.listaAlunos, f)

  def getAlunos(self):
    return self.listaAlunos

  def inserirAlunos(self):
    self.limiteIns = LimInsereAlunos(self) 

  def verificaAluno(self, matriculaAluno):
    for aluno in self.listaAlunos:
      if aluno.getMatriculaAluno() == matriculaAluno:
        return True
    return False

  def getAluno(self, matriculaAluno):
    aluno = None
    for a in self.listaAlunos:
      if a.getMatriculaAluno() == matriculaAluno:
        aluno = a
    return aluno

  def verifCurso(self, nomeCurso):
    listaCursos = []
    listaCursos = self.ctrlPrincipal.ctrlCurso.getCursos()
    for curso in listaCursos:
      if curso.getNome() == nomeCurso:
        return True
    return False

  def mostrarAlunos(self):
    mensagem = 'Matrícula - Nome - Curso\n'
    for est in self.listaAlunos:
      mensagem += f"\n {est.getMatriculaAluno()} - {est.getNome()} - {est.getCurso().getNome()}"
    self.limiteLista = LimExibeAlunos(mensagem)

  def getAlunoMatricula(self, matricula):
    discRet = None
    print('aqui dentro', matricula)
    for aluno in self.listaAlunos:
      print(aluno.getNroMatric())
      if aluno.getNroMatric() == matricula:
        discRet = aluno
      print("matricula",discRet)
    return discRet

  def criaAluno(self, event):
    curso_selecionado = self.limiteIns.inputCurso.get()
    curso = self.ctrlPrincipal.ctrlCurso.getCurso(curso_selecionado)
    matriculaAluno = self.limiteIns.inputMatricula.get()
    nome = self.limiteIns.inputNome.get()
    aluno = Aluno(matriculaAluno, nome, curso)

    if self.verificaAluno(matriculaAluno):
      self.limiteIns.exibeJanela('Erro', 'Aluno já cadastrado com esse numero de matricula')
    else:
      if len(matriculaAluno) == 0 or len(nome) == 0 or len(curso_selecionado) == 0:
        self.limiteIns.exibeJanela('Erro', 'Todos os campos devem ser preenchidos')
      else:
        if not self.verifCurso(curso_selecionado):
          self.limiteIns.exibeJanela('Erro', 'Curso inválido')
        else:
          self.listaAlunos.append(aluno)
          self.limiteIns.exibeJanela('Sucesso', 'Aluno cadastrado corretamente')
          self.limiteIns.inputMatricula.delete(0, len(self.limiteIns.inputMatricula.get()))
          self.limiteIns.inputCurso.delete(0, len(self.limiteIns.inputCurso.get()))                    
          self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
  def fechar(self, event):
    self.limiteIns.destroy()
  