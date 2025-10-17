# IMPORTAR BIBLIOTECAS
import customtkinter as ctk
import subprocess

ctk.set_appearance_mode("dark")
ctk.set_default_color_teme("green")

# CRIA A CLASSE PRINCIPAL DO NOSSO APP
class TerminalApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Terminal CLI")
        self.geometry("600x400")

        # JANELA DE SAÍDA
        self.terminal = ctk.CTkTextbox(self, height=100, wrap="word")
        self.terminal.pack(padx=10, pady=10, fill="both", expand=True)
        self.terminal.insert("end", "Terminal iniciado...\n")
        self.terminal.configure(state="disabled")  # faz com que seja somente leitura

        # ENTRADA DE COMANDOS
        self.command_entry = ctk.CTkEntry(self, placeholder_text="Digite um comando.")
        self.command_entry.pack(padx=10, pady=(0, 10), fill="x")
        self.command_entry.bind("<Return>", self.run_command)

    def run_command(self, event=None):
        command = self.command_entry.get().strip()
        if command:
            self.output_box.configure(state="normal")
            self.output_box.insert("end", f"> {command}\n")
            try:
                result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            except subprocess.CalledProcessError as e:
                result = e.output
            self.output_box.insert("end", result + "\n")
            self.output_box.see("end")
            self.output_box.configure(state="disabled")
            self.command_entry.delete(0, "end")

if __name__ == "__main__":
    app = TerminalApp()
    app.mainloop()
