# 6) Sistema de Gestão de Frotas Uma empresa de logística gerencia uma Frota de Veiculos. Os veículos pertencem à frota, mas podem ser vendidos, 
# transferidos para outra frota ou simplesmente removidos da frota atual sem que o objeto Veiculo seja destruído no sistema. 
# Implemente as classes Frota e Veiculo, aplicando o relacionamento correto entre elas.

class Veiculo:
    def __init__(self, id_veiculo, marca, modelo):
        self.id_veiculo = id_veiculo
        self.marca = marca
        self.modelo = modelo
    
    def __str__(self):
        return f"{self.id_veiculo} — {self.marca} — {self.modelo}"


class Frota:
    def __init__(self, nome):
        self.nome = nome
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        if veiculo not in self.veiculos:
            self.veiculos.append(veiculo)
            print(f"Veículo {veiculo} adicionado à frota {self.nome}.")
        else:
            print(f"Veículo {veiculo} já está na frota {self.nome}.")

    def remover_veiculo(self, veiculo):
        if veiculo in self.veiculos:
            self.veiculos.remove(veiculo)
            print(f"Veículo {veiculo} removido da frota {self.nome}.")
        else:
            print(f"Veículo {veiculo} não está na frota {self.nome}.")

    def listar_veiculos(self):
        print(f"Veículos na frota {self.nome}:")
        for v in self.veiculos:
            print(f"- {v}")


veiculo1 = Veiculo(1, "Toyota", "Corolla")
veiculo2 = Veiculo(2, "Ford", "F-150")
veiculo3 = Veiculo(3, "Honda", "Civic")
veiculo4 = Veiculo(4, "VW", "Gol")

frota1 = Frota("Frota A")
frota2 = Frota("Frota B")

frota1.adicionar_veiculo(veiculo1)
frota1.adicionar_veiculo(veiculo2)
print()

frota1.listar_veiculos()
print()

frota1.remover_veiculo(veiculo1)
print()

frota1.listar_veiculos()
print()

frota2.adicionar_veiculo(veiculo3)
frota2.adicionar_veiculo(veiculo4)
print()

frota2.listar_veiculos()

        