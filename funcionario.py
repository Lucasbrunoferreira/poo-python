from pessoa import Pessoa


class Funcionario(Pessoa):  # Herança - Funcionario "é um(a)" Pessoa
    __salario = 975.00  # Encapsulamento - atributo privado

    def __init__(self, cargo, setor, qtd_dependentes, nome, sexo, data_nascimento):
        super().__init__(nome, sexo, data_nascimento)
        self.cargo = cargo
        self.setor = setor
        self.qtd_dependentes = qtd_dependentes

    def calcular_salario(self, horas_extras):
        valor_hora_extra = (self.__salario / 30) / 8
        total_salario = (horas_extras * valor_hora_extra) + self.__salario
        self.set_renda(total_salario)
        return total_salario

    def set_renda(self, valor):  # Polimorfismo
        if self.qtd_dependentes > 0:
            bonificacao = self.qtd_dependentes * 80
            self.renda = bonificacao + valor
        else:
            pass

    def get_setor(self):
        return self.setor.nome
