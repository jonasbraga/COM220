import tkinter as tk
from tkinter import messagebox

class ModelCliente():
  def __init__(self, nome, email, codigo):
    self.__nome = nome
    self.__email = email
    self.__codigo = codigo

  def getNome(self):
    return self.__nome

  def getEmail(self):
    return self.__email

  def getCodigo(self):
    return self.__codigo

class View():
  def __init__(self, master, controller):
    self.controller = controller
    self.janela = tk.Frame(master)
    self.janela.pack()
    self.frame0_1 = tk.Frame(self.janela)
    self.frame1 = tk.Frame(self.janela)
    self.frame2 = tk.Frame(self.janela)
    self.frame3 = tk.Frame(self.janela)
    self.frame3_1 = tk.Frame(self.janela)
    self.frame4_1 = tk.Frame(self.janela)
    self.frame4 = tk.Frame(self.janela)
    self.frame0_1.pack()
    self.frame1.pack()
    self.frame2.pack()
    self.frame3.pack()
    self.frame3_1.pack()
    self.frame4_1.pack()
    self.frame4.pack()
  
    self.labelInfo0 = tk.Label(self.frame0_1,text="Cadastro de Clientes")
    self.labelInfo1 = tk.Label(self.frame1,text="Nome: ")
    self.labelInfo2 = tk.Label(self.frame2,text="Email: ")
    self.labelInfo3 = tk.Label(self.frame3,text="Código: ")
    self.labelInfo0.pack(side="left")
    self.labelInfo1.pack(side="left")
    self.labelInfo2.pack(side="left")  
    self.labelInfo3.pack(side="left")  

    self.inputText1 = tk.Entry(self.frame1, width=20)
    self.inputText2 = tk.Entry(self.frame2, width=20)
    self.inputText3 = tk.Entry(self.frame3, width=20)    
    self.inputText1.pack(side="left")
    self.inputText2.pack(side="left")
    self.inputText3.pack(side="left")
  
    self.buttonSubmit = tk.Button(self.frame3_1,text="Cadastrar")
    self.buttonClear = tk.Button(self.frame3_1,text="Limpar")
    self.buttonSubmit.pack(side="left")
    self.buttonClear.pack(side="left")
    self.buttonSubmit.bind("<Button>", controller.enterHandler)
    self.buttonClear.bind("<Button>", controller.clearHandler)  
  
    self.labelInfo5 = tk.Label(self.frame4_1,text="\nBusca de Clientes")
    self.labelInfo5.pack(side="left")  
    self.labelInfo4 = tk.Label(self.frame4,text="Código:")
    self.labelInfo4.pack(side="left")  
    self.inputText4 = tk.Entry(self.frame4, width=20)  
    self.inputText4.pack(side="left")
    self.buttonFind = tk.Button(self.janela,text="Buscar")
    self.buttonFind.pack(side="bottom")
    self.buttonFind.bind("<Button>", controller.findClientByCode)

  def mostraJanela(self, titulo, mensagem):
    messagebox.showinfo(titulo, mensagem)
    
class Controller(): 
  def __init__(self):
    self.root = tk.Tk()
    self.root.geometry("500x250")
    self.listaClientes = []

    self.view = View(self.root, self) 

    self.root.title("Gestão de clientes")
    self.root.mainloop()

  def enterHandler(self, event):
    nomeCli = self.view.inputText1.get()
    emailCli = self.view.inputText2.get()
    codigoCli = self.view.inputText3.get()
    if not nomeCli or not emailCli or not codigoCli:
      self.view.mostraJanela("Erro", "Preencha todos os campos!")
    else: 
      cliente = ModelCliente(nomeCli, emailCli, codigoCli)
      self.listaClientes.append(cliente)
      self.view.mostraJanela("Sucesso", "Cliente cadastrado com sucesso!")
      self.clearHandler(event)

  def findClientByCode(self, event):
    codigoCli = self.view.inputText4.get()
    if not codigoCli :
      self.view.mostraJanela("Erro", "Código de consulta vazio!")
    else: 
      clienteEncontrado = False
      for cliente in self.listaClientes: 
        if(cliente.getCodigo() == codigoCli):
          self.view.mostraJanela("Cliente encontrado!", f"Cliente encontrado! \n\n Nome: {cliente.getNome()} \n Email: {cliente.getEmail()} \n Código: {cliente.getCodigo()}")
          clienteEncontrado = True
        
      if not clienteEncontrado:
        self.view.mostraJanela("Cliente não encontrado", f"Código não cadastrado!")
      self.view.inputText3.delete(0, len(self.view.inputText3.get()))

  def clearHandler(self, event):
    self.view.inputText1.delete(0, len(self.view.inputText1.get()))
    self.view.inputText2.delete(0, len(self.view.inputText2.get()))
    self.view.inputText3.delete(0, len(self.view.inputText3.get()))
    
if __name__ == "__main__":
  c = Controller()