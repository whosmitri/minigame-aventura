from modulos.ctkLine import ctkLine
import modulos.jogador as jogador

if ('Verdade Humana' in jogador.Mika.inventario) and ('Coração do Mundo Verde' in jogador.Mika.inventario) and ('Memória do Arquimago' in jogador.Mika.inventario):
    print('Há uma missão secundária disponível. \n[1] SEGUIR EM MISSÃO PRINCIPAL \n[2] AVANÇAR EM MISSÃO SECUNDÁRIA')

print(jogador.Mika.inventario)
