# 2) Sistema de Prontuário Médico Em um sistema hospitalar, o CorpoHumano é composto por vários sOrgao (Coração, Pulmão, Fígado, etc.).
# Um órgão não pode existir de forma independente do corpo ao qual pertence. 
# Se o registro do corpo for removido (em um sistema de simulação, por exemplo), os registros de seus órgãos também devem ser. 
# Implemente as classes CorpoHumano e Orgao, aplicando o relacionamento correto entre elas.

class Orgao:
    def __init__(self, nome):
        self.nome = nome
        
    def __str__(self):
        return f"Órgão: {self.nome}"


class CorpoHumano:
    def __init__(self, nome):
        self.nome = nome
        self.orgaos = []

    def adicionar_orgao(self, orgao_nome):
        orgao = Orgao(orgao_nome)
        self.orgaos.append(orgao)

    def listar_orgaos(self):
        for orgao in self.orgaos:
            print(orgao)

    def __del__(self):

        print(f"Corpo {self.nome} removido, órgãos também foram destruídos.")
        self.orgaos.clear()


corpoHumano = CorpoHumano("Carlos")

corpoHumano.adicionar_orgao("Coração")
corpoHumano.adicionar_orgao("Pulmão")
corpoHumano.adicionar_orgao("Fígado")

corpoHumano.listar_orgaos

