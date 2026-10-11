def exibir_menu_autor():
    print("\n" + "-" * 30)
    print("    GERENCIAR AUTOR")
    print("-" * 30)
    print("1. Cadastrar autor")
    print("2. Listar autores")
    print("3. Atualizar autor")
    print("4. Excluir autor")
    print("5. Voltar ao menu principal")
    print("-" * 30)
    return input("Escolha uma opção: ").strip()


def solicitar_dados_autor():
    nome = input("Digite o nome do autor: ").strip()
    nacionalidade = input("Digite a nacionalidade do autor: ").strip()
    return nome, nacionalidade


def solicitar_id_autor():
    try:
        return int(input("Digite o ID do autor: "))
    except ValueError:
        print("\n[ERRO]: ID inválido! Digite um número inteiro.")
        return None


def mostrar_autores(autores):
    if not autores:
        print("\nNenhum autor encontrado.")
        return

    print("\n--- LISTA DE AUTORES ---")
    for autor in autores:
        # Assumindo retorno do BD como tupla: (id, nome, nacionalidade)
        print(f"ID: {autor[0]} | Nome: {autor[1]} | Nacionalidade: {autor[2]}")


def mensagem(msg):
    """Exibe mensagens de feedback para o usuário."""
    print(f"\n>> {msg}")