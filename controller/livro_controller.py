from model.livro_model import LivroModel
from view.livro_view import (
    exibir_menu_livro,
    solicitar_dados_livro,
    solicitar_id_livro,
    mostrar_livros,
    mensagem
)

class LivroController:

    def __init__(self):
        self.model = LivroModel()

    def menu(self):
        """Gerencia o submenu em loop para Livro."""
        while True:
            opcao = exibir_menu_livro()

            if opcao == '1':
                self.cadastrar()
            elif opcao == '2':
                self.listar()
            elif opcao == '3':
                self.atualizar()
            elif opcao == '4':
                self.excluir()
            elif opcao == '5':
                break  # Voltar ao menu principal
            else:
                mensagem("Opção inválida! Tente novamente.")

    def cadastrar(self):
        try:
            titulo, ano_publicacao, id_autor = solicitar_dados_livro()

            if not titulo or not ano_publicacao or not id_autor:
                mensagem("Todos os campos do livro são obrigatórios!")
                return

            self.model.inserir_livro(titulo, ano_publicacao, id_autor)
            mensagem("Livro cadastrado com sucesso!")

        except Exception as e:
            mensagem(f"Erro ao cadastrar livro: {e}")

    def listar(self):
        try:
            livros = self.model.listar_livros()
            mostrar_livros(livros)

        except Exception as e:
            mensagem(f"Erro ao listar livros: {e}")

    def atualizar(self):
        try:
            id_livro = solicitar_id_livro()

            if id_livro is None:
                return

            titulo, ano_publicacao, id_autor = solicitar_dados_livro()
            if not titulo or not ano_publicacao or not id_autor:
                mensagem("Todos os campos são obrigatórios!")
                return

            self.model.atualizar_livro(id_livro, titulo, ano_publicacao, id_autor)
            mensagem("Livro atualizado com sucesso!")

        except Exception as e:
            mensagem(f"Erro ao atualizar livro: {e}")

    def excluir(self):
        try:
            id_livro = solicitar_id_livro()

            if id_livro is None:
                return

            self.model.excluir_livro(id_livro)
            mensagem("Livro excluído com sucesso!")

        except Exception as e:
            mensagem(f"Erro ao excluir livro: {e}")