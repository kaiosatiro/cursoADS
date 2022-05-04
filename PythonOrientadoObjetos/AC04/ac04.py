# PROGRAMAÇÃO ORIENTADA A OBJETOS
# ATIVIDADE CONTÍNUA 04

# INSIRA ABAIXO O NOME DOS ALUNOS DO GRUPO (máximo 6)
# ALUNO 1: Carlos Roberto       2020021
# ALUNO 2: Victor Ezemplari     2100264
# ALUNO 3: Carolina Aparecida   2100194
# ALUNO 4: Ricardo Tadeu        2101700
# ALUNO 5: Caio Satiro          2020019

from abc import ABC, abstractmethod


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.casas = []

    def incluir_casa(self, casa):
        self.casas.append(casa)


class Casa:
    def __init__(self, nome, animal):
        self.nome = nome
        self.animal = animal
        self.__diretor = None
        self.__monitor = None

    def set_diretor(self, diretor):
        self.__diretor = diretor

    def set_monitor(self, monitor):
            self.__monitor = monitor

    def get_monitor(self):
        return self.__monitor

    def get_diretor(self):
        return self.__diretor


class Disciplina:
    def __init__(self, nome, ementa):
        self.nome = nome
        self.ementa = ementa


class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.disciplinas = []

    @abstractmethod
    def incluir_disciplina(self):
        pass


class Professor(Pessoa):
    def __init__(self, nome, nascimento):
        super().__init__(nome, nascimento)

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


class Aluno(Pessoa):
    def __init__(self, nome, nascimento, tipo):
        super().__init__(nome, nascimento)
        self.tipo = tipo
        self.casa = None
        self.__triunfos = 0
        self.__mau_feitos = 0

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def set_casa(self, casa):
        self.casa = casa

    def incluir_triunfo(self, quantidade):
        self.__triunfos += quantidade

    def incluir_mau_feito(self, quantidade):
        self.__mau_feitos += quantidade

    def get_triunfos(self):
        return self.__triunfos

    def get_mau_feitos(self):
        return self.__mau_feitos


class Torneio:
    def __init__(self, casa1, casa2):
        self.casa1 = casa1
        self.casa2 = casa2
        self.__pontos_casa1 = 0
        self.__pontos_casa2 = 0

    def marcar_ponto(self, casa, quantidade):
        self.casa = casa
        if casa == self.casa1:
            self.__pontos_casa1 += quantidade
        elif casa == self.casa2:
            self.__pontos_casa2 += quantidade

    def get_pontos_casa1(self):
        return self.__pontos_casa1

    def get_pontos_casa2(self):
        return self.__pontos_casa2
