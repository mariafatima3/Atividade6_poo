# 10) Aplicativo de Transporte Em um aplicativo como Uber ou 99, um Motorista está associado a um Veiculo para realizar as viagens. 
# É importante que o sistema saiba qual veículo um motorista está usando no momento, e também qual motorista está dirigindo um determinado veículo. 
# Ambos, Motorista e Veiculo, têm ciclos de vida independentes. Implemente as classes Motorista e Veiculo, aplicando o relacionamento correto entre elas.

class Veiculo:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo
        self.motorista = None
    
    def __str__(self):
        return f"{self.modelo} ({self.placa})"

class Motorista:
    def __init__(self, nome, cnh):
        self.nome = nome
        self.cnh = cnh
        self.veiculo = None
    
    def dirigir(self, veiculo):
       
        if self.veiculo is not None:
            self.veiculo.motorista = None
    
        if veiculo.motorista is not None:
            veiculo.motorista.veiculo = None


        self.veiculo = veiculo
        veiculo.motorista = self

    def parar_de_dirigir(self):
        if self.veiculo:
            self.veiculo.motorista = None
            self.veiculo = None

    def __str__(self):
        return f"{self.nome} (CNH: {self.cnh})"


veiculo = Veiculo("FDC-3751", "Ford, F-150")
motorista = Motorista("José", 231764392)

motorista.dirigir(veiculo)

print(f"Motorista {motorista} está dirigindo o veículo {motorista.veiculo}")
print(f"Veículo {veiculo} está sendo dirigido por {veiculo.motorista}")

motorista.parar_de_dirigir()
print(f"Após parar: Motorista {motorista} está dirigindo {motorista.veiculo}, Veículo {veiculo} está sendo dirigido por {veiculo.motorista}")

