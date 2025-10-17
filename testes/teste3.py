# IMPORTAR BIBLIOTECA
import customtkinter as ctk

# DEFININDO VARIÁVEIS DAS CORES
bg_color = '#000000'
txt_color_output = '#92EC47'
txt_color_input = '#FDFFFC'

# DECLARANDO AS CORES PADRÕES
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# DEFINE A CLASSE DO JOGO
class AppJogo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Jogo no Terminal")
        self.geometry("600x400")
        self.config(background=bg_color)

        # Área de texto
        self.terminal = ctk.CTkTextbox(self, height=100, wrap="word", text_color=txt_color_output)
        self.terminal.pack(padx=10, pady=10, fill="both", expand=True)
        self.terminal.configure(state="disabled")

        # Campo de entrada
        self.entry = ctk.CTkEntry(self, placeholder_text="Digite aqui", text_color=txt_color_input)
        self.entry.pack(padx=10, pady=(0, 10), fill="x")
        self.entry.bind("<Return>", self.processar_input)
        self.entry.configure(state="disabled")  # bloqueado no início

        # Variável de controle
        self.estado_jogo = "inicio"

        # Começa o jogo
        self.mostrar_texto('INICIANDO JOGO ...')
        self.after(0, self.menu)

    def menu(self):
        self.mostrar_texto('='*10 + ' MENU ' + '='*10)
        self.mostrar_texto('1. Carregar jogo \n2. Salvar jogo \n3. Começar do início \n4. Sair')


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

if __name__ == "__main__":
    app = AppJogo()
    app.mainloop()
