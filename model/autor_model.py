
from model.database import Database

class AutorModel:

    def inserir_autor(self, nome, nacionalidade):
        sql = "INSERT INTO autor (nome, nacionalidade) VALUES (%s, %s);"
        
        with Database.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, (nome, nacionalidade))
                conn.commit()

    def listar_autores(self):
        sql = "SELECT id, nome, nacionalidade FROM autor ORDER BY id;"
        
        with Database.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()

    def atualizar_autor(self, id_autor, nome, nacionalidade):
        sql = "UPDATE autor SET nome = %s, nacionalidade = %s WHERE id = %s;"
        
        with Database.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, (nome, nacionalidade, id_autor))
                conn.commit()

    def excluir_autor(self, id_autor):
        sql = "DELETE FROM autor WHERE id = %s;"
        
        with Database.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, (id_autor,))
                conn.commit()