# ATIVIDADE CONTÍNUA 05

# NOMES DOS ALUNOS: (MÁXIMO 6):
# 2100194 ..... Carolina Aparecida
# 2100264 ..... Victor Ezemplari
# 2101700 ..... Ricardo Tadeu
# 2020021 ..... Carlos Roberto
# 2020019 ..... Caio Satiro

# IMPORTAR MÓDULOS
from typing import Collection
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import column

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
engine = create_engine("sqlite:///server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)


# Classe para mapeamento da tabela
class Filme(Base):

    # FAZER AQUI O MAPEAMENTO DA TABELA
    __tablename__ = 'FILME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255))
    ano = Column('ANO', Integer)
    genero = Column('GENERO', String(255))
    duracao = Column('DURACAO', Integer)
    pais = Column('PAIS', String(255))
    diretor = Column('DIRETOR', String(255))
    elenco = Column('ELENCO', String(255))
    avaliacao = Column('AVALIACAO', Float)
    votos = Column('VOTOS', Integer)
                      
    # Método construtor
    def __init__(self, titulo, ano, genero, duracao, pais, diretor, elenco, avaliacao, votos):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.duracao = duracao
        self.pais = pais
        self.diretor = diretor
        self.elenco = elenco
        self.avaliacao = avaliacao
        self.votos = votos


# Classe para interação com o Banco de Dados
class BancoDeDados:
    def criar_tabela(self):
        # Cria a tabela FILME no banco de dados
        connection.execute("""CREATE TABLE IF NOT EXISTS FILME(
                              ID INTEGER PRIMARY KEY,
                              TITULO VARCHAR(255),
                              ANO INT,
                              GENERO VARCHAR(255),
                              DURACAO INT,
                              PAIS VARCHAR(255),
                              DIRETOR VARCHAR(255),
                              ELENCO VARCHAR(255),
                              AVALIACAO FLOAT,
                              VOTOS INT)""")

    def incluir(self, filme):
        # Recebe um objeto da classe Filme e armazena esse
        # objeto no banco de dados.
        session.add(filme)

    def incluir_lista(self, filmes):
        # Recebe uma lista de objetos da classe Filme e armazena esses
        # objetos no banco de dados
        session.add_all(filmes)

    def alterar_avaliacao(self, id_filme, avaliacao):
        # Recebe o id de um filme e altera sua nota de avaliação de
        # acordo com o valor do parametro avaliacao
        filme = session.query(Filme).get(id_filme)
        filme.avaliacao = avaliacao
        session.commit()

    def excluir(self, id_filme):
        # Recebe o id de um filme e exclui o filme correspondente
        # do banco de dados
        filme = session.query(Filme).get(id_filme)
        session.delete(filme)
        session.commit()

    def buscar_todos(self):
        # Realiza busca no banco de dados e retorna uma
        # lista de objetos da classe Filme com todos os filmes cadastrados,
        # ordenados de forma crescente pelo titulo.
        lista = session.query(Filme).order_by(Filme.titulo.asc())
        return lista

    def buscar_por_ano(self, ano):
        # Realiza busca no banco de dados e retorna uma
        # lista de objetos da classe Filme de um determinado ano,
        # ordenados de forma crescente pelo ano em ordem crescente.
        lista = session.query(Filme).filter(Filme.ano == ano).order_by(Filme.ano)
        return lista

    def buscar_por_genero(self, genero):
        # Realiza busca no banco de dados e retorna uma
        # lista de objetos da classe Filme de um gênero específico,
        # ordenados pelo titulo de forma crescente.
        # DICA:
        #     Utilize a função like. Exemplo:
        #     .filter(Filme.genero.like('%' + genero + '%'))
        lista = session.query(Filme).filter(Filme.genero.like('%'+genero+'%')).order_by(Filme.titulo.asc())
        return  lista

    def buscar_por_elenco(self, ator):
        # Realiza busca no banco de dados e retorna uma
        # lista de objetos da classe Filme que tenha um determinado ator/atriz
        # como parte do elenco, ordenados pelo ano em ordem crescente.
        # DICA:
        #     Utilize a função like. Exemplo:
        #     .filter(Filme.elenco.like('%' + ator + '%'))
        lista = session.query(Filme).filter(Filme.elenco.like('%' + ator + '%')).order_by(Filme.ano.asc())
        return lista

    def buscar_melhores_do_ano(self, ano):
        # Realiza busca no banco de dados e retorna uma lista de
        # objetos da classe Filme de um determinado ano, com nota de avaliação
        # maior ou igual a 90.
        # Deve retornar a lista ordenada pela avaliação em ordem crescente.
        lista = session.query(Filme).filter(Filme.ano == int(ano), Filme.avaliacao >= 90).order_by(Filme.avaliacao.asc())
        return lista

    def importar_filmes(self, nome_arquivo):
        # Recebe como parâmetro o nome de um arquivo de texto e importa os
        # dados contidos no arquivo para o banco de dados.
        # Considere que o arquivo contém uma listagem de filmes no formato:
        # titulo;ano;genero;duracao;país;diretor;elenco;avaliacao;votos
        lista = []
        with open(nome_arquivo, 'r', encoding='UTF-8') as arq:
            for cl in arq.readlines():
                cl = cl.split(';')
                filme = Filme(cl[0], int(cl[1]), cl[2], int(cl[3]), cl[4], cl[5], cl[6], float(cl[7]), int(cl[8]))
                lista.append(filme)
            session.add_all(lista)
            session.commit()
            arq.close()

    def exportar_filmes(self, nome_arquivo):
        # Recebe como parâmetro o nome de um arquivo de texto e exporta os dados
        # contidos na tabela de filmes para esse arquivo de texto.
        # O arquivo deve conter uma listagem dos filmes, ordenados pelos TÍTULOS
        # dos filmes, contendo os dados de cada filme em uma linha, no formato:
        # titulo;ano;genero;duracao;país;diretor;elenco;avaliacao;votos
        with open(nome_arquivo, 'w', encoding='UTF-8') as arq:
            resultado = session.query(Filme).order_by(Filme.titulo)
            for i in resultado:
                arq.write(i.titulo +';'+ str(i.ano) +';'+ i.genero +';'+ str(i.duracao) +';'+ i.pais +
                          ';'+ i.diretor +';'+ i.elenco +';'+ str(i.avaliacao) +';'+ str(i.votos) + '\n')
            arq.close()


# EXEMPLO DE PROGRAMA PRINCIPAL
banco = BancoDeDados()
banco.criar_tabela()

# Importa filmes do arquivo movies.txt e salva no banco de dados
banco.importar_filmes('movies.txt')

# Cria um novo Filme e insere no banco de dados
filme1 = Filme("Parasite", 2019, "Comedy, Drama, Thriller", 132, "Korea",
               "Bong Joon Ho", "Song Kang-ho, Jang Hye-jin, Choi Woo-shik", 92, 40273)
banco.incluir(filme1)

# Cria uma lista com dois novos filmes e insere no banco de dados
filme2 = Filme("Joker", 2019, 'Crime, Drama, Thriller', 122, "USA",
               "Todd Phillips", "Joaquin Phoenix, Robert De Niro, Zazie Beetz", 91, 78481)
filme3 = Filme("Avengers: Endgame", 2019, 'Drama, Thriller', 181, "USA",
               "Anthony Russo, Joe Russo", "Robert Downey Jr., Chris Evans, Mark Ruffalo", 93, 715250)
lista_filmes = [filme2, filme3]
banco.incluir_lista(lista_filmes)

# Altera a avalação do filme de id 7 para 98
banco.alterar_avaliacao(7, 98)

# Exclui o filme de id 6
banco.excluir(6)

# Busca todos os filmes
lista = banco.buscar_todos()
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero, f.diretor, f.elenco, f.avaliacao)

# Busca todos os filmes do ano de 2019
lista = banco.buscar_por_ano(2019)
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano)


# Busca todos os filmes do gênero 'Crime'
lista = banco.buscar_por_genero('Crime')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.genero)


# Busca todos os filmes com participação da atriz de nome 'Nicole Balsam'
lista = banco.buscar_por_elenco('Nicole Balsam')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.elenco)


# Busca os melhores filmes do ano de 2019
lista = banco.buscar_melhores_do_ano('2019')
print('-'*60)
for f in lista:         # exibe lista de filmes
    print(f.id, f.titulo, f.ano, f.avaliacao)


# Exporta filmes do banco de dados para um novo arquivo de texto
banco.exportar_filmes('saida.txt')
