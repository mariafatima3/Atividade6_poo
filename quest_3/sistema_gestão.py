# 3) Sistema de Gestão Acadêmica Uma Universidade é organizada em vários Departamentos 
# (ex: Departamento de Ciência da Computação, Departamento de Letras). Cada departamento pertence a uma única universidade. 
# Se a universidade for extinta, seus departamentos deixam de existir. 
# Implemente as classes Universidade e Departamento, aplicando o relacionamento correto entre elas.

class Departamento:
    def __init__(self, nome, universidade):
        self.nome = nome
        self.universidade = universidade  # Corrigido

    def __str__(self):
        return f"Departamento: {self.nome} (Universidade: {self.universidade.nome})"

class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.departamentos = []

    def adicionar_departamento(self, nome_departamento):
       
        departamento = Departamento(nome_departamento, self)
        self.departamentos.append(departamento)

    def listar_departamentos(self):
        print(f"Universidade: {self.nome}")
        for dep in self.departamentos:
            print(f"  - {dep}")


universidade = Universidade("UFCG")
universidade.adicionar_departamento("Ciência da Computação")
universidade.adicionar_departamento("Biologia")
universidade.listar_departamentos()
