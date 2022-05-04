# ATIVIDADE CONTÍNUA 02
# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO 1: Caio Satiro          2020019
# ALUNO 2: Mirelly Simões       1903911 - Trancou a matrícula
# ALUNO 3: Victor Ezemplari     2100264
# ALUNO 4: Carolina Aparecida   2100194
# ALUNO 5: Ricardo Tadeu        2101700
# ALUNO 6: Carlos Roberto       2020021


class Socio:
    def __init__(self, nome, cpf, nascimento, mes, ano):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.mes = mes
        self.ano = ano


class Clube:
    def __init__(self):
        self.socios = []

    def associar(self, socio):
        self.socios.append(socio)

    def numero_de_socios(self):
        return len(self.socios)

    def mes_associacao(self, mes, ano):
        contador = 0
        if mes not in range(1, 13):
            raise TypeError
        elif ano not in range(1000, 9999 + 1):
            raise ValueError
        else:
            for membro in self.socios:
                if membro.mes == mes and membro.ano == ano:
                    contador += 1
        return contador

    def expulsar(self, mes, ano):
        lista = []
        if mes not in range(1, 13):
            raise TypeError
        elif ano not in range(1000, 9999 + 1):
            raise ValueError
        else:
            lista_temp = self.socios.copy()
            for membro in lista_temp:
                if membro.mes == mes and membro.ano == ano:
                    lista.append(membro.nome)
                    self.socios.remove(membro)
            lista.sort()
        return lista
