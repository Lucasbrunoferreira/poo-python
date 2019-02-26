import datetime

from funcionario import Funcionario
from folha_pagamento import FolhaDePagamento
from setor import Setor


cecy = Funcionario(nome="Cecilya",
                   setor=None,
                   data_nascimento=datetime.date(1999, 5, 14),
                   sexo="Feminino",
                   cargo="Gerente",
                   qtd_dependentes=1)


setor_dev = Setor(nome="Desenvolvimento", pausa_cafe="15:30", gerente=cecy)
# Agregação - Setor possui um gerente (Funcionario), e ambos existem sem depender da existencia do outro.


lucas = Funcionario(nome="Lucas Bruno",
                    data_nascimento=datetime.date(1997, 11, 20),
                    sexo="Masculino",
                    cargo="Analista de desenvolvimento",
                    setor=setor_dev,
                    qtd_dependentes=3)  # Composição - Funcionario tem um setor, e setor não existe sem funcionario(s).


folha_pagamento_lucas = FolhaDePagamento(funcionario=lucas, possui_plano_saude=True)

# print(lucas.__salario) Assim como esperado, não é possivél acessar atributos privados diretamente.

print(lucas.nome, lucas.data_nascimento, lucas.sexo, lucas.cargo)  # acessando atributos publicos

print(lucas.get_idade())  # acessando metodos da classe

print(folha_pagamento_lucas.imprimir_folha())

