"""
módulo: jogador.py

Este módulo contém a classe e funções responsáveis pela definição do jogador.

Dependências:
- ctkLine
"""

from modulos.ctkLine import ctkLine

class Mika:
    """
    Representa o personagem principal do jogo e o que o usuário utiliza.

    Atributos:
    - nome (str): nome do personagem.
    - hp (int): pontos de vida.
    - max_hp (int): a quantidade máxima de pontos de vida que o personagem pode ter.
    - inventario (lista): lista de itens que o personagem possui.

    Métodos:
    - add_item(item): adiciona itens no inventário do jogador.
    """

    def __init__(self):
        self.nome = 'Mika'
        self.hp = 10
        self.max_hp = 10
        inventario = ['Amuleto']
        self.inventario = inventario

    # --- INVENTÁRIO ---
    def add_item(self, item):
        """
        Adiciona um item no inventário do jogador (Mika).

        Parâmetros:
        - item (str): nome do item a ser adicionado.
        """
        self.inventario.append(item)


Mika = Mika()