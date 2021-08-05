from tkinter import messagebox, ttk
import tkinter as tk
import pickle
import os

# ================= MAIN =================

class LimitePrincipal:
  def __init__(self, raiz, controle):
    self.raiz = raiz
    self.controle = controle
    self.raiz.geometry('300x60')
    self.raiz.title('Cupom prova')

    self.menuBar = tk.Menu(self.raiz)
    self.menuProduto = tk.Menu(self.menuBar)
    self.menuCupomFiscal = tk.Menu(self.menuBar)
    self.menuSair = tk.Menu(self.menuBar)

    self.menuProduto.add_command(label = 'Cadastrar', command = self.controle.createProduto)
    self.menuProduto.add_command(label = 'Consultar', command = self.controle.findProduto)
    self.menuBar.add_cascade(label = 'Produto', menu = self.menuProduto)

    self.menuCupomFiscal.add_command(label = 'Cadastrar', command = self.controle.createCupomFiscal)
    self.menuCupomFiscal.add_command(label = 'Consultar', command = self.controle.findCupomFiscal)
    self.menuBar.add_cascade(label = 'Cupom Fiscal', menu = self.menuCupomFiscal)

    self.menuSair.add_command(label = 'Salvar', command = self.controle.saveDados)
    self.menuSair.add_command(label = 'Não Salvar', command = lambda: self.raiz.destroy())
    self.menuBar.add_cascade(label = 'Sair', menu = self.menuSair)

    self.raiz.config(menu=self.menuBar)

class ControlePrincipal:
  def __init__(self):
    self.raiz = tk.Tk()
    self.limite = LimitePrincipal(self.raiz, self)
    self.produtoController = ProdutoController()
    self.cupomFiscalController = CupomFiscalController(self)

    self.raiz.mainloop()

  def createProduto(self):
    self.produtoController.cadastraProduto()

  def findProduto(self):
    self.produtoController.findProduto()

  def createCupomFiscal(self):
    self.cupomFiscalController.cadastraCupomFiscal()
    self.cupomFiscalController.atualizaListBox()

  def findCupomFiscal(self):
    self.cupomFiscalController.findCupomFiscal()

  def saveDados(self):
    self.produtoController.saveProduto()
    self.cupomFiscalController.saveCupomFiscal()
    self.raiz.destroy()

# ================= Produto =================

class Produto:
  def __init__(self, codigo, descricao, valor):
    self.__codigo = codigo
    self.__descr = descricao
    self.__valor = valor

  def getCodigo(self):
    return self.__codigo
  
  def getDescricao(self):
    return self.__descr
  
  def getValor(self):
    return self.__valor
  
class LimiteInsereProduto(tk.Toplevel):
  def __init__(self, controle):
    tk.Toplevel.__init__(self)
    self.geometry('250x100')
    self.title('Inserir Produto')
    self.controle = controle

    self.frameCodigo = tk.Frame(self)
    self.frameCodigo.pack()
    self.frameDescricao = tk.Frame(self)
    self.frameDescricao.pack()
    self.frameValorUnitario = tk.Frame(self)
    self.frameValorUnitario.pack()
    self.frameBotao = tk.Frame(self)
    self.frameBotao.pack()

    self.labelCodigo = tk.Label(self.frameCodigo, text = 'Código: ')
    self.labelCodigo.pack(side = 'left')
    self.entraCodigo = tk.Entry(self.frameCodigo, width = 20)
    self.entraCodigo.pack(side = 'left')

    self.labelDescricao = tk.Label(self.frameDescricao, text = 'Descrição do produto: ')
    self.labelDescricao.pack(side = 'left')
    self.entraDescricao = tk.Entry(self.frameDescricao, width = 20)
    self.entraDescricao.pack(side = 'left')

    self.labelValorUnitario = tk.Label(self.frameValorUnitario, text = 'Valor Unitário: ')
    self.labelValorUnitario.pack(side = 'left')
    self.entraValorUnitario = tk.Entry(self.frameValorUnitario, width = 20)
    self.entraValorUnitario.pack(side = 'left')

    self.botaoCadastrar = tk.Button(self.frameBotao, text = 'Cadastrar')
    self.botaoCadastrar.pack(side = 'left')
    self.botaoCadastrar.bind('<Button>', controle.cadastrarProdutoHandler)

    self.botaoConcluido = tk.Button(self.frameBotao, text = 'Sair')
    self.botaoConcluido.pack(side = 'left')
    self.botaoConcluido.bind('<Button>', controle.concluidoInsereHandler)
  
  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

class LimiteConsultaProduto(tk.Toplevel):
  def __init__(self, controle):
    tk.Toplevel.__init__(self)
    self.geometry('250x100')
    self.title('Consultar Produto')
    self.controle = controle

    self.frameProduto = tk.Frame(self)
    self.frameBotao = tk.Frame(self)
    self.frameProduto.pack()
    self.frameBotao.pack()

    self.labelCodigo = tk.Label(self.frameProduto, text = 'Codigo do Produto: ')
    self.entraCodigo = tk.Entry(self.frameProduto, width = 20)
    self.labelCodigo.pack(side = 'left')
    self.entraCodigo.pack(side = 'left')

    self.botaoConsultar = tk.Button(self.frameBotao, text = 'Consultar')
    self.botaoConsultar.pack()
    self.botaoConsultar.bind('<Button>', controle.consultarProdutoHandler)

