import sqlalchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.functions import coalesce
from sqlalchemy.sql.schema import ForeignKey

engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()

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
    pagina = Column('PAGINAS', Integer, nullable=False)
    autor_id = Column('AUTOR_ID', Integer, nullable=False)
    
    def __init__(self, titulo, pagina, autor_id):
        self.titulo = titulo
        self.pagina = pagina
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

lista = session.query(Autor, Livro).filter(Autor.id == Livro.autor_id).order_by(Autor.nome)

for i in lista:
    print(f'''
          {i.Autor.nome}.....{i.Livro.titulo}          
          ''')
    
    