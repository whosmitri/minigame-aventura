"""
módulo: ctkLine.py

Este módulo contém a classe que permite fazer o tratamento de entrada e saída de texto da interface gráfica.
Contém as funções mostrar_texto(texto), esperar_resposta(), bloquear_input() e processar_input().
"""

class ctkLine:
    """
    É uma forma de 

    Atributos:
    - nenhum.

    Métodos:
    - mostrar_texto(texto):
    - esperar_resposta():
    - bloquear_input():
    - processar_input():
    """

    def mostrar_texto(self, texto):
        """
        Mostra os textos na tela do CustomTkinter, deve funcionar como a função "print()".

        Parâmetros:
        - texto (str): dados a serem colocados na tela.
        """
        
        self.terminal.configure(state="normal")
        self.terminal.insert("end", texto + "\n\n")
        self.terminal.see("end")
        self.terminal.configure(state="disabled")
    
    def esperar_resposta(self):
        """
        a
        """

        self.entry.configure(state="normal")
        self.entry.delete(0, "end")
        self.entry.focus()

    def bloquear_input(self):
        """
        Bloqueia a entrada de texto, assim o usuário não pode digitar nada e não interrompe o funcionamento do programa.
        """

        self.entry.configure(state="disabled")

    def processar_input(self, event=None):
        """
        Recebe a informação do usuário e guarda em "resposta" para fazer o tratamento do dado futuramente.
        """

        resposta = self.entry.get()
        self.bloquear_input()
        self.mostrar_texto(f"> {resposta}")
        self.entry.delete(0, "end")

        if self.estado_jogo:
            self.estado_jogo(resposta)