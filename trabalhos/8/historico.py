import tkinter as tk
from tkinter import messagebox
import operator
import pickle
import os

class Historico:
  def __init__(self, aluno, semestre, nota, disciplina):
    self.__aluno = aluno
    self.__semestre = semestre
    self.__nota = nota
    self.__disciplina = disciplina

  def getAluno(self):
    return self.__aluno
  
  def getSemestre(self):
    return self.__semestre

  def getNota(self):
    return self.__nota
  
  def getDisciplina(self):
    return self.__disciplina

class LimInsereHistorico(tk.Toplevel):
  def __init__(self, control):
    tk.Toplevel.__init__(self)
    self.title("Histórico")
    self.control = control

    self.frameAluno = tk.Frame(self)
    self.frameDisc = tk.Frame(self)
    self.frameSemestre = tk.Frame(self)
    self.frameNota = tk.Frame(self)
    self.frameBotao = tk.Frame(self)
    self.frameNota.pack()
    self.frameAluno.pack()
    self.frameDisc.pack()
    self.frameSemestre.pack()
    self.frameBotao.pack()

    self.labelAluno = tk.Label(self.frameAluno,text="Matrícula aluno: ")
    self.labelAluno.pack(side="left")
    self.inputAluno = tk.Entry(self.frameAluno, width=20)
    self.inputAluno.pack(side="left")

    self.labelDisciplina = tk.Label(self.frameDisc,text="Disciplina: ")
    self.labelDisciplina.pack(side="left")
    self.inputDisciplina = tk.Entry(self.frameDisc, width=20)
    self.inputDisciplina.pack(side="left") 

    self.labelSemestre = tk.Label(self.frameSemestre,text="Semestre: ")
    self.labelSemestre.pack(side="left")
    self.inputSemestre = tk.Entry(self.frameSemestre, width=20)
    self.inputSemestre.pack(side="left")

    self.labelNota = tk.Label(self.frameNota,text="Nota: ")
    self.labelNota.pack(side="left")  
    self.inputNota = tk.Entry(self.frameNota, width=20)
    self.inputNota.pack(side="left")             
  
    self.botaoCriar = tk.Button(self.frameBotao ,text="Inserir")      
    self.botaoCriar.pack(side="left")
    self.botaoCriar.bind("<Button>", control.criaHistorico)

    self.botaoFechar = tk.Button(self.frameBotao ,text="Concluído")      
    self.botaoFechar.pack(side="left")
    self.botaoFechar.bind("<Button>", control.fechar)

  def exibeJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

class LimExibeHistorico(tk.Toplevel):
  def __init__(self, control):
    tk.Toplevel.__init__(self)
    self.title("Histórico do Aluno")
    self.control = control

    self.frameAluno = tk.Frame(self)
    self.frameBotao = tk.Frame(self)

    self.frameAluno.pack()
    self.frameBotao.pack()

    self.labelAluno = tk.Label(self.frameAluno,text="Matrícula: ")
    self.labelAluno.pack(side="left")
    self.inputAluno = tk.Entry(self.frameAluno, width=20)
    self.inputAluno.pack(side="left")      
  
    self.botaoCriar = tk.Button(self.frameBotao ,text="Emitir histórico")      
    self.botaoCriar.pack(side="left")
    self.botaoCriar.bind("<Button>", control.mostraHistorico)
  
  def exibeJanela(self, msg):
    self.message = tk.Tk()
    self.message.title('Histórico do aluno')
    self.frame1 = tk.Frame(self.message)
    self.frame1.pack()
    self.frame2 = tk.Frame(self.message)
    self.frame2.pack()

    self.label = tk.Label(self.frame1, text = msg)
    self.label.pack()

    self.botao = tk.Button(self.frame2, text = 'Ok', command = lambda: self.message.destroy())
    self.botao.pack()

  def exibeJanela2(self, titulo, msg):
    messagebox.showinfo(titulo, msg)
  
