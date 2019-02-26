import datetime


class Pessoa:
    renda = None

    def __init__(self, nome,  sexo, data_nascimento):  # Construtor / Visbilidade (atributos publicos)
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento

    def get_idade(self):
        idade = int(datetime.datetime.now().year) - int(datetime.date.replace(self.data_nascimento).year)
        return idade

    def set_renda(self, valor):
        self.renda = valor
