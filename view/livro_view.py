def exibir_menu_livro():
    print("\n" + "-" * 30)
    print("    GERENCIAR LIVRO")
    print("-" * 30)
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Atualizar livro")
    print("4. Excluir livro")
    print("5. Voltar ao menu principal")
    print("-" * 30)
    return input("Escolha uma opção: ").strip()


def solicitar_dados_livro():
    titulo = input("Digite o título do livro: ").strip()
    try:
        ano_publicacao = int(input("Digite o ano de publicação: "))
        id_autor = int(input("Digite o ID do autor associado: "))
        return titulo, ano_publicacao, id_autor
    except ValueError:
        print("\n[ERRO]: Ano e ID do autor devem ser números inteiros.")
        return None, None, None


def solicitar_id_livro():
    try:
        return int(input("Digite o ID do livro: "))
    except ValueError:
        print("\n[ERRO]: ID inválido! Digite um número inteiro.")
        return None


def mostrar_livros(livros):
    if not livros:
        print("\nNenhum livro encontrado.")
        return

    print("\n--- LISTA DE LIVROS ---")
    for livro in livros:
        # Assumindo retorno com JOIN: (id, titulo, ano_publicacao, nome_autor)
        print(f"ID: {livro[0]} | Título: {livro[1]} | Ano: {livro[2]} | Autor: {livro[3]}")


def mensagem(msg):
    """Exibe mensagens de feedback para o usuário."""
    print(f"\n>> {msg}")