class CtrlHistorico():
  def __init__(self, controlPrincipal):
    if not os.path.isfile("historico.pickle"):
      self.lista_historico = []
    else:
      with open("historico.pickle", "rb") as f:
        self.lista_historico = pickle.load(f)
    self.ctrlPrincipal = controlPrincipal

  def salvaHistoricos(self):
    if len(self.lista_historico) != 0:
      with open("historico.pickle", "wb") as f:
        pickle.dump(self.lista_historico, f)

  def getHistorico(self, matriculaAluno):
    historico = None
    for h in self.lista_historico:
      if h.getAluno().getMatriculaAluno == matriculaAluno:
        historico = h
    return historico

  def inserirHistorico(self):
    self.limiteIns = LimInsereHistorico(self) 

  def verificaCampoAluno(self, numeroMatricula):
    for aluno in self.ctrlPrincipal.ctrlAluno.getAlunos():
      if aluno.getMatriculaAluno() == numeroMatricula:
        return True
    return False

  def verificaCampoDisciplina(self, codigoDisciplina):
    for disciplina in self.ctrlPrincipal.ctrlDisciplina.getDisciplinas():
      if disciplina.getCodigo() == codigoDisciplina:
        return True
    return False
  
  def verificaHistorico(self, numeroMatricula):
    for historico in self.lista_historico:
      if historico.getAluno() == numeroMatricula:
        return True
    return False

  def historicoAluno(self):
    self.limiteMos = LimExibeHistorico(self) 

  def mostraHistorico(self, event):
    matricula = self.limiteMos.inputAluno.get()

    if not self.verificaCampoAluno(matricula):
      self.limiteMos.exibeJanela2('Erro', 'Aluno invalido')
    else:
      horasObrigatorias = 0
      elevetivas_horas = 0
      mensagem = 'Matrícula - Semestre - Nota - Disciplina - Resultado\n\n'

      for historico in self.lista_historico:
        obrigatoria = False
        cargaHorariaDisc = 0
        if historico.getAluno().getMatriculaAluno() == matricula:
          
          for disciplina in historico.getAluno().getCurso().getGrade().getDisciplinas():
            if historico.getDisciplina().getCodigo() == disciplina.getCodigo():
              obrigatoria = True
              cargaHorariaDisc = float(disciplina.getCargaHoraria())
          
          if obrigatoria:
            horasObrigatorias += cargaHorariaDisc
          else:
            elevetivas_horas += float(historico.getDisciplina().getCargaHoraria())

          mensagem += f"{historico.getAluno().getMatriculaAluno()} - {historico.getSemestre()} - {historico.getNota()} - {historico.getDisciplina().getCodigo()} - {'Aprovado' if float(historico.getNota()) >= 6.0 else 'Reprovado'}\n" 
          
      mensagem += '\nTotal obrigatória (horas): ' +str(horasObrigatorias)+ '\n'
      mensagem += 'Total eletiva (horas): ' +str(elevetivas_horas)+ '\n'
      self.limiteMos.exibeJanela(mensagem)

  def criaHistorico(self, event):
    alunoSelected = self.limiteIns.inputAluno.get()
    aluno = self.ctrlPrincipal.ctrlAluno.getAlunoMatricula(alunoSelected)
    nota = self.limiteIns.inputNota.get()
    semestre = self.limiteIns.inputSemestre.get()
    disciplinaSelecionada = self.limiteIns.inputDisciplina.get()
    disciplina = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(disciplinaSelecionada)
    validado = True

    if self.verificaHistorico(alunoSelected):
      self.limiteIns.exibeJanela('Erro', 'Aluno inserido já possui histórico')
    else:
      if not self.verificaCampoAluno(alunoSelected):
        self.limiteIns.exibeJanela('Erro', 'Número de matrícula inválido')
        validado = False
      
      if not self.verificaCampoDisciplina(disciplinaSelecionada):
        self.limiteIns.exibeJanela('Erro', 'Código de disciplina inválido')
        validado = False
      
      if len(alunoSelected) == 0 or len(disciplinaSelecionada) == 0 or len(nota) == 0 or len(semestre) == 0:
        self.limiteIns.exibeJanela('Erro', 'Todos os campos devem ser preenchidos')
        validado = False

      if validado:
        historico = Historico(aluno, semestre, nota, disciplina)
        self.lista_historico.append(historico)
        self.limiteIns.exibeJanela('Sucesso', 'Histórico cadastrado com sucesso')
  
    self.limiteIns.inputAluno.delete(0, len(self.limiteIns.inputAluno.get()))
    self.limiteIns.inputDisciplina.delete(0, len(self.limiteIns.inputDisciplina.get()))        
    self.limiteIns.inputNota.delete(0, len(self.limiteIns.inputNota.get()))
    self.limiteIns.inputSemestre.delete(0, len(self.limiteIns.inputSemestre.get()))

  def fechar(self, event):
    self.limiteIns.destroy()