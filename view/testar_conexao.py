from model.database import Database

def testar():
    try:
        print("Tentando conectar ao PostgreSQL...")
        
        # Tenta obter a conexão usando as configurações do seu database.py
        conn = Database.get_connection()
        cursor = conn.cursor()
        
        # Executa uma consulta simples para obter a versão do PostgreSQL
        cursor.execute("SELECT version();")
        versao_db = cursor.fetchone()
        
        print("\n" + "=" * 50)
        print("✅ CONEXÃO REALIZADA COM SUCESSO!")
        print(f"Versão do PostgreSQL: {versao_db[0]}")
        print("=" * 50 + "\n")
        
        cursor.close()
        conn.close()

    except Exception as erro:
        print("\n" + "=" * 50)
        print("❌ ERRO AO CONECTAR AO BANCO DE DADOS!")
        print(f"Detalhe do erro: {erro}")
        print("=" * 50 + "\n")

if __name__ == "__main__":
    testar()