class LimiteMostraProduto:
  def __init__(self, strr, tipo):
    if tipo:
      messagebox.showinfo('Lista de Álbuns', strr)
    else:
      messagebox.showinfo('Aviso', strr)

class ProdutoController:
  def __init__(self):
    if not os.path.isfile('./produto.pickle'):
      self.listaProdutos = []
    else:
      with open('./produto.pickle', 'rb') as f:
        self.listaProdutos = pickle.load(f)

  def getProdutos(self):
    return self.listaProdutos

  def cadastraProduto(self):
    self.LimiteCadastraProduto = LimiteInsereProduto(self)
  
  def findProduto(self):
    self.LimiteBuscaProduto = LimiteConsultaProduto(self)

  def cadastrarProdutoHandler(self, event):
    codigo = self.LimiteCadastraProduto.entraCodigo.get().strip()
    descricao = self.LimiteCadastraProduto.entraDescricao.get()
    valorUnitario = self.LimiteCadastraProduto.entraValorUnitario.get()
    self.listaProdutos.append(Produto(codigo, descricao, valorUnitario))
    self.LimiteCadastraProduto.mostraJanela('Sucesso', 'Produto cadastrado com sucesso')
    self.limpaCodigoInsere(event)
    self.limpaDescricaoInsere(event)
    self.limpaValorUnitarioInsere(event)
  
  def consultarProdutoHandler(self, event):
    codigo = self.LimiteBuscaProduto.entraCodigo.get()
    for produto in self.listaProdutos():
      if codigo == produto.getCodigo():
        LimiteMostraProduto(f"{produto.getCodigo()}\n\n{produto.getDescricao()}\n\n{produto.getValor()}", True)
        self.limpaCodigoConsulta(event)
        return
    LimiteMostraProduto('Produto não encontrado', False)
    self.limpaCodigoConsulta(event)
  
  # Reset form
  def limpaCodigoInsere(self, event):
    self.LimiteCadastraProduto.entraCodigo.delete(0, len(self.LimiteCadastraProduto.entraCodigo.get()))
    
  def limpaDescricaoInsere(self, event):
    self.LimiteCadastraProduto.entraDescricao.delete(0, len(self.LimiteCadastraProduto.entraDescricao.get()))
  
  def limpaValorUnitarioInsere(self, event):
    self.LimiteCadastraProduto.entraValorUnitario.delete(0, len(self.LimiteCadastraProduto.entraValorUnitario.get()))
  
  def limpaCodigoConsulta(self):
    self.LimiteBuscaProduto.entraCodigo.delete(0, len(self.LimiteBuscaProduto.entraCodigo.get()))

  # Salvar dados
  def saveProduto(self):
    if len(self.listaProdutos) != 0:
      with open("./produto.pickle", "wb") as f:
        pickle.dump(self.listaProdutos, f)
  
  def concluidoInsereHandler(self, event):
    self.LimiteCadastraProduto.destroy()
  
  def concluidoConsultaHandler(self, event):
    self.LimiteBuscaProduto.destroy()

# ================= Cupom Fiscal =================

class CupomFiscal:
  def __init__(self, nroCupom, itensCupom):
    self.nroCupom = nroCupom
    self.itensCupom = itensCupom

  def getNroCupom(self):
    return self.nroCupom

  def getItensCupom(self):
    return self.itensCupom

class LimiteInsereProdutos(tk.Toplevel):
  def __init__(self, controle, listaProdutos):
    tk.Toplevel.__init__(self)
    self.geometry('350x250')
    self.title("Inserir Cupom Fiscal")
    self.controle = controle
    self.listaProdutos = listaProdutos
    self.ultimoProduto = ''

    self.frameNroCupom = tk.Frame(self)
    self.frameProdutos = tk.Frame(self)
    self.frameBotao = tk.Frame(self)
    self.frameNroCupom.pack()
    self.frameProdutos.pack()
    self.frameBotao.pack()        

    self.labelNroCupom = tk.Label(self.frameNroCupom,text="Digite o numero do cupom fiscal: ")
    self.labelNroCupom.pack(side="left")
    self.entraNroCupom = tk.Entry(self.frameNroCupom, width=20)
    self.entraNroCupom.pack(side="left")

    self.labelProdutos = tk.Label(self.frameProdutos,text="Escolha os produtos: ")
    self.labelProdutos.pack(side="left") 
    self.listaBox = tk.Listbox(self.frameProdutos, width = 30)
    self.listaBox.pack(side="left")

    self.botaoCadastrarProduto = tk.Button(self.frameBotao ,text="Inserir produto")           
    self.botaoCadastrarProduto.pack(side="left")
    self.botaoCadastrarProduto.bind("<Button>", controle.createProdutoHandler)

    self.botaoCadastrar = tk.Button(self.frameBotao ,text="Fechar cupom")           
    self.botaoCadastrar.pack(side="left")
    self.botaoCadastrar.bind("<Button>", controle.cadastrarCupomFiscalHandler) 

    self.botaoConcluido = tk.Button(self.frameBotao, text = 'Sair')
    self.botaoConcluido.pack(side = 'left')
    self.botaoConcluido.bind('<Button>', controle.concluidoCadastraCupomFiscal)  

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

