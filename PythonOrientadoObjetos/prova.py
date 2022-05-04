'''
Implemente as classes Empresa e Funcionario.
A classe Funcionario possui os atributos PRIVADOS nome e salario
a classe Empresa possui o atributo funcionarios que armazena uma lista de
objetos da classe Funcionario.
Os atributos das classes devem ser inicializados nos construtores.
A lista de funcionarios deve ser inicializada como vazia.

A classe Funcionario deve implementar os métodos get_nome e get_salario.
A classe Empresa deve implementar os métodos:
    incluir_funcionario: recebe como entrada um objeto Funcionario e o insere
    na lista de funcionarios.
    quantidade_funcionarios: retorna a quantidade de funcionários que recebem
    salário superior a R$ 2.000,00
'''


# --------------------- IMPLEMENTE SEU CÓDIGO AQUI --------------------------
class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario
    
    def get_nome(self):
        return self.__nome
    
    def get_salario(self):
        return self.__salario

class Empresa:
    def __init__(self):
        self.funcionarios = []
    
    def incluir_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def quantidade_funcionarios(self):
        quantidade = 0
        for funcionario in self.funcionarios:
            if funcionario.get_salario() > 2000:
                quantidade += 1
        return quantidade


# -------------- PROGRAMA PRINCIPAL (não deve ser alterado) -----------------

func1 = Funcionario('John', 4000)
print("Nome:", func1.get_nome())
print("Salário:", func1.get_salario())

func2 = Funcionario('George', 2500)
print("Nome:", func2.get_nome())
print("Salário:", func2.get_salario())

func3 = Funcionario('Mathew', 1800)
print("Nome:", func3.get_nome())
print("Salário:", func3.get_salario())

empresa = Empresa()
empresa.incluir_funcionario(func1)
empresa.incluir_funcionario(func2)
empresa.incluir_funcionario(func3)
print("Quantidade de Funcionarios:", empresa.quantidade_funcionarios())