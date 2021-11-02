# classes Biblioteca e Livro:
# - A Biblioteca contem uma lista de livros disponiveis e uma lista de livros alugados
# - A biblioteca possui um metodo para alugar um livro. Caso o livro jah esteja alugado a pessoa nao poderah alugar este livro.
# - A biblioteca possui um metodo para devolver o livro.
# - A biblioteca possui um metodo que devolve o nome do livro mais alugado.
from math import floor

class Livro:
    codigo = None
    nome = None
    autor = None
    __qtdeAlugueis = 0

    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor
               
    def incrementaAluguel(self):
        self.__qtdeAlugueis += 1
    def getQtdeAlugueis(self):
        return self.__qtdeAlugueis

class Biblioteca:
    alugados = []
    disponiveis = []

    def inserir(self, livro):
        self.disponiveis.append(livro)

    def alugar(self, livro):
        ok = True
        mensagem = None
        if livro in self.disponiveis:
            for i in self.disponiveis:
                if i == livro:
                    i.incrementaAluguel()
                    self.alugados.append(i)
                    self.disponiveis.remove(i)
                    break
        elif livro in self.alugados:
            ok = False
            mensagem = "O livro ja esta alugado, infelizmente voce nao podera alugar"
        else:
            ok = False
            mensagem = "O livro nao existe"
        return (ok, mensagem)

    def devolver(self, codLivro):
        ok = True
        mensagem = None
        for livro in self.alugados:
            if livro.codigo == codLivro:
                self.disponiveis.append(livro)
                self.alugados.remove(livro)
                break
        else:
            ok = False
            mensagem = "O livro nao esta alugado"
        return (ok, mensagem)

    def livroMaisAlugado(self):
        ok = True
        mensagem = None
        maior = 0
        nome = None
        for livro in self.disponiveis:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        for livro in self.alugados:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        if maior == 0:
            ok = False
            mensagem = "Nenhum livro foi alugado ainda"
        else:
            mensagem = "O livro mais alugado e: %s (%d alugueis)"%(nome, maior)
            return (ok, mensagem)

#O Código acima foi produzido pelo professor Cícero Garrozzi para realização deste exercício

#Ordenar as listas alugados e disponiveis separadamente
    def insertionSort(self, livros):
        for i in range(1,len(livros)):
            livro = livros[i]
            k = i
            while k > 0 and livro.nome < livros[k - 1].nome:
                livros[k] = livros[k - 1]
                k -= 1
            livros[k] = livro
        return livros

#Mesclar os resultados das duas listas ordenadas
    def merge(self, alugados, disponiveis):
        comprimento = len(alugados) + len(disponiveis)
        livros = [None for i in range(comprimento)]
        i = 0
        j = 0
        limite_esquerda = len(alugados)
        limite_direita = len(disponiveis)
        for k in range(0,comprimento):
            if i == limite_esquerda:
                livros[k] = disponiveis[j]
                j = j + 1
            elif j == limite_direita:
                livros[k] = alugados[i]
                i = i + 1
            elif alugados[i].nome < disponiveis[j].nome:
                livros[k] = alugados[i]
                i = i + 1
            else:
                livros[k] = disponiveis[j]
                j = j + 1
        return livros
    
#Definir um método "livrosOrdenadosPeloNome"
    def livrosOrdenadosPeloNome(self):
        alugados = self.insertionSort(self.alugados)
        disponiveis = self.insertionSort(self.disponiveis)
        livrosOrdenados = self.merge(alugados, disponiveis)
        return livrosOrdenados

#Tratar a entrada
entrada = input()
listaEntrada = entrada.split(',')

quantidadeLivros = int(listaEntrada.pop(0))

biblioteca = Biblioteca()
for i in range(quantidadeLivros):
    codigo = listaEntrada.pop(0)
    nome = listaEntrada.pop(0)
    autor = listaEntrada.pop(0)
    livro = Livro(codigo, nome, autor)
    biblioteca.inserir(livro)

#Tratar a saída
livrosOrdenados = biblioteca.livrosOrdenadosPeloNome()
codigosOrdenados = []
for livro in livrosOrdenados:
    codigosOrdenados.append(livro.codigo)

saida = " ".join(codigosOrdenados)
print(saida)