class LimiteConsultaCupomFiscal(tk.Toplevel):
  def __init__(self, controle):
    tk.Toplevel.__init__(self)
    self.geometry('250x100')
    self.title('Consultar CupomFiscal')
    self.controle = controle

    self.frameCupomFiscal = tk.Frame(self)
    self.frameBotao = tk.Frame(self)
    self.frameCupomFiscal.pack()
    self.frameBotao.pack()

    self.labelNroCupom = tk.Label(self.frameCupomFiscal, text = 'Numero do Cupom Fiscal: ')
    self.entraNroCupom = tk.Entry(self.frameCupomFiscal, width = 20)
    self.labelNroCupom.pack(side = 'left')
    self.entraNroCupom.pack(side = 'left')

    self.botaoConsultar = tk.Button(self.frameBotao, text = 'Consultar')
    self.botaoConsultar.pack()
    self.botaoConsultar.bind('<Button>', controle.findCupomFiscalHandler)  
    
  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg) 

class LimiteMostraCupomFiscal(tk.Toplevel):
  def __init__(self, strr):
    messagebox.showinfo('Lista de músicas', strr)

class CupomFiscalController:       
  def __init__(self, controlePrincipal):
    if not os.path.isfile('./cupomFiscal.pickle'):
      self.listaCupomFiscal = []
    else:
      with open('./cupomFiscal.pickle', 'rb') as f:
        self.listaCupomFiscal = pickle.load(f)

    self.controlePrincipal = controlePrincipal
    self.produtoController = controlePrincipal.produtoController
  
  def findCupomFiscal(self):
    self.LimiteBuscaCupomFiscal = LimiteConsultaCupomFiscal(self)

  def cadastraCupomFiscal(self):
    self.listaProdutosSelecionadas = []     
    self.listaProdutos = []
    for produtos in self.produtoController.getProdutos():
      self.listaProdutos.append(produtos.getCodigo())
    self.LimiteCadastraProduto = LimiteInsereProdutos(self, self.listaProdutos)
  
  def cadastrarCupomFiscalHandler(self, event):
    nroCupomFiscal = self.LimiteCadastraProduto.entraNroCupom.get()
    produtos = self.listaProdutosSelecionadas
    cupomFiscal = CupomFiscal(nroCupomFiscal, produtos)
    self.listaCupomFiscal.append(cupomFiscal)
    self.LimiteCadastraProduto.mostraJanela('Aviso', 'Cupom Fiscal criado com sucesso')
    self.LimiteCadastraProduto.destroy()
  
  def createProdutoHandler(self, event):
    produtoCodigo = self.LimiteCadastraProduto.listaBox.get(tk.ACTIVE)
    for produto in self.produtoController.getProdutos():
      if produtoCodigo == produto.getCodigo():
        self.listaProdutosSelecionadas.append(produto)
  
  def findCupomFiscalHandler(self, event):
    nroCupom = self.LimiteBuscaCupomFiscal.entraNroCupom.get()
    strr = ''
    for cupomFiscal in self.listaCupomFiscal:
      if nroCupom == cupomFiscal.getNroCupom():
        strr += f"{cupomFiscal.getNroCupom()}: "
        for produtos in cupomFiscal.getItensCupom():
          strr += f"{produtos.getCodigo()} - {produtos.getDescricao()} - {produtos.getValor()}\n" 
        self.LimiteBuscaCupomFiscal.mostraJanela('Cupom fiscal encontrada', strr)
        return
    self.LimiteBuscaCupomFiscal.mostraJanela('Aviso', 'Cupom fiscal não encontrada')
    
  def concluidoCadastraCupomFiscal(self, event):
    self.LimiteCadastraProduto.destroy()
  
  def saveCupomFiscal(self):
    if len(self.listaCupomFiscal) != 0:
      with open("./cupomFiscal.pickle", "wb") as f:
        pickle.dump(self.listaCupomFiscal, f)

  def atualizaListBox(self):
    listaProdutos = self.produtoController.getProdutos()
    vetorProdutos = []
    self.LimiteCadastraProduto.listaBox.delete(0, tk.END)
    for produto in listaProdutos:
      vetorProdutos.append(produto.getCodigo())
    for music in vetorProdutos:
      self.LimiteCadastraProduto.listaBox.insert(tk.END, music)  

    self.controlePrincipal.raiz.after(100, self.atualizaListBox)

if __name__ == '__main__':
  App = ControlePrincipal()