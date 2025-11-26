# 9) Sistema de Blog: Em um sistema de blog, um Post pode ter vários Comentarios. Os comentários são específicos de um post; eles não fazem sentido sem o post original. 
# Se um Post for apagado, todos os seus Comentarios devem ser apagados junto. Implemente as classes Post e Comentario, aplicando o relacionamento correto entre elas.

class Comentario:
    def __init__(self, autor, conteudo):
        self.autor = autor
        self.conteudo = conteudo
    
    def __str__(self):
        return f"{self.autor}: {self.conteudo}"

class Post:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo
        self.comentarios = []

    def adicionar_comentario(self, autor, conteudo):
        comentario = Comentario(autor, conteudo)
        self.comentarios.append(comentario)

    def mostrar_comentarios(self):
        if not self.comentarios:
            print("Nenhum comentário.")
        else:
            for c in self.comentarios:
                print(c)

    def __str__(self):
        return f"Post: {self.titulo}\n{self.conteudo}"

post1 = Post("Meu Primeiro Post", "Este é o conteúdo do post.")
post1.adicionar_comentario("João", "Muito bom!")
post1.adicionar_comentario("Beatriz", "Gostei do post!")

print(post1)
post1.mostrar_comentarios()

del post1
