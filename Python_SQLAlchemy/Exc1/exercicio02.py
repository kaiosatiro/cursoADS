# Importação das bibliotecas do SQLAlchemy
import sqlalchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


# Criar Conexão com Banco SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()


# Criar sessão com o Banco de Dados
Base = declarative_base(engine)
session = Session()

connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR(
           ID INTEGER PRIMARY KEY,
           NOME varchar(255) NOT NULL)""")

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO(
           ID INTEGER PRIMARY KEY,
           TITULO VARCHAR(255) NOT NULL,
           PAGINAS INT NOT NULL,
           AUTOR_ID INT NOT NULL)""")


class Autor(Base):
    __tablename__ = 'AUTOR'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)

    def __init__(self, nome):
        self.nome = nome


class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255), nullable=False)
    paginas = Column('PAGINAS', Integer, nullable=False)
    autor_id = Column('AUTOR_ID', Integer, nullable=False)

    def __init__(self, titulo, paginas, autor_id):
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id


autor1 = Autor('Paulo')
autor2 = Autor('Fernanda')
session.add(autor1)
session.add(autor2)
session.commit()

livro1 = Livro('Titulo do livro 1', 300, autor1.id)
livro2 = Livro('Titulo do livro 2', 150, autor2.id)
session.add(livro1)
session.add(livro2)
session.commit()

# consulta todos os autores
lista = session.query(Autor)
for n in lista:
    print(n.id, n.nome)

# consulta todos os livro
lista = session.query(Livro)
for n in lista:
    print(n.id, n.titulo, n.paginas, n.autor_id)

# exemplo de join
lista = session.query(Livro, Autor).filter(Livro.autor_id == Autor.id)
for n in lista:
    print(n.Livro.titulo, n.Autor.nome)

connection.close()
