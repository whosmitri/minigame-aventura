import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class JogoTerminal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Jogo no Terminal")
        self.geometry("600x400")

        # Área de texto
        self.terminal = ctk.CTkTextbox(self, height=300, wrap="word")
        self.terminal.pack(padx=10, pady=10, fill="both", expand=True)
        self.terminal.configure(state="disabled")

        # Campo de entrada
        self.entry = ctk.CTkEntry(self, placeholder_text="Aguardando...")
        self.entry.pack(padx=10, pady=(0, 10), fill="x")
        self.entry.bind("<Return>", self.processar_input)
        self.entry.configure(state="disabled")  # bloqueado no início

        # Variável de controle
        self.estado_jogo = "inicio"

        # Começa o jogo
        self.mostrar_texto("Você acorda em uma cela escura, sem lembrar de nada.")
        self.mostrar_texto("Uma voz sussurra: 'Diga seu nome, prisioneiro.'")
        self.esperar_resposta("nome")

    def mostrar_texto(self, texto):
        self.terminal.configure(state="normal")
        self.terminal.insert("end", texto + "\n")
        self.terminal.see("end")
        self.terminal.configure(state="disabled")

    def esperar_resposta(self, estado):
        self.estado_jogo = estado
        self.entry.configure(state="normal")
        self.entry.delete(0, "end")
        self.entry.focus()

    def bloquear_input(self):
        self.entry.configure(state="disabled")

    def processar_input(self, event=None):
        resposta = self.entry.get().strip()
        self.bloquear_input()
        self.mostrar_texto(f"> {resposta}")
        self.entry.delete(0, "end")

        # Lógica baseada no estado atual do jogo
        if self.estado_jogo == "nome":
            self.nome_jogador = resposta
            self.mostrar_texto(f"A voz repete: '{self.nome_jogador}... hmm... nome forte.'")
            self.mostrar_texto("Você vê uma chave no chão. Pegar a chave? (sim/não)")
            self.esperar_resposta("pegar_chave")

        elif self.estado_jogo == "pegar_chave":
            if resposta.lower() == "sim":
                self.mostrar_texto("Você pega a chave. Ela brilha em sua mão.")
                self.mostrar_texto("A porta range lentamente ao ser destrancada...")
                self.mostrar_texto("FIM DO EXEMPLO.")
            elif resposta.lower() == "não":
                self.mostrar_texto("Você ignora a chave. A cela permanece trancada.")
                self.mostrar_texto("FIM DO EXEMPLO.")
            else:
                self.mostrar_texto("Resposta inválida. Tente novamente: (sim/não)")
                self.esperar_resposta("pegar_chave")

if __name__ == "__main__":
    app = JogoTerminal()
    app.mainloop()
