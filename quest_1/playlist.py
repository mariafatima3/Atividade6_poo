# 1) Sistema de Streaming de Música Você está modelando um sistema como o Spotify. Uma Playlist é uma coleção de Musicas. 
# Uma mesma música pode estar em várias playlists diferentes ou em nenhuma. 
# Se um usuário apagar uma playlist, as músicas que estavam nela não devem ser removidas do sistema.
# Implemente as classes Playlist e Musica, aplicando o relacionamento correto entre elas.

class Musica:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def __str__(self):
        return f"{self.titulo} — {self.artista}"


class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        if musica not in self.musicas:
            self.musicas.append(musica)

    def remover_musica(self, musica):
        if musica in self.musicas:
            self.musicas.remove(musica)

    def listar_musicas(self):
        print(f"Playlist: {self.nome}")
        for musica in self.musicas:
            print(" -", musica)



musica1 = Musica ("Sonda-me, Usa-me", "Missionário Shalom")
musica2 = Musica ("Tua Graça Me Basta", "Diante do Trono")
musica3 = Musica("Aclame ao Senhor", "Vencedores por Cristo")
musica4 = Musica("Eu Tenho a Senha", "João Gomes")

playlist = Playlist("Favoritas")

playlist.adicionar_musica(musica1)
playlist.adicionar_musica(musica2)
playlist.adicionar_musica(musica3)

playlist.remover_musica(musica4)

playlist.listar_musicas()