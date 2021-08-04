import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
import os

class Playlist:
  def __init__(self, nome, listaMusicas):
    self.nome = nome
    self.listaMusicas = listaMusicas

  def getNome(self):
    return self.nome

  def getMusicas(self):
    return self.listaMusicas

class LimiteInserePlaylist(tk.Toplevel):
  def __init__(self, controle, listaArtistas):
    tk.Toplevel.__init__(self)
    self.geometry('350x250')
    self.title("Inserir Playlist")
    self.controle = controle
    self.listaArtistas = listaArtistas
    self.ultimoArtista = ''

    self.frameNome = tk.Frame(self)
    self.frameArtistas = tk.Frame(self)
    self.frameMusicas = tk.Frame(self)
    self.frameBotao = tk.Frame(self)
    self.frameNome.pack()
    self.frameArtistas.pack()
    self.frameMusicas.pack()
    self.frameBotao.pack()        

    self.labelNome = tk.Label(self.frameNome,text="Digite o nome da Playlist: ")
    self.labelNome.pack(side="left")
    self.entraNome = tk.Entry(self.frameNome, width=20)
    self.entraNome.pack(side="left")

    self.labelArtista = tk.Label(self.frameArtistas, text="Escolha o artista: ")
    self.labelArtista.pack(side="left")
    self.escolhaArtista = tk.StringVar()
    self.combobox = ttk.Combobox(
      self.frameArtistas, textvariable=self.escolhaArtista, state="readonly", values=self.listaArtistas)
    self.combobox.pack(side="left")
      
    self.labelMusicas = tk.Label(self.frameMusicas,text="Escolha as músicas: ")
    self.labelMusicas.pack(side="left") 
    self.listaBox = tk.Listbox(self.frameMusicas, width = 30)
    self.listaBox.pack(side="left")

    self.botaoCadastrarMusica = tk.Button(self.frameBotao ,text="Inserir música")           
    self.botaoCadastrarMusica.pack(side="left")
    self.botaoCadastrarMusica.bind("<Button>", controle.createMusicaHandler)

    self.botaoCadastrar = tk.Button(self.frameBotao ,text="Criar Playlist")           
    self.botaoCadastrar.pack(side="left")
    self.botaoCadastrar.bind("<Button>", controle.cadastrarPlaylistHandler) 

    self.botaoConcluido = tk.Button(self.frameBotao, text = 'Sair')
    self.botaoConcluido.pack(side = 'left')
    self.botaoConcluido.bind('<Button>', controle.concluidoCadastraPlaylist)  

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

class LimiteConsultaPlaylist(tk.Toplevel):
  def __init__(self, controle):
    tk.Toplevel.__init__(self)
    self.geometry('250x50')
    self.title('Consultar Playlist')
    self.controle = controle

    self.framePlaylist = tk.Frame(self)
    self.frameBotao = tk.Frame(self)
    self.framePlaylist.pack()
    self.frameBotao.pack()

    self.labelTitulo = tk.Label(self.framePlaylist, text = 'Nome da Playlist: ')
    self.entraTitulo = tk.Entry(self.framePlaylist, width = 20)
    self.labelTitulo.pack(side = 'left')
    self.entraTitulo.pack(side = 'left')

    self.botaoConsultar = tk.Button(self.frameBotao, text = 'Consultar')
    self.botaoConsultar.pack()
    self.botaoConsultar.bind('<Button>', controle.findPlaylistHandler)  
    
  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg) 

class LimiteMostraPlaylist(tk.Toplevel):
  def __init__(self, strr):
    messagebox.showinfo('Lista de músicas', strr)

class PlaylistController:       
  def __init__(self, controlePrincipal):
    if not os.path.isfile('./playlist.pickle'):
      self.listaPlaylist = []
    else:
      with open('./playlist.pickle', 'rb') as f:
        self.listaPlaylist = pickle.load(f)

    self.controlePrincipal = controlePrincipal
    self.artistaController = controlePrincipal.artistaController
    self.musicaController = controlePrincipal.musicaController
  
  def findPlaylist(self):
    self.LimiteBuscaPlaylist = LimiteConsultaPlaylist(self)

  def cadastraPlaylist(self):
    self.listaMusicasSelecionadas = []     
    self.listaArtistas = []
    for arti in self.artistaController.getArtistas():
      self.listaArtistas.append(arti.getNome())
    self.LimiteCadastraPlaylist = LimiteInserePlaylist(self, self.listaArtistas)
  
  def cadastrarPlaylistHandler(self):
    nomePlaylist = self.LimiteCadastraPlaylist.entraNome.get()
    musicas = self.listaMusicasSelecionadas
    playlist = Playlist(nomePlaylist, musicas)
    self.listaPlaylist.append(playlist)
    self.LimiteCadastraPlaylist.mostraJanela('Aviso', 'Playlist criada com sucesso')
    self.LimiteCadastraPlaylist.destroy()
  
  def createMusicaHandler(self):
    musicaNome = self.LimiteCadastraPlaylist.listaBox.get(tk.ACTIVE)
    for musc in self.musicaController.getMusicas():
      if self.isSameMusic(musicaNome, musc.getTitulo()):
        self.listaMusicasSelecionadas.append(musc)
        self.LimiteCadastraPlaylist.listaBox.delete(tk.ACTIVE)
  
  def findPlaylistHandler(self):
    play = self.LimiteBuscaPlaylist.entraTitulo.get()
    strr = ''
    for plst in self.listaPlaylist:
      if self.isSamePlaylist(play, plst.getNome()):
        strr += f"{plst.getNome()}\n\n"
        for mus in plst.getMusicas():
          strr += f"{mus.getNroFaixa()} - {mus.getTitulo()}\n" 
        self.LimiteBuscaPlaylist.mostraJanela('Playlist encontrada', strr)
        return
    self.LimiteBuscaPlaylist.mostraJanela('Aviso', 'Playlist não encontrada')

  def isSameMusic(self, music1, music2):
    return music1.strip().lower() == music2.strip().lower()

  def isSamePlaylist(self, playlist1, playlist2):
    return playlist1.strip().lower() == playlist2.strip().lower()

  def isSameArtista(self, artista1, artista2):
    return artista1.strip().lower() == artista2.strip().lower()

  def concluidoCadastraPlaylist(self):
    self.LimiteCadastraPlaylist.destroy()
  
  def savePlaylist(self):
    if len(self.listaPlaylist) != 0:
      with open("./playlist.pickle", "wb") as f:
        pickle.dump(self.listaPlaylist, f)

  def atualizaListBox(self):
    listaMusicas = self.musicaController.getMusicas()
    artistaSel = self.LimiteCadastraPlaylist.escolhaArtista.get()
    if  self.LimiteCadastraPlaylist.ultimoArtista != artistaSel:
      vetorMusicas = []
      self.LimiteCadastraPlaylist.listaBox.delete(0, tk.END)
      for mus in listaMusicas:
        if self.isSameArtista(artistaSel, mus.getArtista().getNome()): 
          if mus not in self.listaMusicasSelecionadas:
            vetorMusicas.append(mus.getTitulo())
      for music in vetorMusicas:
        self.LimiteCadastraPlaylist.listaBox.insert(tk.END, music)  
      self.LimiteCadastraPlaylist.ultimoArtista = artistaSel

    self.controlePrincipal.raiz.after(100, self.atualizaListBox)
  
