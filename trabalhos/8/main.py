import tkinter as tk
from tkinter import messagebox
import aluno as a
import disciplina as d
import grade as g
import historico as h
import curso as c

class LimPrincipal():

  def __init__(self, root, control):
    self.control = control
    self.root = root
    self.root.geometry('500x300')
    self.menubar = tk.Menu(self.root)        
    self.alunoMenu = tk.Menu(self.menubar)
    self.discipMenu = tk.Menu(self.menubar)
    self.cursoMenu = tk.Menu(self.menubar)
    self.gradeMenu = tk.Menu(self.menubar)
    self.histMenu = tk.Menu(self.menubar) 
    self.salvarMenu = tk.Menu(self.menubar)

    self.menubar.add_cascade(label="Aluno", menu=self.alunoMenu)
    self.alunoMenu.add_command(label="Adicionar", command=self.control.inserirAlunos)
    self.alunoMenu.add_command(label="Exibir", command=self.control.mostrarAlunos)

    self.menubar.add_cascade(label="Disciplina", menu=self.discipMenu)  
    self.discipMenu.add_command(label="Adicionar", command=self.control.inserirDisciplinas)
    self.discipMenu.add_command(label="Exibir", command=self.control.mostrarDisciplinas)            

    self.menubar.add_cascade(label="Curso", menu=self.cursoMenu) 
    self.cursoMenu.add_command(label="Adicionar", command=self.control.inserirCurso)
    self.cursoMenu.add_command(label="Exibir", command=self.control.mostrarCursos)  

    self.menubar.add_cascade(label="Grade", menu=self.gradeMenu)
    self.gradeMenu.add_command(label="Adicionar", command=self.control.inserirGrade)
    self.gradeMenu.add_command(label="Exibir", command=self.control.mostrarGrades)        

    self.menubar.add_cascade(label="Histórico", menu=self.histMenu)
    self.histMenu.add_command(label="Adicionar", command=self.control.inserirHistorico)
    self.histMenu.add_command(label="Exibir", command=self.control.exibirHistorico)        

    self.menubar.add_cascade(label="Salvar", menu=self.salvarMenu)
    self.salvarMenu.add_command(label="Salvar", command=self.control.salvaDados)

    self.root.config(menu=self.menubar)
    
class ControlPrincipal():   

  def __init__(self):
    self.root = tk.Tk()
    self.ctrlGrade = g.CtrlGrade(self)
    self.ctrlCurso = c.CtrlCurso(self)
    self.ctrlHistorico = h.CtrlHistorico(self)
    self.limite = LimPrincipal(self.root, self) 
    self.ctrlAluno = a.CtrlAluno(self)
    self.ctrlDisciplina = d.CtrlDisciplina()
    self.root.title("Trabalho 12")
    self.root.mainloop()
  
#Trigger funções do aluno
  def mostrarAlunos(self):
    self.ctrlAluno.mostrarAlunos()    
  def inserirAlunos(self):
    self.ctrlAluno.inserirAlunos()

#Trigger funções da grade
  def inserirGrade(self):
    self.ctrlGrade.inserirGrade()

  def mostrarGrades(self):
    self.ctrlGrade.mostrarGrades()

#Trigger funções do histórico
  def inserirHistorico(self):
    self.ctrlHistorico.inserirHistorico()

  def exibirHistorico(self):
    self.ctrlHistorico.historicoAluno()

#Trigger funções da disciplina
  def inserirDisciplinas(self):
    self.ctrlDisciplina.inserirDisciplina()

  def mostrarDisciplinas(self):
    self.ctrlDisciplina.mostrarDisciplinas()

#Trigger funções do curso
  def inserirCurso(self):
    self.ctrlCurso.inserirCurso()

  def mostrarCursos(self):
    self.ctrlCurso.mostrarCursos()

#Persistencia em todas as classes
  def salvaDados(self):
    self.ctrlHistorico.salvaHistoricos()
    self.ctrlCurso.salvaCurso()
    self.ctrlDisciplina.salvaDisciplinas()
    self.ctrlAluno.salvaAlunos()
    self.ctrlGrade.salvaGrades()

if __name__ == '__main__':
  App = ControlPrincipal()