import datetime


class Pessoa:
    def __init__(self, nome,  sexo, data_nascimento):  # Construtor - Encapsulamento de atributos pubicos
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento

    def get_idade(self):
        idade = int(datetime.datetime.now().year) - int(datetime.date.replace(self.data_nascimento).year)
        return idade
