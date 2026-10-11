from model.database import Database

class LivroModel:

    def inserir_livro(self, titulo, ano_publicacao, id_autor):
        sql = "INSERT INTO livro (titulo, ano_publicacao, autor_id) VALUES (%s, %s, %s);"
        
        with Database.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, (titulo, ano_publicacao, id_autor))
                conn.commit()

    def listar_livros(self):
        # Utiliza JOIN para buscar o nome do autor associado ao livro
        sql = """
            SELECT l.id, l.titulo, l.ano_publicacao, a.nome
            FROM livro l
            JOIN autor a ON l.autor_id = a.id
            ORDER BY l.id;
        """
        
        with Database.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()

    def atualizar_livro(self, id_livro, titulo, ano_publicacao, id_autor):
        sql = """
            UPDATE livro 
            SET titulo = %s, ano_publicacao = %s, autor_id = %s 
            WHERE id = %s;
        """
        
        with Database.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, (titulo, ano_publicacao, id_autor, id_livro))
                conn.commit()

    def excluir_livro(self, id_livro):
        sql = "DELETE FROM livro WHERE id = %s;"
        
        with Database.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, (id_livro,))
                conn.commit()











