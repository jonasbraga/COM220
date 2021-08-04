import tkinter as tk
from tkinter import messagebox
import pickle
import os

class Album:
  def __init__(self, titulo, ano, artista):
    self.titulo = titulo
    self.ano = ano
    self.artista = artista
    self.musicas = []
  
  def getTitulo(self):
    return self.titulo

  def getAno(self):
    return self.ano
  
  def getMusicas(self):
    return self.musicas
  
  def addMusica(self, musica):
    self.musicas.append(musica)

class LimiteInsereAlbum(tk.Toplevel):
  def __init__(self, controle):
    tk.Toplevel.__init__(self)
    self.geometry('250x100')
    self.title('Inserir Álbum')
    self.controle = controle

    self.frameTitulo = tk.Frame(self)
    self.frameAno = tk.Frame(self)
    self.frameArtista = tk.Frame(self)
    self.frameBotao = tk.Frame(self)
    self.frameTitulo.pack()
    self.frameAno.pack()
    self.frameArtista.pack()
    self.frameBotao.pack()

    self.labelInsereTitulo = tk.Label(self.frameTitulo, text = 'Titulo do Álbum: ')
    self.labelInsereTitulo.pack(side = 'left')
    self.entraTitulo = tk.Entry(self.frameTitulo, width = 20)
    self.entraTitulo.pack(side = 'left')

    self.labelInsereAno = tk.Label(self.frameAno, text = 'Ano do Álbum: ')
    self.labelInsereAno.pack(side = 'left')
    self.entraAno = tk.Entry(self.frameAno, width = 20)
    self.entraAno.pack(side = 'left')

    self.labelInsereArtista = tk.Label(self.frameArtista, text = 'Artista do Álbum: ')
    self.labelInsereArtista.pack(side = 'left')
    self.entraArtista = tk.Entry(self.frameArtista, width = 20)
    self.entraArtista.pack(side = 'left')

    self.botaoCadastrar = tk.Button(self.frameBotao, text = 'Cadastrar')
    self.botaoCadastrar.pack(side = 'left')
    self.botaoCadastrar.bind('<Button>', controle.cadastrarAlbumHandler)

    self.botaoConcluido = tk.Button(self.frameBotao, text = 'Sair')
    self.botaoConcluido.pack(side = 'left')
    self.botaoConcluido.bind('<Button>', controle.concluidoInsereHandler)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

class LimiteConsultaAlbum(tk.Toplevel):
  def __init__(self, controle):
    tk.Toplevel.__init__(self)
    self.geometry('250x50')
    self.title('Consultar Álbum')
    self.controle = controle

    self.frameAlbum = tk.Frame(self)
    self.frameBotao = tk.Frame(self)
    self.frameAlbum.pack()
    self.frameBotao.pack()

    self.labelTitulo = tk.Label(self.frameAlbum, text = 'Titulo do Álbum: ')
    self.entraTitulo = tk.Entry(self.frameAlbum, width = 20)
    self.labelTitulo.pack(side = 'left')
    self.entraTitulo.pack(side = 'left')

    self.botaoConsultar = tk.Button(self.frameBotao, text = 'Consultar')
    self.botaoConsultar.pack()
    self.botaoConsultar.bind('<Button>', controle.consultarAlbumHandler)

class LimiteMostraAlbum:
  def __init__(self, strr, tipo):
    if tipo:
      messagebox.showinfo('Álbum encontrado', strr)
    else:
      messagebox.showinfo('Aviso', strr)

class AlbumController:
  def __init__(self, controlePrincipal):
    if not os.path.isfile('./album.pickle'):
      self.listaAlbuns = []
    else:
      with open('./album.pickle', 'rb') as f:
        self.listaAlbuns = pickle.load(f)
  
    self.controlePrincipal = controlePrincipal
    self.artistaController = controlePrincipal.artistaController
    self.musicaController = controlePrincipal.musicaController
  
  def getAlbums(self):
    return self.listaAlbuns

  def cadastraAlbum(self):
    self.LimiteCadastraAlbum = LimiteInsereAlbum(self)
  
  def findAlbum(self):
    self.LimiteBuscaAlbum = LimiteConsultaAlbum(self)

  def cadastrarAlbumHandler(self):
    titulo = self.LimiteCadastraAlbum.entraTitulo.get()
    ano = self.LimiteCadastraAlbum.entraAno.get()
    nomeArtista = self.LimiteCadastraAlbum.entraArtista.get()

    for art in self.artistaController.getArtistas():
      if self.isSameArtista(nomeArtista, art.getNome()):
        album = Album(titulo, ano, art)
        self.listaAlbuns.append(album)
        art.addAlbum(album)
        self.LimiteCadastraAlbum.mostraJanela('Sucesso', 'Álbum cadastrado com sucesso')
        self.limpaTituloInsere()
        self.limpaAnoInsere()
        self.limpaArtistaInsere()
        return

    self.LimiteCadastraAlbum.mostraJanela('Aviso', 'Artista não encontrado')
  
  def isSameArtista(self, artista1, artista2):
    return artista1.strip().lower() == artista2.strip().lower()

  def consultarAlbumHandler(self):
    titulo = self.LimiteBuscaAlbum.entraTitulo.get()
    strr = ''
    for album in self.getAlbums():
      if self.isSameAlbum(titulo, album.getTitulo()):
        strr += f"{titulo}\n\n"
        for musicas in album.getMusicas():
          strr += f"{musicas.getNroFaixa()} - {musicas.getTitulo()}\n"
        LimiteMostraAlbum(strr, True)
        self.limpaTituloConsulta()
        return
    LimiteMostraAlbum('Álbum não encontrado', False)
    self.limpaTituloConsulta()

  def isSameAlbum(self, album1, album2):
    return album1.strip().lower() == album2.strip().lower()

  # Reset form
  def limpaTituloInsere(self):
    self.LimiteCadastraAlbum.entraTitulo.delete(0, len(self.LimiteCadastraAlbum.entraTitulo.get()))
  
  def limpaAnoInsere(self):
    self.LimiteCadastraAlbum.entraAno.delete(0, len(self.LimiteCadastraAlbum.entraAno.get()))
  
  def limpaArtistaInsere(self):
    self.LimiteCadastraAlbum.entraArtista.delete(0, len(self.LimiteCadastraAlbum.entraArtista.get()))
  
  def limpaTituloConsulta(self):
    self.LimiteBuscaAlbum.entraTitulo.delete(0, len(self.LimiteBuscaAlbum.entraTitulo.get()))

  # Salvar dados
  def saveAlbum(self):
    if len(self.listaAlbuns) != 0:
      with open("./album.pickle", "wb") as f:
        pickle.dump(self.listaAlbuns, f)
  
  def concluidoInsereHandler(self):
    self.LimiteCadastraAlbum.destroy()
  
  def concluidoConsultaHandler(self):
    self.LimiteBuscaAlbum.destroy()