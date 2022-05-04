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


# Criar tabela no banco de dados, caso não exista
connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255) NOT NULL,
                        IDADE INT NOT NULL,
                        SALARIO FLOAT NOT NULL)
                    """)


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)
    idade = Column('IDADE', Integer, nullable=False)
    salario = Column('SALARIO', Float, nullable=False)
    
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

'''
lista = []
while True:
    nome = input("Nome do funcionario (Digite 'SAIR' para finalizar): ")
    if nome == 'SAIR':
        break
    idade = int(input('Idade do Funcionário: '))
    salario = float(input('Salário do funcionario: '))
    func = Funcionario(nome, idade, salario)
    lista.append(func)

session.add_all(lista)
session.commit()
'''
lista = session.query(Funcionario).order_by(Funcionario.nome)
for n in lista:
    print('ID: ', n.id)
    print('Nome: ', n.nome)
    print('Idade: ', n.idade)
    print('Salário: ', n.salario)
    print('-------------------------')
    
print('FUNCIONARIO COM SALARIO SUPERIOR A R$ 2000.00')
lista = session.query(Funcionario).filter(Funcionario.salario > 2000).order_by(Funcionario.nome)
for n in lista:
    print('ID: ', n.id)
    print('Nome: ', n.nome)
    print('Idade: ', n.idade)
    print('Salário: ', n.salario)
    print('-------------------------')
