# 4) Sistema de Gerenciamento de Eventos Você está criando um sistema para gerenciar conferências. 
# Uma Conferencia possui uma lista de Palestrantes. Um palestrante é uma pessoa que pode participar de várias conferências 
# diferentes ao longo do tempo e seu cadastro deve permanecer no sistema independentemente das conferências. 
# Implemente as classes Conferencia e Palestrante, aplicando o relacionamento correto entre elas.

class Palestrante:
    def __init__(self, nome, id_palestrante):
        self.nome = nome
        self.id_palestrante = id_palestrante
        self._conferencias = [] 

    def __str__(self):
        return f"Palestrante(ID: {self.id_palestrante}, Nome: {self.nome})"

    def adicionar_conferencia(self, conferencia):
        if conferencia not in self._conferencias:
            self._conferencias.append(conferencia)

    @property
    def conferencias(self):
        return self._conferencias


class Conferencia:
    def __init__(self, nome, data, local, id_conferencia):
        self.nome = nome
        self.data = data
        self.local = local
        self.id_conferencia = id_conferencia
        self.palestrantes = [] 

    def adicionar_palestrante(self, palestrante):
        if palestrante not in self.palestrantes:
            self.palestrantes.append(palestrante)
            palestrante.adicionar_conferencia(self)



palestrante = Palestrante("Beatriz", 13)

conferencia = Conferencia("Cibersegurança", "2025-05-10", "São Paulo", 173)
conferencia.adicionar_palestrante(palestrante)

print("Palestrantes da conferência:")
for p in conferencia.palestrantes:
    print(p)

print("\nConferências da Beatriz:")
for conf in palestrante.conferencias:
    print(conf.nome)

