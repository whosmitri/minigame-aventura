"""
módulo: main.py

Este módulo contém as funcionalidades principais do jogo, como a interface gráfica, e é um meio de integração.

Dependências:
- CustomTkinter
- ctkLine
- fases
- jogador
"""

# --- BIBLIOTECA E MÓDULOS ---
import customtkinter as ctk

from modulos.ctkLine import ctkLine
import modulos.fases as fases
import modulos.jogador as jogador


# --- DEFININDO VARIÁVEIS DAS CORES ---
bg_color = '#000000'
color_white = '#FDFFFC'
color_gray = '#DCDCDC'
color_darkgray = '#A9A9A9'
color_black = '#222021'

# --- DECLARANDO AS CORES PADRÕES ---
ctk.set_appearance_mode("dark")

# --- JOGO ---
class AppJogo(ctk.CTk, ctkLine):
    def __init__(self):
        super().__init__()
        self.title('MiniGame Aventura')
        self.geometry("650x400")
        self.config(background=bg_color) # formata a cor de fundo


        # --- MENU: BOTÕES ---
        botoes_frame = ctk.CTkFrame(self, fg_color=bg_color)   # criamos um frame para separar os botões da parte principal da aplicação (saída terminal + entrada)
        botoes_frame.pack(pady=10)

        self.botao1 = ctk.CTkButton(botoes_frame, fg_color=color_gray, hover_color=color_darkgray, text_color=color_black, text='1. Carregar Jogo', command=self.carregar_jogo)
        self.botao1.pack(side=ctk.LEFT, padx=10, pady=5)

        self.botao2 = ctk.CTkButton(botoes_frame, fg_color=color_gray, hover_color=color_darkgray, text_color=color_black, text='2. Salvar Jogo', command=self.salvar_jogo)
        self.botao2.pack(side=ctk.LEFT, padx=10, pady=5)

        self.botao3 = ctk.CTkButton(botoes_frame, fg_color=color_gray, hover_color=color_darkgray, text_color=color_black, text='3. Começar do Início', command=self.comecar_inicio)
        self.botao3.pack(side=ctk.LEFT, padx=10, pady=5)

        self.botao4 = ctk.CTkButton(botoes_frame, fg_color=color_gray, hover_color=color_darkgray, text_color=color_black, text='4. Sair', command=self.sair)
        self.botao4.pack(side=ctk.LEFT, padx=10, pady=5)


        # --- SAÍDA TERMINAL ---
        self.terminal = ctk.CTkTextbox(self, height=100, wrap='word', fg_color=bg_color, text_color=color_white, font=('Consolas', 15))
        self.terminal.pack(padx=10, pady=10, fill='both', expand=True)
        self.terminal.configure(state='disabled')


        # --- ENTRADA DE TEXTO ---
        self.entry = ctk.CTkEntry(self, placeholder_text='Digite aqui', text_color=color_white, font=('Consolas', 15))
        self.entry.pack(padx=10, pady=(0, 10), fill="x")
        self.entry.bind("<Return>", self.processar_input)
        self.entry.configure(state="disabled")

        # --- MENU: TEXTO ---
        self.mostrar_texto('='*20 + '\nMiniGame Aventura \n' + '='*20)
        self.mostrar_texto('> Bem-Vindo \n> Recomenda-se o uso de papel e caneta para anotações!')


        # --- MENU: INSTRUÇÃO DE COMO FUNCIONAM OS BOTÕES ---
        self.mostrar_texto('Sobre os botões: \n1. Carregar Jogo: carrega o seu último salvamento. \n2. Salvar Jogo: salva o estado atual do jogo (seus status de jogador e fase atual). \n3. Começar do Início: começa do início independente do seu progresso atual. \n4. Sair: sai sem salvar, cuidado!')


        # --- CONTROLE DE FASES ---
        self.fase_atual = 0

        self.fases = {
            1: fases.Missao1,
            2: fases.Missao2,
            3: fases.Missao3, 	# incompleto
            4: fases.Missao4,
            5: fases.Secundaria1,
            6: fases.Missao5,
            7: fases.Missao6,
            8: fases.Secundaria2,
            9: fases.Secundaria3,
            10: fases.Missao7, 	# incompleto
            11: fases.Fim
        }

    def iniciar_fase(self, numero):
        fase_classe = self.fases.get(numero)
        if fase_classe:
            self.fase_atual = numero
            self.fase_iniciar = fase_classe(self)
            self.fase_iniciar.iniciar()
        else:
            self.mostrar_texto("Fase não encontrada.")


    # --- FUNÇÕES DOS BOTÕES ---
    def carregar_jogo(self):
        self.mostrar_texto('='*20 + '\nJogo carregado. Iniciando de onde parou...\n' + '='*20)
        self.start = self.iniciar_fase(6)
        self.after(1000, lambda: self.start)

    def salvar_jogo(self):
        self.mostrar_texto('='*20 + '\nJogo salvo.\n' + '='*20)

    def comecar_inicio(self):
        self.mostrar_texto('='*20 + '\nComeçando do início...\n' + '='*20)
        self.after(1000, lambda: self.iniciar_fase(1))
        
    def sair(self):
        self.mostrar_texto('='*20 + '\nSaindo do jogo.\n' + '='*20)
        self.after(1000, self.destroy)