# ATIVIDADE CONTÍNUA 03

# NOMES DOS ALUNOS (máximo 6 alunos)
# ALUNO 1: Caio Satiro          2020019
# ALUNO 2: Victor Ezemplari     2100264
# ALUNO 3: Carolina Aparecida   2100194
# ALUNO 4: Ricardo Tadeu        2101700
# ALUNO 5: Carlos Roberto       2020021


class SuperPoder:
    def __init__(self, nome, categoria):
        self.__nome = nome
        self.__categoria = categoria

    def get_nome(self):
        return self.__nome

    def get_categoria(self):
        return self.__categoria


class Personagem:
    def __init__(self, nome, nome_vida_real):
        self.__nome = nome
        self.__nome_vida_real = nome_vida_real
        self.__poderes = []

    def adicionar_super_poder(self, superpoder):
        if len(self.__poderes) == 4:
            raise ValueError
        else:
            self.__poderes.append(superpoder)

    def get_poder_total(self):
        soma = 0
        for poder in self.__poderes:
            soma += poder.get_categoria()
        return soma


class SuperHeroi(Personagem):
    def get_poder_total(self):
        poder = super().get_poder_total()
        return poder * 1.1


class Vilao(Personagem):
    def __init__(self, nome, nome_vida_real, tempo_de_prisao):
        super().__init__(nome, nome_vida_real)
        self.tempo_de_prisao = tempo_de_prisao


class Confronto:
    def lutar(self, superheroi, vilao):
        heroi = superheroi.get_poder_total()
        bandido = vilao.get_poder_total()
        if heroi > bandido:
            return 1
        elif bandido > heroi:
            return 2
        else:
            return 0
