

class FolhaDePagamento:
    custoPlanoSaude = 104.90
    total_salario = None

    def __init__(self, funcionario, possui_plano_saude):
        self.funcionario = funcionario
        self.possui_plano_saude = possui_plano_saude

    def imprimir_folha(self):
        salario_funcionario = self.funcionario.calcular_salario(horas_extras=59)

        if self.possui_plano_saude:
            self.total_salario = salario_funcionario - self.custoPlanoSaude
        else:
            self.total_salario = salario_funcionario

        folha = 'Nome: {}     ' \
                'Cargo: {}    ' \
                'Setor: {}    ' \
                'Salario: {}  '.format(self.funcionario.nome,
                                       self.funcionario.cargo,
                                       self.funcionario.get_setor(),
                                       self.total_salario)

        return folha
