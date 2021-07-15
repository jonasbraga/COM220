import tkinter as tk
from tkinter import messagebox

class ModelCliente():
  def __init__(self, nome, email):
    self.__nome = nome
    self.__email = email
    
  def getNome(self):
    return self.__nome

  def getEmail(self):
    return self.__email

class View():
  def __init__(self, master, controller):
    self.controller = controller
    self.janela = tk.Frame(master)
    self.janela.pack()
    self.frame1 = tk.Frame(self.janela)
    self.frame2 = tk.Frame(self.janela)
    self.frame1.pack()
    self.frame2.pack()
  
    self.labelInfo1 = tk.Label(self.frame1,text="Nome: ")
    self.labelInfo2 = tk.Label(self.frame2,text="Email: ")
    self.labelInfo1.pack(side="left")
    self.labelInfo2.pack(side="left")  

    self.inputText1 = tk.Entry(self.frame1, width=20)
    self.inputText1.pack(side="left")
    self.inputText2 = tk.Entry(self.frame2, width=20)
    self.inputText2.pack(side="left")             
  
    self.buttonSubmit = tk.Button(self.janela,text="Enter")      
    self.buttonSubmit.pack(side="left")
    self.buttonSubmit.bind("<Button>", controller.enterHandler)
  
    self.buttonClear = tk.Button(self.janela,text="Clear")      
    self.buttonClear.pack(side="left")
    self.buttonClear.bind("<Button>", controller.clearHandler)  

    # Ex2: Acrescentar o botão para listar os clientes cadastrados           

  def mostraJanela(self, titulo, mensagem):
    messagebox.showinfo(titulo, mensagem)
    
class Controller():       
  def __init__(self):
    self.root = tk.Tk()
    self.root.geometry('500x200')
    self.listaClientes = []

    # Cria a view passando referência da janela principal e
    # de si próprio (controlador)
    self.view = View(self.root, self) 

    self.root.title("Exemplo MVC")
    # Inicia o mainloop
    self.root.mainloop()

  def enterHandler(self, event):
    nomeCli = self.view.inputText1.get()
    emailCli = self.view.inputText2.get()
    cliente = ModelCliente(nomeCli, emailCli)
    self.listaClientes.append(cliente)
    self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
    self.clearHandler(event)

  def clearHandler(self, event):
    self.view.inputText1.delete(0, len(self.view.inputText1.get()))
    self.view.inputText2.delete(0, len(self.view.inputText2.get()))
    
  # Ex2: implementar função para listar os clientes cadastrados
  # def clientesHandler(self, event):

if __name__ == '__main__':
  c = Controller()