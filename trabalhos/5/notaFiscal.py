class Produto:
  def __init__(self, cod, descricao, valor):
    self.__cod = cod
    self.__descr = descricao
    self.__valor = valor

  def getCod(self):
    return self.__cod
  
  def getDescricao(self):
    return self.__descr
  
  def getValor(self):
    return self.__valor
     
class NotaFiscal():
  def __init__(self, nroNF, nomeCliente, itensDesejados):
    self.__nroNF = nroNF
    self.__nomeCliente = nomeCliente
    self.__itensNF = []
    self.__createNotaFiscal(itensDesejados)
    
  def __createNotaFiscal(self, itens):
  
    produtosIndisponiveis = 0

    for produto, quantidade in itens:
      produtosIndisponiveis += 1
      if(produto.getCod() not in Loja.estoque.keys()):
        print(f"O produto \"{produto.getDescricao()}\" não existe no estoque.\n")
        continue
      if((Loja.estoque[produto.getCod()] <= 0)):
        print(f"O produto \"{produto.getDescricao()}\" não tem mais estoque.\n")
        continue
      if((Loja.estoque[produto.getCod()] - quantidade) < 0):
        print(f"Não há estoque de \"{produto.getDescricao()}\" suficiente para a compra.\n")
        continue

      produtosIndisponiveis -= 1
      Loja.estoque[produto.getCod()] -= quantidade
      self.__itensNF.append([produto, quantidade])
    
    if produtosIndisponiveis == len(itens):
      print("Nota fiscal não criada.\n\n")
    elif produtosIndisponiveis == 0:
      print("Nota fiscal criada com sucesso.\n\n")
    elif produtosIndisponiveis < len(itens):
      print("Nota fiscal criada parcialmente.\n\n")

  def getIDNotaFiscal(self):
    return self.__nroNF
  
  def getNome(self):
    return self.__nomeCliente
  
  def getItens(self):
    produtos = []
    for produto, quantidade in self.__itensNF:
      produtos.append([produto.getDescricao(), produto.getValor(), quantidade])
    return produtos
      
  def getValorNota(self):
    totalNotaFiscal = 0
    for produto, quantidade in self.__itensNF:
      totalNotaFiscal += (produto.getValor() * quantidade)
    return totalNotaFiscal
 
class Loja:
  estoque = {
    15010: 4,
    15011: 10,
    15012: 1,
    15013: 1,
    15014: 2,
    15015: 0,
    15016: 4,
    15017: 3,
    15018: 1,
    15019: 3
  }
  produtos = [
    Produto(15011, "Camiseta Polo", 70), 
    Produto(15019, "Calça Jeans", 80),
    Produto(15013, "Boné Nike", 45),
    Produto(15012, "Calça Moletom Adidas", 149), 
    Produto(15015, "Camiseta Regata", 40),
    Produto(15014, "Blusa de frio", 139), 
    Produto(15017, "Jaqueta de couro", 300),
    Produto(15016, "Meia lupo", 20),
    Produto(15010, "Gravata", 30),
    Produto(15018, "Terno Smoking", 440)
  ]

notasFiscais = [
  NotaFiscal(372311, 'Jonas Braga',     [[Loja.produtos[0], 6], [Loja.produtos[1], 1], [Loja.produtos[4], 1]]),
  NotaFiscal(135614, 'Pedro dos testes', [[Loja.produtos[6], 4]]),
  NotaFiscal(252126, 'Jãozin QA',       [[Loja.produtos[7], 2], [Loja.produtos[8], 1], [Loja.produtos[3], 2]]),
  NotaFiscal(135614, 'Luana testadora', [[Loja.produtos[5], 2], [Loja.produtos[3], 1]]),
]

print("======== INFORMAÇÕES DA COMPRA ========\n")

for cliente in notasFiscais:
  print(f"ID da Nota: {cliente.getIDNotaFiscal()}")
  print(f"Cliente: {cliente.getNome()}")
  print("Produtos:")
  for item in cliente.getItens():
    print(f"\t Produto: {item[0]}")
    print(f"\t Valor unitário: {item[1]}")
    print(f"\t Quantidade: {item[2]}")
    print()
  print(f"Preço total: {cliente.getValorNota()}")
  print("\n=====================================================\n")
