# from model.autor_model import AutorModel
# autor_model = AutorModel()
# print("Tentando inserir um autor...")
# autor_model.inserir_autor("Machado de Assis", "Brasileira")
# print("Autor inserido com sucesso!")
# autores = autor_model.listar_autores()
# print("\nLista de autores no banco:")
# for autor in autores:
#     print(autor)


from controller.autor_controller import AutorController
from controller.livro_controller import LivroController
# Se você tiver uma função de menu principal na view, pode importá-la assim:
# from view.principal_view import menu_principal


def main():
    autor_controller = AutorController()
    livro_controller = LivroController()

    while True:
        try:
            # Caso ainda não tenha criado uma view principal separada, 
            # pode usar o print direto ou importar da view:
            print("\n" + "=" * 40)
            print("       BIBLIOTECA UNIVERSITÁRIA")
            print("=" * 40)
            print("1. Gerenciar Autores")
            print("2. Gerenciar Livros")
            print("0. Sair")
            print("=" * 40)
            
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                autor_controller.menu()

            elif opcao == "2":
                livro_controller.menu()

            elif opcao == "0":
                print("Saindo do sistema...")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()