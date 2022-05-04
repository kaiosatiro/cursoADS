import sqlalchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import column

engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()

Base = declarative_base(engine)
session = Session()

connection.execute(""" CREATE TABLE IF NOT EXISTS FUNCIONARIO(
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255) NOT NULL,
                        IDADE INT NOT NULL,
                        SALARIO FLOAT NOT NULL)""")

class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)
    idade = Column('IDADE', String(255), nullable=False)
    salario = Column('SALARIO', Float, nullable=False)
    
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


func1 = Funcionario('Paraiaba', 30, 100.00)
func2 = Funcionario('Jamerson', 20, 200.00)
func3 = Funcionario('Joseildo', 40, 300.00)
lista = [func1, func2, func3]

session.add_all(lista)
session.commit()

consulta = session.query(Funcionario).all()

for i in consulta:
    print(f'''
          Nome...... {i.nome}
          Salario... {i.salario}
          ''')

consulta = session.query(Funcionario).filter(Funcionario.salario > 150)

for i in consulta:
    print(f'''
          Nome...... {i.nome}
          Salario... {i.salario}
          ''')