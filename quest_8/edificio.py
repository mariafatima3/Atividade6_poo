# 8) Sistema de Cadastro Imobiliário Um Edificio é composto por múltiplos Apartamentos. 
# Cada apartamento está fisicamente contido em um único edifício e não pode existir de forma independente. 
# Se o registro do edifício for removido do sistema, os registros de todos os seus apartamentos também devem ser. 
# Implemente as classes Edificio e Apartamento, aplicando o relacionamento correto entre elas.

class Apartamento:
    def __init__(self, numero, andar, tamanho, edificio):
        self.numero = numero
        self.andar = andar
        self.tamanho = tamanho
        self.edificio = edificio  
    
    def __str__(self):
        return f"Apartamento {self.numero}, Andar: {self.andar}, Tamanho: {self.tamanho}m², Edifício: {self.edificio.nome}"
    
class Edificio:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.apartamentos = []

    def adicionar_apartamento(self, numero, andar, tamanho):
        apartamento = Apartamento(numero, andar, tamanho, self)
        self.apartamentos.append(apartamento)
        
    def remover_apartamento(self, numero):
        self.apartamentos = [apt for apt in self.apartamentos if apt.numero != numero]

    def listar_apartamentos(self):
        if not self.apartamentos:
            print("Nenhum apartamento cadastrado.")
        else:
            for apartamento in self.apartamentos:
                print(apartamento)

    def __str__(self):
        return f"Edifício {self.nome}, Endereço: {self.endereco}, Total de Apartamentos: {len(self.apartamentos)}"


edificio = Edificio("Residencial Porto do Sol","Rua Severino Tomaz de Aquino")
edificio.adicionar_apartamento(18, 1, 80)
edificio.adicionar_apartamento(20, 1, 75)

print(edificio)
edificio.listar_apartamentos()

edificio.remover_apartamento(18)
print("\nApós remover o apartamento 18:")
edificio.listar_apartamentos()

del edificio 

        