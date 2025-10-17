import customtkinter as ctk

class MenuJogo(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Menu do Jogo")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="="*10 + " MENU " + "="*10, font=("Arial", 20))
        self.label.pack(pady=10)

        botoes_frame = ctk.CTkFrame(self)
        botoes_frame.pack(pady=10)

        # Botões para as opções
        self.botao1 = ctk.CTkButton(botoes_frame, text="1. Carregar Jogo", command=self.carregar_jogo)
        self.botao1.pack(side=ctk.LEFT, pady=5)

        self.botao2 = ctk.CTkButton(botoes_frame, text="2. Salvar Jogo", command=self.salvar_jogo)
        self.botao2.pack(side=ctk.LEFT, pady=5)

        self.botao3 = ctk.CTkButton(botoes_frame, text="3. Começar do Início", command=self.comecar_jogo)
        self.botao3.pack(side=ctk.LEFT, pady=5)

        self.botao4 = ctk.CTkButton(botoes_frame, text="4. Sair", command=self.sair)
        self.botao4.pack(side=ctk.LEFT, pady=5)

        # Terminal de saída
        self.terminal = ctk.CTkTextbox(self, height=100, wrap="word")
        self.terminal.pack(pady=10, padx=10, fill="both", expand=True)
        self.terminal.configure(state="disabled")

    def mostrar_texto(self, texto):
        self.terminal.configure(state="normal")
        self.terminal.insert("end", texto + "\n")
        self.terminal.see("end")
        self.terminal.configure(state="disabled")

    def carregar_jogo(self):
        self.mostrar_texto("Jogo carregado.")

    def salvar_jogo(self):
        self.mostrar_texto("Jogo salvo.")

    def comecar_jogo(self):
        self.mostrar_texto("Começando do início...")

    def sair(self):
        self.mostrar_texto("Saindo do jogo.")
        self.after(1000, self.destroy)  # Espera 1 segundo e fecha

if __name__ == "__main__":
    app = MenuJogo()
    app.mainloop()
