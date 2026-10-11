import psycopg2


class Database:
    """Classe responsável por gerenciar a conexão com o PostgreSQL."""

    @staticmethod
    def get_connection():
        return psycopg2.connect(
            host="localhost",
            port=5432,
            database="biblioteca",
            user="postgres",
            password="postgres"  
        )

