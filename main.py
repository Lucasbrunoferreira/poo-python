import datetime

from funcionario import Funcionario


lucas = Funcionario(nome="Lucas Bruno",
                    data_nascimento=datetime.date(1997, 11, 20),
                    sexo="Masculino",
                    cargo="Analista de desenvolvimento")


print(lucas.nome, lucas.data_nascimento, lucas.sexo, lucas.cargo)  # acessando atributos publicos

# print(lucas.__salario) Assim como esperado, não é possivél acessar atributos privados diretamente.

print(lucas.calcular_salario(horas_extras=36))

print(lucas.get_idade())
