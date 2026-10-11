from model.autor_model import AutorModel
from view.autor_view import (
    exibir_menu_autor,
    solicitar_dados_autor,
    solicitar_id_autor,
    mostrar_autores,
    mensagem
)

class AutorController:

    def __init__(self):
        self.model = AutorModel()

    def menu(self):
        """Gerencia o submenu em loop para Autor."""
        while True:
            opcao = exibir_menu_autor()

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
            nome, nacionalidade = solicitar_dados_autor()

            if not nome or not nacionalidade:
                mensagem("Nome e nacionalidade são obrigatórios!")
                return

            self.model.inserir_autor(nome, nacionalidade)
            mensagem("Autor cadastrado com sucesso!")

        except Exception as e:
            mensagem(f"Erro ao cadastrar autor: {e}")

    def listar(self):
        try:
            autores = self.model.listar_autores()
            mostrar_autores(autores)

        except Exception as e:
            mensagem(f"Erro ao listar autores: {e}")

    def atualizar(self):
        try:
            id_autor = solicitar_id_autor()

            if id_autor is None:
                return

            nome, nacionalidade = solicitar_dados_autor()
            if not nome or not nacionalidade:
                mensagem("Nome e nacionalidade são obrigatórios!")
                return

            self.model.atualizar_autor(id_autor, nome, nacionalidade)
            mensagem("Autor atualizado com sucesso!")

        except Exception as e:
            mensagem(f"Erro ao atualizar autor: {e}")

    def excluir(self):
        try:
            id_autor = solicitar_id_autor()

            if id_autor is None:
                return

            self.model.excluir_autor(id_autor)
            mensagem("Autor excluído com sucesso!")

        except Exception as e:
            mensagem(f"Erro ao excluir autor: {e}")




