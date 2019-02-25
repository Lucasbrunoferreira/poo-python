from pessoa import Pessoa


class Funcionario(Pessoa):  # Herança - Funcionario herda a classe Pessoa
    __salario = 975.00  # Encapsulamento - atributo privado

    def __init__(self, cargo, nome, sexo, data_nascimento):
        super().__init__(nome, sexo, data_nascimento)
        self.cargo = cargo

    def calcular_salario(self, horas_extras):
        valor_hora_extra = (self.__salario / 30) / 8
        total_salario = (horas_extras * valor_hora_extra) + self.__salario
        return total_salario
