import tkinter as tk
from tkinter import messagebox
import pickle
import os

class Disciplina:
  def __init__(self, codigo, nome, cargaHoraria):
    self.__codigo = codigo
    self.__nome = nome
    self.__cargaHoraria = cargaHoraria

  def getCodigo(self):
    return self.__codigo
  
  def getNome(self):
    return self.__nome
  
  def getCargaHoraria(self):
    return self.__cargaHoraria

class LimInsereDisciplinas(tk.Toplevel):
  def __init__(self, control):
    tk.Toplevel.__init__(self)
    self.title("Disciplina")
    self.control = control

    self.frameCargaHor = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameNome = tk.Frame(self)
    self.frameCod = tk.Frame(self)
    self.frameCod.pack()
    self.frameNome.pack()
    self.frameCargaHor.pack()
    self.frameButton.pack()

    self.labelCargaHr = tk.Label(self.frameCargaHor,text="Carga horária: ")
    self.labelCargaHr.pack(side="left")
    self.inputCargaHr = tk.Entry(self.frameCargaHor, width=20)
    self.inputCargaHr.pack(side="left")  

    self.labelCod = tk.Label(self.frameCod,text="Código: ")
    self.labelCod.pack(side="left")
    self.inputCod = tk.Entry(self.frameCod, width=20)
    self.inputCod.pack(side="left")

    self.labelNome = tk.Label(self.frameNome,text="Nome: ")
    self.labelNome.pack(side="left")
    self.inputNome = tk.Entry(self.frameNome, width=20)
    self.inputNome.pack(side="left")          
  
    self.botaoInserir = tk.Button(self.frameButton ,text="Inserir")      
    self.botaoInserir.pack(side="left")
    self.botaoInserir.bind("<Button>", control.criaDisciplina)

    self.botaoFechar = tk.Button(self.frameButton ,text="Concluído")      
    self.botaoFechar.pack(side="left")
    self.botaoFechar.bind("<Button>", control.fechar)

  def exibeJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

class LimExibeDisciplinas():
  def __init__(self, str):
    self.message = tk.Tk()
    self.message.title('Lista de Disciplinas')
    self.frame1 = tk.Frame(self.message)
    self.frame1.pack()
    self.frame2 = tk.Frame(self.message)
    self.frame2.pack()

    self.label = tk.Label(self.frame1, text = str)
    self.label.pack()

    self.botao = tk.Button(self.frame2, text = 'Ok', command = lambda: self.message.destroy())
    self.botao.pack()
  
class CtrlDisciplina():
  def __init__(self):
    if not os.path.isfile("disciplina.pickle"):
      self.lista_disciplinas = []
    else:
      with open("disciplina.pickle", "rb") as f:
        self.lista_disciplinas = pickle.load(f)

  def salvaDisciplinas(self):
    if len(self.lista_disciplinas) != 0:
      with open("disciplina.pickle", "wb") as f:
        pickle.dump(self.lista_disciplinas, f)

  def getDisciplinas(self):
    return self.lista_disciplinas

  def verificaDisciplina(self, codigo_disciplina):
    for disciplina in self.lista_disciplinas:
      if disciplina.getCodigo() == codigo_disciplina:
        return True
    return False    

  def getDisciplina(self, codigo_disciplina):
    disciplina = None
    for d in self.lista_disciplinas:
      if d.getCodigo() == codigo_disciplina:
        disciplina = d
    return disciplina

  def inserirDisciplina(self):
    self.limiteIns = LimInsereDisciplinas(self) 

  def mostrarDisciplinas(self):
    mensagem = 'Código | Nome | Carga Horária\n'

    for disciplina in self.lista_disciplinas:
      mensagem += '\n' + disciplina.getCodigo() + ' - ' + disciplina.getNome() + ' - ' + disciplina.getCargaHoraria()
    self.limiteLista = LimExibeDisciplinas(mensagem)

  def criaDisciplina(self, event):
    carga_horaria = self.limiteIns.inputCargaHr.get()
    codigo_disciplina = self.limiteIns.inputCod.get()
    nome_disciplina = self.limiteIns.inputNome.get()

    if self.verificaDisciplina(codigo_disciplina):
      self.limiteIns.exibeJanela('Erro', 'Disciplina já existente com esse código')
    else:
      if len(codigo_disciplina) == 0 or len(nome_disciplina) == 0 or len(carga_horaria) == 0:
        self.limiteIns.exibeJanela('Erro', 'Todos os campos devem ser preenchidos')
      else:
        disciplina = Disciplina(codigo_disciplina, nome_disciplina, carga_horaria)
        self.lista_disciplinas.append(disciplina)
        self.limiteIns.exibeJanela('Sucesso', 'Disciplina cadastrada!')
        self.limiteIns.inputCod.delete(0, len(self.limiteIns.inputCod.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputCargaHr.delete(0, len(self.limiteIns.inputCargaHr.get()))

  def fechar(self, event):
    self.limiteIns.destroy()