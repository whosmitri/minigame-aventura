"""
módulo: fases.py

Este módulo contém as classes e funções principais para a lógica de fases do jogo.
Inclui a classe FasesBase com a função principal iniciar().
Cada fase é uma classe: Missao1(FasesBase), Missao2(FasesBase), Secundaria2(FasesBase), etc.

Dependências:
- ctkLine
- jogador
"""

from random import randint

from modulos.ctkLine import ctkLine
import modulos.jogador as jogador


class FasesBase:
    def __init__(self, jogo):
        self.jogo = jogo
    
    def iniciar(self):
        pass

    def mudar_fase(self):
        self.jogo.mostrar_texto('Escolha sua próxima ação: \n[1] PARAR \n[2] SEGUIR PARA PRÓXIMA FASE')

        self.jogo.estado_jogo = self.processar_mudar_fase
        self.jogo.esperar_resposta()

    def processar_mudar_fase(self, resposta):
        if (resposta == '1'):
            self.jogo.mostrar_texto('Você escolheu parar o jogo.')
        elif (resposta == '2'):
            self.jogo.mostrar_texto('Indo para a próxima fase...')
            self.jogo.fase_atual += 1
            self.jogo.iniciar_fase(self.jogo.fase_atual)
        else:
            self.jogo.mostrar_texto('Opção inválida. Tente novamente.')
            self.mudar_fase(self)


# --- MISSÕES PRINCIPAIS ---

# --- MISSÃO 1 ---
class Missao1(FasesBase):
    def iniciar(self):
        self.jogo.mostrar_texto('??? \n“Há muito tempo, o mundo era repleto de magia. Criaturas encantadas andavam entre os humanos, feitiços eram usados para curar, proteger e cultivar a terra. \nMas um dia, uma sombra tomou conta de tudo, ela trouxe desequilíbrio e destruição. \nA magia foi corrompida e os grandiosos Quatro Magos Fundadores tiveram que selá-la. A magia desapareceu. Ninguém mais sabia conjurar um feitiço, os livros mágicos se tornaram lendas, e os seres encantados sumiram sem deixar rastros. \nMas, Mika, meu querido, a magia nunca desaparece, ela se esconde, apenas esperando o momento certo para se revelar.”')
        self.jogo.after(4000, self.passo2)
    
    def passo2(self):
        self.jogo.mostrar_texto('Você acorda, sentindo o amuleto pulsar em seu peito, a memória de sua avó tão viva quanto ele. Você precisa desvendar o mistério do mundo por ela: Cassandra, sua avó. E ela te deu algumas instruções antes de partir.')
        self.jogo.after(2000, self.passo3)
    
    def passo3(self):
        self.jogo.mostrar_texto('Cassandra \n“Quando o amuleto brilhar, Mika, é o seu chamado para descobrir os segredos do passado. Confie nele e permita que ele o guie pelos caminhos onde a magia ainda sussurra”')
        self.jogo.after(2000, self.passo4)
    
    def passo4(self):
        self.jogo.mostrar_texto('Inspirado pelos antigos contos sobre a antiga magia de sua avó, você se levanta, pronto para mais um dia.')
        self.jogo.after(2000, self.passo5)
    
    def passo5(self):
        self.jogo.mostrar_texto('O seu amuleto começa a brilhar, em sintonia com a natureza.')
        self.jogo.mostrar_texto('Algumas flores começam a brilhar pelo caminho esquerdo.')
        self.jogo.after(2000, self.passo6)

    def passo6(self):
        self.jogo.mostrar_texto('Escolher caminho: \n[1] SEGUIR PARA DIREITA \n[2] SEGUIR PARA ESQUERDA')

        self.jogo.estado_jogo = self.processar_decisao
        self.jogo.esperar_resposta()

    def processar_decisao(self, decisao):
        if (decisao=='1'):
            self.jogo.mostrar_texto('Não é esse o caminho certo. Siga o amuleto.')
            self.jogo.after(1500, self.passo6)
        
        elif (decisao=='2'):
            self.jogo.mostrar_texto('O amuleto sempre vai te guiar pelo caminho certo, cabe a você decidir se vai escutá-lo.')
            self.jogo.mostrar_texto('Assim como os contos de sua avó, tomados como lendas por vários.')
            self.jogo.after(2000, self.passo7)
        
        else:
            self.jogo.after(1500, self.passo6)
            
    
    def passo7(self):
        self.jogo.mostrar_texto('Depois de um tempo andando, você avista uma pequena vila, um pouco isolada do resto do mundo...')

        self.jogo.after(3500, self.mudar_fase)



# --- MISSÃO 2 ---
class Missao2(FasesBase):
    def iniciar(self):
        self.jogo.mostrar_texto('Você adentra a Vila da Neblina, onde o silêncio é rei e os moradores falam apenas em sussurros.')
        self.jogo.after(2000, self.passo2)
    
    def passo2(self):
        self.jogo.mostrar_texto('As ruas são estreitas, cobertas por pedras úmidas. Há um clima de desconfiança no ar. Algo antigo e não dito permeia o lugar.')
        self.jogo.mostrar_texto('“Sinais”, cochicham os mais velhos. Mas ninguém ousa explicar o que são.')
        self.jogo.mostrar_texto('Há algo de inquieto naquele lugar. Algo que respira nas margens da realidade.')
        self.jogo.after(2000, self.passo3)
    
    def passo3(self):
        self.jogo.mostrar_texto('À frente, uma garotinha está parada, sozinha e melancólica. O olhar perdido entre o chão e as brumas.')
        self.jogo.after(2500, self.passo4)
    
    def passo4(self):
        self.jogo.mostrar_texto('Você se aproxima.')
        self.jogo.after(2000, self.passo5)
    
    def passo5(self):
        self.jogo.mostrar_texto('Mika \n“Olá, você está bem? Precisa de ajuda?”')
        self.jogo.after(2000, self.passo6)
    
    def passo6(self):
        self.jogo.mostrar_texto('Ela se vira devagar. A voz que sai é suave, mas carrega preocupação.')
        self.jogo.mostrar_texto('??? \n“Oh, sim, por favor, minhas ovelhas não param de sumir e não sei mais o que fazer, ninguém consegue descobrir o porquê!”')
        self.jogo.after(2000, self.passo7)
    
    def passo7(self):
        self.jogo.mostrar_texto('Mika \n(Talvez meu amuleto possa me dar alguma vantagem!) \n“Não se preocupe, eu posso te ajudar!!”')
        self.jogo.after(2000, self.passo8)
    
    def passo8(self):
        self.jogo.mostrar_texto('Stella \n“Muito obrigada, meu nome é Stella, eu vou te mostrar por onde ir.”')
        self.jogo.after(3500, self.passo9)
    
    def passo9(self):
        self.jogo.mostrar_texto('COMEÇA MISSÃO “AO RESGATE!” \nObjetivo: Ajude Stella com os desaparecimentos estranhos das ovelhas.')
        self.jogo.after(3500, self.passo10)
    
    def passo10(self):
        self.jogo.mostrar_texto('Ela aponta para os campos onde sempre levava as ovelhas para pastar. ')
        self.jogo.mostrar_texto('Stella \n“É aqui que eu trago as ovelhas todos os dias, mas algumas se afastam e eu não consigo mais encontrá-las, não estou mais conseguindo ficar em paz”')
        self.jogo.after(2000, self.passo11)
    
    def passo11(self):
        self.jogo.mostrar_texto('Você sente o amuleto a brilhar sutilmente, mas não entende direito porque ele faz isso, talvez aquilo era a magia?')
        self.jogo.mostrar_texto('Andando mais um pouco, você encontra algumas pegadas. Você decide segui-las antes que desapareçam na névoa e, à medida que avança, mais o seu amuleto brilha.')
        self.jogo.after(2000, self.passo12)
    
    def passo12(self):
        self.jogo.mostrar_texto('O rastro chega ao seu fim, mas o seu amuleto brilha indicando o caminho.')
        self.jogo.mostrar_texto('Durante a investigação, um homem se aproxima. Capa escura, pergaminhos e armas presos à cintura, olhos atentos.')
        self.jogo.after(2000, self.passo13)
        
    
    def passo13(self):
        self.jogo.mostrar_texto('Conversar com ele? \n[1] SIM \n[2] NÃO ')
        
        self.jogo.estado_jogo = self.processar_decisao
        self.jogo.esperar_resposta()

    def processar_decisao(self, decisao):
        if (decisao=='1'):
            self.jogo.mostrar_texto('??? \n“Que incrível a sua joia. Haha, não se preocupe, sou só uma viajante. Me diga, você também ouviu os sussurros? Eu vou te contar: este lugar já carregava feridas antes mesmo da névoa chegar. Há registros antigos... de fendas entre mundos... e de entidades que se comunicam por meio de ecos e símbolos.” ')
            self.jogo.after(4000, self.decisao1_passo14)

        elif (decisao=='2'):
            self.jogo.mostrar_texto('O homem te observa de relance, mas continua seu caminho. ')
            self.jogo.after(2000, self.passo15)
        
        else:
            self.jogo.after(1500, self.passo13)
    

    def decisao1_passo14(self):
        self.jogo.mostrar_texto('Eron \n“Eu sou o Eron, eu te vi com aquela garota e preciso dizer que se você quiser proteger esta vila, comece pelas fendas.”')
        self.jogo.mostrar_texto('Ele permanece em silêncio e você se afasta.')
        self.jogo.after(2500, self.passo15)
    
    def passo15(self):
        self.jogo.mostrar_texto('Você ouve um balido distante... e um segundo depois, mais nada.')
        self.jogo.after(3000, self.passo16)
    
    def passo16(self):
        self.jogo.mostrar_texto('Então você avista uma fenda na terra, escondia com raízes, seu amuleto brilha mais do que nunca. Vendo o que tinha lá dentro: espíritos antigos, despertados por ecos de magia esquecida. Eles estavam confundindo as ovelhas com seres encantados de outrora. Não queriam machucar, apenas lembrar... ')
        self.jogo.after(3000, self.passo17)
    
    def passo17(self):
        self.jogo.mostrar_texto('Você consegue recuperar as ovelhas e levá-las de volta a Stella. ')
        self.jogo.after(2000, self.passo18)
    
    def passo18(self):
        self.jogo.mostrar_texto('Stella \n“Não acredito que você conseguiu! Muito obrigada!!”')
        self.jogo.mostrar_texto('Ela sorri gentilmente para você. ')

        self.jogo.after(2000, self.passo19)
    
    def passo19(self):
        self.jogo.mostrar_texto('Stella \n“Eu sabia que ainda tinha um jeito, se prestarmos atenção, cada pegada na terra, cada sussurro no vento pode ser a pista que precisamos para salvar o que ainda resta de vida neste lugar” ')
        self.jogo.after(2000, self.passo20)
    
    def passo20(self):
        self.jogo.mostrar_texto('Você se despede de Stella, sabe que é hora de continuar sua missão e tem a certeza de que a magia é real e sua volta está afetando até as regiões mais afastadas.')

        self.jogo.after(3500, self.mudar_fase)



# --- MISSAO 3 ---
class Missao3(FasesBase):
    def iniciar(self):
        self.jogo.mostrar_texto('O amuleto brilha novamente, indicando o caminho, e você decide segui-lo. ')
        self.jogo.after(3500, self.passo2)

    def passo2(self):
        self.jogo.mostrar_texto('Até que você chega na Aldeia de Runna.')
        self.jogo.mostrar_texto('Logo ao entrar alguém esbarra em você, um pequeno e jovem garoto.')
        self.jogo.after(2000, self.passo3)

    def passo3(self):
        self.jogo.mostrar_texto('??? \n“Me desculpe! Eu estou indo para uma reunião importante!”')
        self.jogo.after(2000, self.passo4)

    def passo4(self):
        self.jogo.mostrar_texto('Mika \n(Aqui parece um lugar bem mais vivo que a Vila da Neblina...) \n“Tá tudo bem, estou apenas de passagem, sou o Mika.”')
        self.jogo.after(2000, self.passo5)

    def passo5(self):
        self.jogo.mostrar_texto('Tomel \n“É um prazer te conhecer, eu sou o Tomel! O mais novo membro do Conselho da Névoa!”')
        self.jogo.after(2000, self.passo6)

    def passo6(self):
        self.jogo.mostrar_texto('Mika \n“Conselho da Névoa?”')
        self.jogo.after(2000, self.passo7)

    def passo7(self):
        self.jogo.mostrar_texto('Tomel \n“Acho que eu posso te levar até meus superiores, eles vão gostar de conversar com você.”')
        self.jogo.after(2000, self.passo8)

    def passo8(self):
        self.jogo.mostrar_texto('Vocês andam por um tempo, Tomel já sabia todo o caminho de cabeça.')
        self.jogo.mostrar_texto('A cidade era boa, tranquila e com habitantes alegres.')
        self.jogo.after(5000, self.passo9)

    def passo9(self):
        self.jogo.mostrar_texto('Vocês chegam a uma casa, não era muito grande, mas não era pequena.')
        self.jogo.after(2000, self.passo10)

    def passo10(self):
        self.jogo.mostrar_texto('??? \n“Tomel, finalmente! Por que a demora? Nós já estávamos começando e- quem é esse do seu lado?”')
        self.jogo.mostrar_texto('Você percebe um certo tom de desaprovação e desconfiança.')
        self.jogo.after(2000, self.passo11)

    def passo11(self):
        self.jogo.mostrar_texto('Tomel \n“Não se preocupe, Senhor Faenor! Ele se chama Mika e é um viajante, mas não só isso, ele tem ligação com a magia, veja o amuleto dele!”')
        self.jogo.mostrar_texto('Tomel então se mostra um garoto observador e inteligente, por mais que ele pareça jovem e ingênuo.')
        self.jogo.after(2000, self.passo12)

    def passo12(self):
        self.jogo.mostrar_texto('Faenor \n“Bem, que falta de educação a minha, sente-se, Mika, tome seu lugar também, Tomel, acho que precisamos conversar com o Senhor Mika”')
        self.jogo.after(2000, self.passo13)

    def passo13(self):
        self.jogo.mostrar_texto('Você acompanha Tomel até a mesa em que Faenor e os outros membros estavam sentados.')
        self.jogo.after(2000, self.passo14)

    def passo14(self):
        self.jogo.mostrar_texto('Você sente que todos estão te observando, mas prefere não pensar sobre isso.')
        self.jogo.after(2000, self.passo15)

    def passo15(self):
        self.jogo.mostrar_texto('Faenor \n“Me perdoe, Senhor Mika, nós somos o Conselho da Névoa, atualmente estamos investigando a magia e seu possível retorno. Entenda, apenas queremos manter nossa pequena aldeia segura.”')
        self.jogo.after(2000, self.passo16)

    def passo16(self):
        self.jogo.mostrar_texto('Faenor \n“Então me conte, Mika, qual o seu envolvimento nisso? Devemos nos preocupar com sua chegada?”')
        self.jogo.after(2000, self.passo17)

    def passo17(self):
        self.jogo.mostrar_texto('Você sente uma tensão pairando. ')
        self.jogo.after(3000, self.passo18)

    def passo18(self):
        self.jogo.mostrar_texto('Mika \n“Não se preocupem, eu sou só um viajante de passagem, também estou investigando sobre a magia, eu quero ajudar!” ')
        self.jogo.after(2000, self.fim)

    def fim(self):
        self.jogo.mostrar_texto('Fase incompleta...')
        self.jogo.after(2000, self.mudar_fase)



# --- MISSÃO 4 ---
class Missao4(FasesBase):
    def iniciar(self):
        self.jogo.mostrar_texto('Você continua seguindo o brilho do amuleto.')
        self.jogo.after(2000, self.passo2)
    
    def passo2(self):
        self.jogo.mostrar_texto('O caminho vai ficando mais sombrio à medida que você avança. A terra começa a morrer e sussurros começam a correr com o vento.')
        self.jogo.after(2500, self.passo3)
    
    def passo3(self):
        self.jogo.mostrar_texto('Até que você chega na Cidade de Varek. Ou o que restou dela.')
        self.jogo.after(2000, self.passo_escolha_caminho)

    def passo_escolha_caminho(self):
        self.jogo.mostrar_texto('Escolher o caminho:\n[1] SEGUIR PARA ESQUERDA\n[2] SEGUIR EM FRENTE\n[3] SEGUIR PARA DIREITA')

        self.jogo.estado_jogo = self.processar_caminho
        self.jogo.esperar_resposta()

    def processar_caminho(self, decisao):
        if decisao == '1':
            self.jogo.mostrar_texto('Uma biblioteca, uma grande escola e diversas casas destruídas.')
            self.jogo.after(1500, self.passo_lado_esquerdo)

        elif decisao == '2':
            self.jogo.after(1000, self.passo_centro)

        elif decisao == '3':
            self.jogo.mostrar_texto('Um parque, uma padaria e diversas casas destruídas.')
            self.jogo.after(1500, self.passo_lado_direito)

        else:
            self.jogo.after(1000, self.passo_escolha_caminho)

    def passo_lado_esquerdo(self):
        self.jogo.mostrar_texto('Escolher caminho:\n[1] CONTINUAR AQUI\n[2] VOLTAR')

        self.jogo.estado_jogo = self.processar_lado_esquerdo
        self.jogo.esperar_resposta()

    def processar_lado_esquerdo(self, decisao):
        if decisao == '1':
            self.jogo.mostrar_texto('Não há nada para fazer aqui.')
            self.jogo.after(1000, self.passo_lado_esquerdo)

        elif decisao == '2':
            self.jogo.after(1000, self.passo_escolha_caminho)

        else:
            self.jogo.after(1000, self.passo_lado_esquerdo)

    def passo_lado_direito(self):
        self.jogo.mostrar_texto('Escolher caminho:\n[1] CONTINUAR AQUI\n[2] VOLTAR')

        self.jogo.estado_jogo = self.processar_lado_direito
        self.jogo.esperar_resposta()

    def processar_lado_direito(self, decisao):
        if decisao == '1':
            self.jogo.mostrar_texto('Não há mais nada para fazer aqui.')
            self.jogo.after(1000, self.passo_lado_direito)

        elif decisao == '2':
            self.jogo.after(1000, self.passo_escolha_caminho)

        else:
            self.jogo.after(1000, self.passo_lado_direito)

    def passo_centro(self):
        self.jogo.mostrar_texto('Você chega ao centro destruído, há uma estátua no centro.')
        self.jogo.after(2000, self.centro_passo4)
    
    def centro_passo4(self):
        self.jogo.mostrar_texto('???\n“Por favor me ajude...”')
        self.jogo.after(2000, self.centro_passo5)
    
    def centro_passo5(self):
        self.jogo.mostrar_texto('Você se vira, tentando achar quem disse isso, mas não há ninguém, até que mais vozes pedem socorro.')
        self.jogo.after(2000, self.centro_passo6)
    
    def centro_passo6(self):
        self.jogo.mostrar_texto('??? \n“Nos ajude a sair daqui! Estamos presos!”')
        self.jogo.after(2000, self.centro_passo7)
    
    def centro_passo7(self):
        self.jogo.mostrar_texto('??? \n“Me ajude, eu não consigo respirar...”')
        self.jogo.after(2000, self.centro_passo8)
    
    def centro_passo8(self):
        self.jogo.mostrar_texto('??? \n“Eu não consigo ver nada, Ele acabou com tudo...”')
        self.jogo.after(2000, self.centro_passo9)
    
    def centro_passo9(self):
        self.jogo.mostrar_texto('Mais pedidos de socorro, alguns gritam, mas a maioria são sussurros levados pelo ar, até que...')
        self.jogo.after(2000, self.centro_passo10)
    
    def centro_passo10(self):
        self.jogo.mostrar_texto('??? \n“Garotinho! Hey!”')
        self.jogo.after(2000, self.centro_passo11)
    
    def centro_passo11(self):
        self.jogo.mostrar_texto('??? \n“Rutha, eu acho que ele não vai te ouvir...”')
        self.jogo.after(2000, self.centro_passo12)
    
    def centro_passo12(self):
        self.jogo.mostrar_texto('Mika \n“Quem está aí? Eu estou ouvindo! Se precisar de ajuda eu estoua disposição!”')
        self.jogo.after(2000, self.centro_passo13)

    def centro_passo13(self):
        self.jogo.mostrar_texto('Rutha?\n“Aproxime-se! A estátua!”')
        self.jogo.after(2000, self.centro_passo14)
    
    def centro_passo14(self):
        self.jogo.mostrar_texto('Você anda em direção a estátua e, ao chão, restos mortais. Mas logo duas almas se fazem presentes: uma mulher alta e forte e um homem esguio.')
        self.jogo.mostrar_texto('Rutha?\n“Olá, jovem viajante, eu sou a Dame Rutha, a Capitão Dame Rutha!”')
        self.jogo.after(2000, self.centro_passo15)
    
    def centro_passo15(self):
        self.jogo.mostrar_texto('Dame Rutha\n“Estou esperando há tanto tempo por alguém para me ajudar. Eu perdi minha família há muito tempo e queria vê-los novamente. Você precisa trazer seus restos mortais para cá.”')
        self.jogo.after(2000, self.centro_passo16)
    
    def centro_passo16(self):
        self.jogo.mostrar_texto('COMEÇA MISSÃO “JUNTOS NOVAMENTE”\nObjetivo: Encontre os restos mortais dos familiares da Dame Rutha e reúna a família.')
        self.jogo.after(3000, self.passo17)

    def passo17(self):
        self.restos_encontrados = []
        self.jogo.mostrar_texto('Dame Rutha\n“A minha mãe adorava ir à biblioteca, ela ia lá todos os dias e era amiga da bibliotecária. E meu pai era professor na escola, mas sempre que possível ele passeava pelo parque. Eu também tinha uma irmã, ela trabalhava na padaria fazendo doces.”')
        self.jogo.after(2000, self.passo_escolha_locais)

    def passo_escolha_locais(self):
        self.jogo.mostrar_texto('Já sabe em que locais podem estar os restos mortais?\nSelecione as opções separando por vírgual (exemplo: 1, 2, 3):\n[1] BIBLIOTECA\n[2] ESCOLA\n[3] CASAS DESTRUÍDAS (LADO ESQUERDO)\n[4] PARQUE\n[5] PADARIA\n[6] CASAS DESTRUÍDAS (LADO DIREITO)')
        self.jogo.estado_jogo = self.processar_locais
        self.jogo.esperar_resposta()

    def processar_locais(self, resposta):
        # opcoes = set(map(str.strip, resposta.split(',')))
        # corretas = {'1', '2', '4', '5'}
        self.resposta_correta = '1, 2, 4, 5'

        if (resposta == self.resposta_correta):
            self.jogo.mostrar_texto('Correto!')
            self.jogo.after(2000, self.passo18_escolher_local)
        else:
            self.jogo.mostrar_texto('Isso não parece condizer com as informações dadas por Dame Rutha.')
            self.jogo.after(1500, self.passo_escolha_locais)

    def passo18_escolher_local(self):
        self.jogo.mostrar_texto('Para onde você deseja seguir? \n[1] BIBLIOTECA \n[2] ESCOLA \n[3] PARQUE \n[4] PADARIA \n[5] VOLTAR PARA DAME RUTHA')
        self.jogo.estado_jogo = self.passo18_processar_decisao
        self.jogo.esperar_resposta()
    
    def passo18_processar_decisao(self, decisao):
        if (decisao=='1'):
            self.jogo.mostrar_texto('A antiga biblioteca está em ruínas. Estantes tombadas, livros queimados, mas ainda há fragmentos do passado aqui. Você começa a investigar.')
            self.jogo.after(2000, self.decisao1_passo19)
        
        elif (decisao=='2'):
            self.jogo.mostrar_texto('A antiga escola está de pé, mas vazia. Nos corredores silenciosos, os ecos das vozes infantis clamando por ajuda. Cadernos abertos, brinquedos esquecidos, quadros partidos. Aqui, o futuro foi interrompido.')
            self.jogo.after(2000, self.decisao2_passo19)
        
        elif (decisao=='3'):
            self.jogo.mostrar_texto('Antes um lugar de encontros e risos, agora o parque é apenas cinza e poeira. Os bancos quebrados e as árvores queimadas contam a história de um mundo que não volta mais.')
            self.jogo.after(2000, self.decisao3_passo19)
        
        elif (decisao=='4'):
            self.jogo.mostrar_texto('O aroma dos pães e doces há muito foi substituído pelo cheiro de madeira queimada. A segunda casa da irmã da Rutha se encontrava totalmente destruída')
            self.jogo.after(2000, self.decisao4_passo19)
        
        elif (decisao=='5'):
            if (len(self.restos_encontrados)>=3):
                self.jogo.after(2000, self.passo21)
            else:
                self.jogo.mostrar_texto('Parece que ainda falta...')
                self.jogo.after(2000, self.passo18_escolher_local)
        
        else:
            self.jogo.mostrar_texto('Digite uma opção válida.')
            self.jogo.after(2000, self.passo18_escolher_local)


    def decisao1_passo19(self):
        self.jogo.mostrar_texto('Você investiga o local.')
        self.jogo.after(2000, self.decisao1_passo20)
    
    def decisao1_passo20(self):
        self.jogo.mostrar_texto('O crânio da mãe de Rutha está aqui.')
        self.restos_encontrados.append('mãe')
        self.jogo.mostrar_texto('Você ganhou 1 resto mortal.')
        self.jogo.after(2000, self.passo18_escolher_local)
    

    def decisao2_passo19(self):
        self.jogo.mostrar_texto('Você investiga o local.')
        self.jogo.after(2000, self.decisao2_passo20)
    
    def decisao2_passo20(self):
        self.jogo.mostrar_texto('O crânio do pai de Rutha não está aqui.')
        self.jogo.mostrar_texto('Você ganhou 0 resto mortal.')
        self.jogo.after(2000, self.passo18_escolher_local)
    

    def decisao3_passo19(self):
        self.jogo.mostrar_texto('Você investiga o local.')
        self.jogo.after(2000, self.decisao3_passo20)
    
    def decisao3_passo20(self):
        self.jogo.mostrar_texto('O crânio do pai de Rutha está aqui.')
        self.restos_encontrados.append('pai')
        self.jogo.mostrar_texto('Você ganhou 1 resto mortal.')
        self.jogo.after(2000, self.passo18_escolher_local)
    

    def decisao4_passo19(self):
        self.jogo.mostrar_texto('Você investiga o local.')
        self.jogo.after(2000, self.decisao4_passo20)
    
    def decisao4_passo20(self):
        self.jogo.mostrar_texto('O crânio da irmã de Rutha está aqui.')
        self.restos_encontrados.append('irmã')
        self.jogo.mostrar_texto('Você ganhou 1 resto mortal.')
        self.jogo.after(2000, self.passo18_escolher_local)
    

    def passo21(self):
        self.jogo.mostrar_texto('Mika \n“Dame Rutha! Eu os encontrei!”')
        self.jogo.mostrar_texto('Você mostra os quatro crânios e Rutha abre um grande sorriso. Você os coloca ao lado de seus restos mortais.')
        self.jogo.after(2000, self.passo22)
    
    def passo22(self):
        self.jogo.mostrar_texto('Dame Rutha \n“Está vendo, Malvin? Eu disse que o garoto conseguiria, ele é um guerreiro como eu!”')
        self.jogo.after(2000, self.passo23)
    
    def passo23(self):
        self.jogo.mostrar_texto('Malvin\n“Eu não faço a menor ideia de como ele conseguiu reconhecer a cidade, eu morei aqui a minha vida toda e tudo parece tão... diferente.”')
        self.jogo.after(2000, self.passo24)
    
    def passo24(self):
        self.jogo.mostrar_texto('Dame Rutha\n“Não subestime esse garotinho, eu sinto que algo bom o aguarda...”')
        self.jogo.after(2000, self.passo25)
    
    def passo25(self):
        self.jogo.mostrar_texto('Dame Rutha \n“Jovem, eu preciso te agradecer, me diga seu nome.”')
        self.jogo.after(2000, self.passo26)
    
    def passo26(self):
        self.jogo.mostrar_texto('Mika \n“Eu sou o Mika! Mas não se preocupe, era o mínimo que eu podia fazer!”')
        self.jogo.after(2000, self.passo27)
    
    def passo27(self):
        self.jogo.mostrar_texto('Dame Rutha \n“Jovem Guerreiro Mika, não seja tão modesto, hahaha! Muito obrigada, eu finalmente vou poder descansar em paz, minha família está comigo...”')
        self.jogo.after(2000, self.passo28)
    
    def passo28(self):
        self.jogo.mostrar_texto('A alma da Dame Rutha começa a desaparecer, como se estivesse sendo levada pelo vento. Você e Malvin observam a partida dela em silêncio.')
        self.jogo.after(2000, self.passo29)
    
    def passo29(self):
        self.jogo.mostrar_texto('Quando ela vai embora completamente, Malvin começa a falar.')
        self.jogo.mostrar_texto('Malvin \n“Nas vestes da Rutha tem um mapa, acreditam que ele leva para o esconderijo do Arquimago. Também tem uma joia muito interessante, ela surgiu logo após Rutha... bem, morrer. Ela gostaria que ficasse com você”')
        jogador.Mika.add_item('Mapa do Arquimago')
        jogador.Mika.add_item('Antigo Mundo')
        print(jogador.Mika.inventario)
        self.jogo.after(2000, self.passo30)
    
    def passo30(self):
        self.jogo.mostrar_texto('Você ganhou 1 mapa e 1 fragmento sagrado “Antigo Mundo”')

        self.jogo.after(3500, self.mudar_fase)



# --- MISSAO 5 ---
class Missao5(FasesBase):
    def iniciar(self):
        self.jogo.mostrar_texto('Seu amuleto volta a brilhar, indicando mais um caminho a seguir.')
        self.jogo.after(2000, self.passo29_batalha)
    
    def passo2(self):
        self.jogo.mostrar_texto('Por fim você chega a Floresta de Eldariel. A atmosfera ali é diferente, é mais viva e a presença da magia é mais forte.')
        self.jogo.after(2000, self.passo3)
    
    def passo3(self):
        self.jogo.mostrar_texto('Você caminha por um tempo e encontra uma figura envolta por uma luz dourada, como um fragmento do próprio Sol. Ela rapidamente vai até você, você observa que além do brilho, ela possui asas quase transparentes.')
        self.jogo.mostrar_texto('??? \n“Você! Você deve ser Mika! A floresta me falou sobre você, um viajante que chegaria com amuleto encantado. Vamos! Rápido! Nós temos coisas a fazer e-”')
        self.jogo.after(3000, self.passo4)
    
    def passo4(self):
        self.jogo.mostrar_texto('Mika \n“Calma, quem é você? A floresta falou? A magia ainda tá viva nesse lugar?!”')
        self.jogo.after(2000, self.passo5)
    
    def passo5(self):
        self.jogo.mostrar_texto('??? \n“Ah sim, claro! Me desculpa, eu sou Eyla, uma fada da luz, eu sou uma das últimas criaturas mágicas existentes, nós estamos aqui para cumprir com a nossa parte do selamento, mas o selo está se rompendo, alguma coisa aconteceu e agora o coração da floresta agoniza...”')
        self.jogo.after(2000, self.passo6)
    
    def passo6(self):
        self.jogo.mostrar_texto('Eyla \n“Mas a floresta me contou que um viajante chegaria, portador de um amuleto encantado e do destino do mundo. Você pode nos ajudar, Mika!”')
        self.jogo.after(2500, self.passo7)
    
    def passo7(self):
        self.jogo.mostrar_texto('Você pensa um pouco, tentando absorver tudo que foi dito, e logo conta sua missão, pensando que ela pode realmente te ajudar. Ela te escuta com atenção e logo surge uma ideia:')
        self.jogo.after(3000, self.passo8)
    
    def passo8(self):
        self.jogo.mostrar_texto('Eyla \n“Eu sei quem pode ajudar! Koryn guarda os segredos esquecidos do antigo mundo, ele pode nos ajudar a chegar até Yrenn, a Dríade Maior.”')
        self.jogo.after(2000, self.passo9)

    def passo9(self):
        self.jogo.mostrar_texto('Eyla \n“Koryn era o antigo mensageiro, ele levava as ordens de Yrenn para os humanos, pode-se dizer que tinham boa convivência, ele até gostava dos humanos, até aquele dia... um grupo de humanos invadiu a floresta e começou a pegar pequenas criaturas, espalharam fogo e alguns não sobreviveram. Todos ficamos com raiva, mas Koryn ainda guarda mágoas em seu coração. Ele era um bom homem, Mika, antes da invasão.”')
        self.jogo.after(3000, self.passo10)
    
    def passo10(self):
        self.jogo.mostrar_texto('Eyla \n“É melhor irmos logo!”')
        self.jogo.mostrar_texto('Eyla começa a voar rapidamente e você corre atrás dela. Até que chegam a um círculo de pedras antigas. Ali, envolto em musgo e flores flutuantes, está um homem, mas não um homem comum, a parte de cima de seu corpo é de um humano, com exceção dos chifres e orelhas, e a parte de baixo é de bode. Seria esse Koryn?')
        self.jogo.after(2000, self.passo11)
    
    def passo11(self):
        self.jogo.mostrar_texto('Antes que vocês se aproximem, Eyla te puxa para mais perto.')
        self.jogo.mostrar_texto('Eyla \n“Lembre-se, Mika, Koryn não vai confiar em você. Tente vencer o jogo dele... ah sim, ele tem um jeitinho só dele de falar!”')
        self.jogo.after(2000, self.passo12)
    
    def passo12(self):
        self.jogo.mostrar_texto('Eyla \n“Koryn! Veja só o que eu trouxe!”')
        self.jogo.after(2000, self.passo13)
    
    def passo13(self):
        self.jogo.mostrar_texto('Koryn então te olha de forma julgadora, você até tenta conversar com ele, mas ele é mais rápido que você.')
        self.jogo.mostrar_texto('Koryn \n“Você, viajante, está pronto para ser julgado pela floresta?”')
        self.jogo.after(2000, self.passo14)
    
    def passo14(self):
        self.jogo.mostrar_texto('Mika \n“Eu vim para ajudar. Quero restaurar o que foi perdido.”')
        self.jogo.after(2000, self.passo15)

    def passo15(self):
        self.jogo.mostrar_texto('Koryn \n“Palavras são leves como folhas ao vento. Prove com ações. Traga-me as verdades que carrega e as alinhe com os sussurros da floresta.”')
        self.jogo.after(2000, self.passo16_desafio_inicio)
    
    # --- DESAFIO ---
    def passo16_desafio_inicio(self):
        self.jogo.mostrar_texto('COMEÇA O DESAFIO \nObjetivo: montar a sequência correta dos acontecimentos com base no que Eyla te contou.')
        self.jogo.after(2000, self.passo17_desafio_opcoes)
    
    def passo17_desafio_opcoes(self):
        self.jogo.mostrar_texto('Escreva os números corretos e na ordem correta, separados por vírgula e espaço (por exemplo: 5, 2, 6, 1): \n[1] KORYN AINDA ESTÁ COM RAIVA \n[2] KORYN GOSTAVA DOS HUMANOS \n[3] OS HUMANOS SEGUIAM A YRENN \n[4] KORYN ERA MENSAGEIRO \n[5] OS HUMANOS INVADIRAM A FLORESTA \n[6] KORYN LUTOU CONTRA OS HUMANOS \n[7] KORYN ERA UM BOM HOMEM \nDigite aqui: ')
        self.jogo.estado_jogo = self.desafio_processar_decisao
        self.jogo.esperar_resposta()

    def desafio_processar_decisao(self, decisao):
        if (decisao=='4, 2, 7, 5, 1'):
            self.jogo.mostrar_texto('Koryn \n“Vejo clareza no seu espírito. A floresta aceita sua ajuda...”')
            self.jogo.after(2000, self.passo18)
        
        else:
            self.jogo.mostrar_texto('Koryn \n“As raízes se entrelaçam com mentiras, tente novamente...”')
            self.jogo.after(2000, self.passo17_desafio_opcoes)
    
    def passo18(self):
        self.jogo.mostrar_texto('Ele finalmente se levanta e você percebe que ele é mais alto que você, talvez ele tenha 1,70m? Não importa muito, na verdade.')
        self.jogo.mostrar_texto('Koryn \n“Você provou seu valor. Irei te guiar até Yrenn, mas tenha cuidado, nem todos verão com bons olhos a sua chegada.”')
        self.jogo.mostrar_texto('Eyla começa a sorrir, entusiasmada que tudo esteja indo tão bem.')
        self.jogo.after(2000, self.passo19)
    
    def passo19(self):
        self.jogo.mostrar_texto('Vocês então começam a seguir Koryn, se aprofundando na floresta.')
        self.jogo.after(2000, self.passo20)
    
    def passo20(self):
        self.jogo.mostrar_texto('Onde vocês param é um lugar mágico, tanto figurativamente quanto literalmente.')
        self.jogo.after(2000, self.passo21)
    
    def passo21(self):
        self.jogo.mostrar_texto('As árvores parecem que vão até o céu, mas a luz do sol ainda consegue passar por pequenos buracos entre as copas, no centro, há um grande e antiga árvore e, encostada nela, há um ser de beleza divina. Sua pele parecia esculpida na madeira mais fina, seus cabelos eram de folhas volumosas, tão longos que cobriam parte de seu corpo, como uma roupa, e tinha pequenos galhos que pássaros e mariposas se utilizavam para descansar. Então, ao sentir a presença de mais alguém, ela abriu os olhos, eram grandes e tão azuis quanto o céu, transmitiam puridade ao mesmo tempo em que pareciam observar o fundo de sua alma.')
        self.jogo.after(5000, self.passo22)
    
    def passo22(self):
        self.jogo.mostrar_texto('Yrenn \n“Portador do amuleto, o que te traz às minhas terras?”')
        self.jogo.mostrar_texto('A voz que saiu era suave e terna, mas também carregava consigo o tom do julgamento, era intensa.')
        self.jogo.after(2000, self.passo23)
    
    def passo23(self):
        self.jogo.mostrar_texto('Koryn \n“Minha Senhora, eu já conversei com ele, eu acho que-”')
        self.jogo.after(1500, self.passo24)
    
    def passo24(self):
        self.jogo.mostrar_texto('Yrenn \n“Silêncio, Koryn, eu confio em você, mas deixe que ele próprio conte sua história. Posso confiar em você também, Viajante?”')
        self.jogo.after(2000, self.passo25)
    
    def passo25(self):
        self.jogo.mostrar_texto('Tão pronto quanto ela tinha terminado de falar, surge uma voz familiar.')
        self.jogo.mostrar_texto('??? \n“Senhor Mika, quanta gentileza sua nos trazer ao coração da floresta.”')
        self.jogo.after(2000, self.passo26)
    
    def passo26(self):
        self.jogo.mostrar_texto('Mika \n“Faenor?”')
        self.jogo.after(2000, self.passo27)
    
    def passo27(self):
        self.jogo.mostrar_texto('Uma agitação atrás dele começa a se formar, o conselho todo estava lá e não pareciam amigáveis.')
        self.jogo.after(2000, self.passo28)
    
    def passo28(self):
        self.jogo.mostrar_texto('Yrenn, que observava quieta a toda essa situação, decide se levantar. Os animais fogem, a luz do sol não chega mais, o chão treme um pouco e uma parede de folhas e raízes se foram entre Mika e o Conselho da Névoa, era quase uma arena.')
        self.jogo.mostrar_texto('Yrenn \n“Mostre-me, então, sua força.” ')
        self.jogo.after(4000, self.passo29_batalha)
    
    # --- BATALHA ---
    def passo29_batalha(self):
        self.jogo.mostrar_texto('BATALHA MIKA VS. CONSELHO DA NÉVOA ')
        self.vida_mika = jogador.Mika.hp
        self.vida_faenor = 10
        self.jogo.after(2000, self.passo30_batalha)
    
    def passo30_batalha(self):
        self.jogo.mostrar_texto('Faenor \n“Você acha que pode ganhar, Mika? Nós vamos aproveitar todos os benefícios que a magia pode oferecer.”')
        self.jogo.after(2000, self.passo31_batalha_opcoes)
    
    def passo31_batalha_opcoes(self):
        self.jogo.mostrar_texto('Escolha o que fazer: \n[1] ATACAR COM ESPADA \n[2] SE CURAR')
        self.jogo.estado_jogo = self.batalha_processar_decisao
        self.jogo.esperar_resposta()
    
    def batalha_definir_turno(self):
        d_mika = randint(1, 6)
        d_faenor = randint(1, 6)

        if (d_mika > d_faenor):
            self.jogo.mostrar_texto('Você ganhou o turno.')
            pass
            # self.jogo.after(2000, self.passo31_batalha_opcoes)
        
        else:
            self.jogo.mostrar_texto('Você perdeu o turno.')
            self.jogo.after(2000, self.batalha_faenor)
    
    def batalha_mostrar_vida(self):
        self.jogo.mostrar_texto(f'Sua vida: {self.vida_mika}, \nVida de Faenor: {self.vida_faenor}')

    def batalha_processar_decisao(self, decisao):
        dado = randint(1, 6)
        if (decisao=='1'):
            self.jogo.mostrar_texto(f'Você deu um ataque de {dado}')
            self.vida_faenor -= dado
            self.batalha_mostrar_vida()

            if (self.vida_mika > 0):
                self.batalha_vitoria()
                self.jogo.after(2000, self.passo31_batalha_opcoes)
            else:
                self.jogo.after(2000, self.batalha_derrota)
        
        elif (decisao=='2'):
            self.jogo.mostrar_texto(f'Você curou {dado} pontos da sua vida')
            self.vida_mika += dado
            self.batalha_mostrar_vida()

            self.jogo.after(2000, self.passo31_batalha_opcoes)
    
    def batalha_faenor(self):
        dado = randint(1, 6)

        self.jogo.mostrar_texto(f'Faenor te deu um ataque de {dado}')
        self.vida_mika -= dado
        self.batalha_mostrar_vida()

        self.batalha_vitoria()

        if (self.vida_mika > 0):
            self.jogo.after(2000, self.passo31_batalha_opcoes)
        else:
            self.jogo.after(2000, self.batalha_derrota)
    
    def batalha_derrota(self):
        self.jogo.mostrar_texto('FINAL RUIM \nA floresta silencia. O Conselho da Névoa te derrota. A esperança se desfaz como folhas secas ao vento.')
    
    def batalha_vitoria(self):
        if (self.vida_faenor <= 0):
            self.jogo.mostrar_texto('Faenor \n“Mika... você devia entender...” ')
            self.jogo.after(2000, self.passo32)
        else:
            pass


    def passo32(self):
        self.jogo.mostrar_texto('Yrenn levanta sua mão e raízes começam a crescer do chão antes que os outros membros do conselho possam te atacar. As raízes os envolvem e começam a ser absorvidos para o chão, gritos desesperados se tornam presentes e, de um segundo a outro, silêncio.')
        self.jogo.after(4000, self.passo33)
    
    def passo33(self):
        self.jogo.mostrar_texto('Yrenn \n“Você lutou com honra em prol de nossa floresta, Mika, neto da Última Guardiã, o nosso destino repousa em suas mãos.”')
        self.jogo.after(3000, self.passo34)
    
    def passo34(self):
        self.jogo.mostrar_texto('Você ganhou 1 fragmento sagrado “Coração do Mundo Verde”. ')
        jogador.Mika.add_item('Coração do Mundo Verde')
        self.jogo.after(3000, self.passo35)

    def passo35(self):
        self.jogo.mostrar_texto('Yrenn \n“Lamento que ele esteja envelhecido, os anos não foram gentis com nossa floresta...” ')
        self.jogo.after(3000, self.passo36)
    
    def passo36(self):
        self.jogo.mostrar_texto('Eyla \n“Não se preocupe, Mika, ele pode não ter a mesma força que antes... mas ainda pode ser restaurado.” ')
        self.jogo.after(3000, self.passo37)
    
    def passo37(self):
        self.jogo.mostrar_texto('Koryn  “Eyla, o que você está fazendo?!!!” ')
        self.jogo.after(1500, self.passo38)
    
    def passo38(self):
        self.jogo.mostrar_texto('A fada se aproxima do fragmento, uma pequena semente cristalina, e concentra toda sua luz nele. Sua essência e força vital é absorvida, no fim, ela se desfaz como pequenas partículas brilhantes. ')
        self.jogo.after(4000,self.passo39)
    
    def passo39(self):
        self.jogo.mostrar_texto('Koryn \n“Ela... se foi...” ')
        self.jogo.after(2000, self.passo40)
    
    def passo40(self):
        self.jogo.mostrar_texto('Yrenn \n“Seu sacrifício não será em vão. A missão está concluída. Vá, Mika. O mundo ainda precisa de você.” ')
        self.jogo.after(2000, self.fim)
    
    def fim(self):
        self.jogo.mostrar_texto('Você agora carrega consigo uma amiga e uma chave para salvar o mundo.')
        self.jogo.mostrar_texto('É hora de partir.')

        self.jogo.after(3500, self.mudar_fase)



# --- MISSAO 6 ---
class Missao6(FasesBase):
    def iniciar(self):
        self.jogo.mostrar_texto('O amuleto brilha novamente, em sintonia com o vento. Sua jornada agora te conduz a apenas um lugar: o covil do Arquimago. A Torre de Selenar, uma construção esquecida pelo tempo e oculta entre véus de névoa.')
        self.jogo.after(2000, self.passo2)
    
    def passo2(self):
        self.jogo.mostrar_texto('A cada passo em direção à torre, o ar se torna mais denso, como se os ecos do passado ali se acumulassem, aguardando por alguém que ousasse ouvir.')
        self.jogo.after(2000, self.passo3)
    
    def passo3(self):
        self.jogo.mostrar_texto('Ao entrar, o interior da torre revela um labirinto de escadas, portas e corredores. No chão, inscrições enigmáticas, e nas paredes, murmúrios que dançam entre o tempo.')
        self.jogo.after(2000, self.passo4)
    
    def passo4(self):
        self.jogo.mostrar_texto('Da mochila, você pega o mapa obtido com Dame Rutha. Nele, há anotações marcadas com urgência: \n"Se guiar pelo Norte e pelo Sul, seguir pelo passado, presente e futuro."')
        self.jogo.mostrar_texto('Logo adiante, uma escritura no chão começa a brilhar e revela uma nova pista: \n"Norte, presente, norte, futuro, norte, futuro, onde a morte chegou."')
        self.jogo.after(2000, self.passo5)
    
    def passo5(self):
        self.jogo.mostrar_texto('Mika: \n“Entendi... preciso escolher os caminhos corretos em cada andar. Cada direção tem um significado e o tempo e o espaço são uma chave.”')
        self.jogo.after(2000, self.passo6_escolher_caminho)
    
    def passo6_escolher_caminho(self):
        self.jogo.mostrar_texto('Escolher caminho: \n[1] VOLTAR \n[2] SEGUIR PELO MEIO ')

        self.jogo.estado_jogo = self.passo6_processar_decisao
        self.jogo.esperar_resposta()

    def passo6_processar_decisao(self, decisao):
        if (decisao=='1'):
            self.jogo.after(2000, self.passo5)
        
        elif (decisao=='2'):
            self.jogo.mostrar_texto('Há uma escada. Você sobe a escada.')
            self.jogo.after(2000, self.passo7_escolher_caminho)
        
        else:
            self.jogo.mostrar_texto('Digite uma opção válida.')
            self.jogo.after(1000, self.passo6_escolher_caminho)
    
    def passo7_escolher_caminho(self):
        self.jogo.mostrar_texto('Escolher caminho: \n[1] SEGUIR PELA DIREITA \n[2] SEGUIR PELO MEIO \n[3] SEGUIR PELA ESQUERDA')

        self.jogo.estado_jogo = self.passo7_processar_decisao
        self.jogo.esperar_resposta()

    def passo7_processar_decisao(self, decisao):
        if (decisao=='1') or (decisao=='3'):
            self.jogo.mostrar_texto('Uma sala velha. Nada muito importante.')
            self.jogo.mostrar_texto('Você decide voltar.')
            self.jogo.after(1000, self.passo7_escolher_caminho)
        
        elif (decisao=='2'):
            print('ixi')
            self.jogo.mostrar_texto('Há uma outra escada.')
            self.jogo.after(1000, self.passo8_escolher_caminho)

    def passo8_escolher_caminho(self):
        self.jogo.mostrar_texto('Escolher caminho: \n[1] SUBIR \n[2] VOLTAR')
        self.jogo.estado_jogo = self.passo8_processar_decisao
        self.jogo.esperar_resposta()
    
    def passo8_processar_decisao(self, decisao):
        if (decisao=='1'):
            self.jogo.mostrar_texto('Ao subir a escada, você chega a um novo andar.')
            self.jogo.after(2000, self.passo9_escolher_caminho)

        elif (decisao=='2'):
            self.jogo.after(2000, self.passo7_escolher_caminho)
        
        else:
            self.jogo.mostrar_texto('Digite uma opção válida.')
            self.jogo.after(2000, self.passo7_escolher_caminho)
        
    def passo9_escolher_caminho(self):
        self.jogo.mostrar_texto('Escolher caminho: \n[1] SEGUIR PELA DIREITA \n[2] SEGUIR PELO MEIO \n[3] SEGUIR PELA ESQUERDA')

        self.jogo.estado_jogo = self.passo9_processar_decisao
        self.jogo.esperar_resposta()

    def passo9_processar_decisao(self, decisao):
        if (decisao=='3') or (decisao=='2'):
            self.jogo.mostrar_texto('Uma sala velha. Nada muito importante.')
            self.jogo.mostrar_texto('Você decide voltar.')
            self.jogo.after(2000, self.passo9_escolher_caminho)
        
        elif (decisao=='1'):
            self.jogo.mostrar_texto('Há uma outra escada.')
            self.jogo.after(2000, self.passo10_escolher_caminho)

        else:
            self.jogo.mostrar_texto('Digite uma opção válida.')
            self.jogo.after(2000, self.passo9_escolher_caminho)
    
    def passo10_escolher_caminho(self):
        self.jogo.mostrar_texto('Escolher caminho: \n[1] SUBIR')
        self.jogo.estado_jogo = self.passo10_processar_decisao
        self.jogo.esperar_resposta()
    
    def passo10_processar_decisao(self, decisao):
        if (decisao=='1'):
            self.jogo.mostrar_texto('Novos caminhos se formam a sua frente.')
            self.jogo.after(2000, self.passo11_escolher_caminho)
        
        else:
            self.jogo.mostrar_texto('Digite uma opção válida.')
            self.jogo.after(2000, self.passo10_escolher_caminho)
    
    def passo11_escolher_caminho(self):
        self.jogo.mostrar_texto('Escolher caminho: \n[1] SEGUIR PELA DIREITA \n[2] SEGUIR PELO MEIO \n[3] SEGUIR PELA ESQUERDA')
        self.jogo.estado_jogo = self.passo11_processar_decisao
        self.jogo.esperar_resposta()


    def passo11_processar_decisao(self, decisao):
        if (decisao=='1'):
            self.jogo.mostrar_texto('Você anda um pouco e por fim chega em uma sala de pergaminhos. Ao entrar, o ambiente muda. É como se os sussurros cessassem por um momento.')
            self.jogo.after(2000, self.passo12_escolher_caminho)

        elif (decisao=='2'):
            self.jogo.mostrar_texto('Uma escada.')
            self.jogo.mostrar_texto('Escolher caminho: \n[1] SUBIR \n[2] VOLTAR')

        elif (decisao=='3'):
            self.jogo.mostrar_texto('Uma sala velha. Nada muito importante.')
            self.jogo.mostrar_texto('Escolher caminho: \n[1] VOLTAR')
    
    def passo12_escolher_caminho(self):
        self.jogo.mostrar_texto('Onde procurar? \n[1] ESTANTE \n[2] PILHA DE PERGAMINHOS \n[3] MESA CENTRAL \n[4] GRANDE RELÓGIO')
        self.jogo.estado_jogo = self.passo12_processar_decisao
        self.jogo.esperar_resposta()
    
    def passo12_processar_decisao(self, decisao):
        if (decisao=='1'):
            self.jogo.after(2000, self.passo12_escolher_caminho)
        elif (decisao=='2'):
            self.jogo.after(2000, self.passo12_escolher_caminho)
        elif (decisao=='3'):
            self.jogo.mostrar_texto('Você se aproxima da mesa e começa a procurar.')
            self.jogo.after(2000, self.passo13)
        elif (decisao=='4'):
            self.jogo.after(2000, self.passo12_escolher_caminho)
        else:
            self.jogo.mostrar_texto('Digite uma opção válida!')
            self.jogo.after(2000, self.passo12_escolher_caminho)
    
    def passo13(self):
        self.jogo.mostrar_texto('Entre anotações e livros, está um crânio. Logo vem a sua mente: “onde a morte chegou”.')
        self.jogo.after(3000, self.passo14)
    
    def passo14(self):
        self.jogo.mostrar_texto('Você pega aquele crânio e lá está um pequeno cristal que começa a brilhar com uma aura púrpura e pulsante.')
        self.jogo.after(3500, self.passo15)
    
    def passo15(self):
        self.jogo.mostrar_texto('Mika: \n“Esse fragmento... parece diferente. Como se guardasse dor... e raiva.”')
        self.jogo.after(2000, self.passo16)
    
    def passo16(self):
        self.jogo.mostrar_texto('Você ganhou 1 fragmento sagrado “Corrupção”.')
        self.jogo.after(4000, self.fim)
    
    def fim(self):
        self.jogo.mostrar_texto('??? \n“Você veio por respostas, mas está pronto para a verdade?” ')
        self.jogo.after(2000, self.mudar_fase)



# --- MISSÃO 7 ---
class Missao7(FasesBase):
    def iniciar(self):
        self.jogo.mostrar_texto('Missão 7 - O Último Julgamento')
        self.jogo.mostrar_texto('Fase incompleta...')
        self.jogo.after(2000, self.mudar_fase)





# --- MISSÕES SECUNDÁRIAS ---

# --- SECUNDÁRIA 1 ---
class Secundaria1(FasesBase):
    def iniciar(self):
        self.jogo.mostrar_texto('Malvin \n"Tudo isso deve ser uma loucura para você, não é?"')
        self.jogo.after(2000, self.passo2)
    
    def passo2(self):
        self.jogo.mostrar_texto('Malvin \n"A nossa cidade... ela nem sempre foi assim. Antigamente, éramos um centro de saber, tecnologia e magia. a magia florescia em cada flor e em cada humano, em cada sonho. Mas talvez... talvez nunca estivéssemos prontos para o que ela exigia de nós."')
        self.jogo.after(3000, self.passo3)
    
    def passo3(self):
        self.jogo.mostrar_texto('Pela primeira vez, Malvin se dirige diretamente a você, com o olhar distante.')
        self.jogo.after(2500, self.passo4)
    
    def passo4(self):
        self.jogo.mostrar_texto('Malvin \n"Então ele apareceu. Ninguém sabe de onde veio, nem por quê. Só que chegou trazendo destruição, em nome de uma paz que só ele acreditava existir. Nós resistimos, mas perdemos. Perdemos tudo. A cidade... foi consumida por ele. O Arquimago."')
        self.jogo.after(3000, self.passo5)
    
    def passo5(self):
        self.jogo.mostrar_texto('Avançar em missão secundária?\n[1] SEGUIR EM MISSÃO PRINCIPAL\n[2] AVANÇAR EM MISSÃO SECUNDÁRIA')
        self.jogo.estado_jogo = self.passo6_processar_inicio
        self.jogo.esperar_resposta()

    def passo6_processar_inicio(self, decisao):
        if decisao == '1':
            self.jogo.mostrar_texto('As ruínas sussurram memórias que você não pode carregar.')
            self.jogo.after(3000, self.decisao1_passo7)
            
        elif decisao == '2':
            self.jogo.mostrar_texto('Malvin entrega a você um velho caderno, coberto por fuligem e tempo.')
            self.jogo.after(2000, self.decisao2_passo7)

        else:
            self.jogo.after(1000, self.passo5)
    
    def decisao1_passo7(self):
        self.jogo.mostrar_texto('Não há mais o que fazer aqui.')
        self.jogo.mostrar_texto('O mundo lá fora aguarda sua decisão. Você parte da cidade, com passos guiados pelo desconhecido.')
        
        self.missao5 = Missao5(self.jogo)
        self.jogo.after(2000, self.missao5.iniciar())
    

    def decisao2_passo7(self):
        self.jogo.mostrar_texto('Malvin\n“Este é o meu diário, contém os registros dos meus últimos dias de vida, antes da cidade ser destruída. Mas algumas páginas se perderam nos escombros. Se você as encontrar... talvez entenda”')
        self.jogo.after(1000, self.passo8)
        
    
    def passo8(self):
        self.jogo.mostrar_texto('COMEÇA MISSÃO “FRAGMENTOS DE MALVIN”\nObjetivo: Recupere as páginas perdidas do Diário de Malvin espalhadas pela cidade destruída.')
        self.folhas = 0
        self.jogo.after(1000, self.passo9_escolha_caminho)

    def passo9_escolha_caminho(self):
        self.jogo.mostrar_texto('Escolher o caminho: \n[1] SEGUIR PARA ESQUERDA \n[2] SEGUIR PARA DIREITA')
        self.jogo.estado_jogo = self.passo9_processar_caminho
        self.jogo.esperar_resposta()

    def passo9_processar_caminho(self, decisao):
        if decisao == '1':
            self.jogo.mostrar_texto('Você vê uma biblioteca, uma grande escola e diversas casas destruídas.')
            self.jogo.mostrar_texto('Seguir para: \n[1] BIBLIOTECA \n[2] ESCOLA \n[3] CASAS DESTRUÍDAS')
            self.jogo.estado_jogo = self.decisao1_lado_esquerdo
            self.jogo.esperar_resposta()

        elif decisao == '2':
            self.jogo.mostrar_texto('Seguir para: \n[1] PARQUE \n[2] PADARIA \n[3] CASAS DESTRUÍDAS')
            self.jogo.estado_jogo = self.decisao2_lado_direito
            self.jogo.esperar_resposta()
            
        else:
            self.jogo.after(1000, self.passo9_escolha_caminho)
    
    def passo10_escolher_caminho(self):
        self.jogo.mostrar_texto('Escolher o caminho: \n[1] CONTINUAR AQUI \n[2] VOLTAR')
        self.jogo.estado_jogo = self.passo10_processar_caminho
        self.jogo.esperar_resposta()
    
    def passo10_processar_caminho(self, decisao):
        if (decisao=='1'):
            self.jogo.mostrar_texto('Não há mais nada para fazer aqui...')
            self.jogo.after(1000, self.passo10_escolher_caminho)

        elif (decisao == '2'):
            self.jogo.after(1000, self.passo9_escolha_caminho)


    def decisao1_lado_esquerdo(self, decisao):
        if decisao == '1':
            self.jogo.mostrar_texto('A antiga biblioteca está em ruínas. Estantes tombadas, livros queimados, mas ainda há fragmentos do passado aqui. Você começa a investigar.')
            self.jogo.mostrar_texto('Você encontrou alguns papéis.')
            self.folhas += 1
            self.jogo.mostrar_texto('Você ganhou 1 folha(s) do diário.')
            self.jogo.after(1000, self.passo10_escolher_caminho)

        elif decisao == '2':
            self.jogo.mostrar_texto('A antiga escola está de pé, mas vazia. Nos corredores silenciosos, os ecos das vozes infantis clamando por ajuda. Cadernos abertos, brinquedos esquecidos, quadros partidos. Aqui, o futuro foi interrompido.')
            self.jogo.mostrar_texto('Você não encontrou nenhum papel.')
            self.jogo.mostrar_texto('Você ganhou 0 folha(s) do diário.')
            self.jogo.after(1000, self.passo10_escolher_caminho)

        elif decisao == '3':
            self.jogo.mostrar_texto('Casas colapsadas e restos calcinados de vidas comuns. Mesas postas que nunca foram usadas, roupas penduradas que nunca foram vestidas. O silêncio é opressor. Você investiga o local.')
            self.jogo.mostrar_texto('Você não encontrou nenhum papel.')
            self.jogo.mostrar_texto('Você ganhou 0 folha(s) do diário.')
            self.jogo.after(1000, self.passo10_escolher_caminho)

        else:
            self.jogo.after(1000, self.passo10_escolher_caminho)

        self.verifica_folhas()

    def decisao2_lado_direito(self, decisao):
        if decisao == '1':
            self.jogo.mostrar_texto('Antes um lugar de encontros e risos, agora o parque é apenas cinza e poeira. Os bancos quebrados e as árvores queimadas contam a história de um mundo que não volta mais. Malvin costumava caminhar por aqui ao entardecer. Você investiga o local.')
            self.jogo.mostrar_texto('Você encontrou alguns papéis.')
            self.folhas += 1
            self.jogo.mostrar_texto('Você ganhou 1 folha(s) do diário.')
            self.jogo.after(1000, self.passo10_escolher_caminho)

        elif decisao == '2':
            self.jogo.mostrar_texto('O aroma dos pães doces há muito foi substituído pelo cheiro de madeira queimada. A padaria favorita de Malvin ainda guarda suas marcas: uma mesa isolada, anotações grudadas na parede. Ali, ele escrevia seus pensamentos enquanto observava a cidade respirar. Você investiga o local.')
            self.jogo.mostrar_texto('Você encontrou alguns papéis.')
            self.folhas += 2
            self.jogo.mostrar_texto('Você ganhou 2 folha(s) do diário.')
            self.jogo.after(1000, self.passo10_escolher_caminho)

        elif decisao == '3':
            self.jogo.mostrar_texto('Estas casas parecem ter sido as últimas a cair. Entre os destroços, uma escrivaninha destruída ainda carrega a lembrança de alguém que tentou escrever até o fim. Você investiga o local.')
            self.jogo.mostrar_texto('Você encontrou alguns papéis.')
            self.folhas += 1
            self.jogo.mostrar_texto('Você ganhou 1 folha(s) do diário.')
            self.jogo.after(1000, self.passo10_escolher_caminho)

        else:
            self.jogo.after(1000, self.passo_escolha_caminho)

        self.verifica_folhas()

    def verifica_folhas(self):
        if self.folhas >= 5:
            self.jogo.mostrar_texto('MISSÃO CONCLUÍDA')
            self.jogo.mostrar_texto('Você ganhou 1 fragmento sagrado “Verdade Humana”')

            jogador.Mika.add_item('Verdade Humana')
            self.jogo.after(2000, self.passo11)
    
    def passo11(self):
        self.jogo.mostrar_texto('Diário de Malvin')
        self.jogo.mostrar_texto('“DIA 1: \nUm homem estranho chegou, começou a gritar no meio da praça central, ele falou algumas coisas sobre paz e uso da magia. Não me importo muito, nossa província é próspera.')
        self.jogo.after(3000, self.passo12)
    
    def passo12(self):
        self.jogo.mostrar_texto('...')
        self.jogo.mostrar_texto('DIA 5: \nO homem ainda não partiu, sempre vejo ele na praça, mas parece que nossos líderes estão se irritando com ele.')
        self.jogo.after(3000, self.passo13)
    
    def passo13(self):
        self.jogo.mostrar_texto('DIA 7: \nO homem foi forçado a sair, acho que finalmente teremos um pouco de paz.')
        self.jogo.after(3000, self.passo14)
    
    def passo14(self):
        self.jogo.mostrar_texto('DIA 10: \nHoje o dia estava correndo normalmente, aproveitei e vim na padaria e peguei meu pão doce favorito, mas uma movimentação estranha começou a vir do interior. Algumas pessoas chegaram agitadas, crianças chorando e rostos assustados, eles falavam sobre um homem estranho que conjurava feitiços estranho. “Arquimago! Arquimago! Não o enfrente!” alguns gritavam.')
        self.jogo.after(4000, self.passo15)
    
    def passo15(self):
        self.jogo.mostrar_texto('DIA 13: \nEu vi o rosto dele, do Arquimago, era ele, o homem estranho da praça.')
        self.jogo.after(3000, self.passo16)
    
    def passo16(self):
        self.jogo.mostrar_texto('DIA 13: \nEu vi o rosto dele, do Arquimago, era ele, o homem estranho da praça.')
        self.jogo.after(3000, self.passo17)
    
    def passo17(self):
        self.jogo.mostrar_texto('DIA 18: \nO Arquimago está tentando tomar nossa cidade, nossos líderes estão tentando reverter a situação, me chamaram para escrever relatórios. Eu conheci Dame Rutha, a capitã, ela teve que deixar sua família para se dedicar totalmente ao nosso governo. Eu gostaria de saber mais sobre ela, aparentemente vamos passar muito tempo juntos, ela é forte, dedicada, incrível.')
        self.jogo.after(4000, self.passo18)
    
    def passo18(self):
        self.jogo.mostrar_texto('DIA 19: \nAcho que estamos conseguindo vencê-lo!')
        self.jogo.after(4000, self.passo19)
    
    def passo19(self):
        self.jogo.mostrar_texto('DIA 26: \nDestruído.')
        self.jogo.after(5000, self.passo20)
    
    def passo20(self):
        self.jogo.mostrar_texto('DIA 27: \nNão estou com tempo para escrever, nem sei se consigo, Ele destrói tudo que toca, ninguém consegue pará-lo, Ele é como uma sombra, sua espada divide florestas e cortas rios, você pode tentar fugir e ele vai te encontrar. \nRutha está péssima, talvez ela tenha perdido algum familiar, ela não conversa com ninguém. \nEle chegou na capital, diversas casas destruídas, Ele atacou a escola e a biblioteca. Não posso mais pegar meu pão doce favorito.')
        self.jogo.after(4000, self.passo21)
    
    def passo21(self):
        self.jogo.mostrar_texto('DIA 29: \nRutha voltou a falar comigo, estamos tentando ser fortes, fizemos um pequeno picnic hoje com a comida do exército, ela e nossos superiores estão fazendo um plano para reverter de vez a situação, dizem que há esperança. Rutha sorriu pela primeira vez em um muito tempo, estou feliz!')
        self.jogo.after(5000, self.passo22)
    
    def passo22(self):
        self.jogo.mostrar_texto('DIA 37: \nDame Rutha está morta. O cadáver dela está na minha frente. Preciso dizer que o plano falhou? \nEu não consigo encontrar ninguém, está tudo deserto. \nNão quero sair daqui, há corpos por todos os lugares. \nRutha saberia o que fazer. \nNão consigo parar de chorar.')
        self.jogo.after(4000, self.passo23)
    
    def passo23(self):
        self.jogo.mostrar_texto('DIA 38: \nHoje eu trouxe o corpo da Rutha para o centro da praça, na estátua favorita dela, eu espero que ela esteja descansando. \nEu vou ficar aqui por enquanto, tenho esperanças que alguém possa vir.')
        self.jogo.after(3000, self.passo24)
    
    def passo24(self):
        self.jogo.mostrar_texto('DIA 41: \nMe sinto cada vez mais fraco.”')
        self.jogo.after(4000, self.passo25)
    
    def passo25(self):
        self.jogo.mostrar_texto('Os registros acabaram.')
        self.jogo.after(3000, self.passo26)
    
    def passo26(self):
        self.jogo.mostrar_texto('Um silêncio incomum se instaura no local, não há nenhum lamento ou gritos por ajuda.')
        self.jogo.mostrar_texto('Nada. Apenas o peso da memória.')
        self.jogo.after(4000, self.passo27)
    
    def passo27(self):
        self.jogo.mostrar_texto('Você ganhou 1 fragmento sagrado “Verdade Humana”')
        self.jogo.after(3000, self.fim)

    def fim(self):
        self.jogo.mostrar_texto('É hora de seguir sua jornada.')

        self.jogo.after(3500, self.mudar_fase)



# --- SECUNDÁRIA 2 ---
class Secundaria2(FasesBase):
    def iniciar(self):
        self.jogo.mostrar_texto('Uma figura surge diante de você. Um jovem de expressão rígida e olhar determinado.')
        self.jogo.mostrar_texto('Sem dizer uma palavra, ele saca a espada...')
        self.jogo.after(2000, self.passo2)
    
    def passo2(self):
        self.jogo.mostrar_texto('Mas não avança.')
        self.jogo.after(2000, self.passo3)
    
    def passo3(self):
        self.jogo.mostrar_texto('Ele desfere um golpe no ar e uma sombra se projeta, indo em sua direção.')
        self.jogo.after(2000, self.passo4)
    
    def passo4(self):
        self.jogo.mostrar_texto('Você consegue desviar.')
        self.jogo.mostrar_texto('Mika (pensando) \n(Esse deve ser o Arquimago...)')
        self.jogo.mostrar_texto('O que fazer agora? \n[1] ATACAR \n[2] CONVERSAR')
        
        self.jogo.estado_jogo = self.processar_decisao
        self.jogo.esperar_resposta()

    def processar_decisao(self, decisao):
        if (decisao=='1'):
            self.jogo.mostrar_texto('Você avança para revidar.')
            self.jogo.mostrar_texto('Mas, antes que sua lâmina toque o ar, o jovem se desfaz como névoa soprada pelo vento.')
            self.jogo.after(3000, self.decisao1_passo5)

        elif (decisao=='2'):
            self.jogo.mostrar_texto('Você dá um passo à frente, sem intenções de atacar. Ao fazer isso, o fragmento "Corrupção" começa a brilhar em sua mão.')
            self.jogo.mostrar_texto('A luz o envolve e você é sugado para dentro dela.')
            self.jogo.after(3000, self.decisao2_passo5)
        
        else:
            self.jogo.after(1500, self.passo4)

    def decisao1_passo5(self):
        self.jogo.mostrar_texto('Silêncio.')
        self.jogo.after(3000, self.decisao1_passo6)
            
    def decisao1_passo6(self):
        self.jogo.mostrar_texto('Você sente que perdeu algo, mas também que talvez não estivesse pronto para ouvir.')
        self.jogo.after(3000, lambda: self.jogo.iniciar_fase(10))
    

    def decisao2_passo5(self):
        self.jogo.mostrar_texto('É uma dimensão incomum, suspensa no vazio, a sensação era como estar no espaço, um breu intenso, você não consegue ver nada.')
        self.jogo.after(2500, self.decisao2_passo6)
    
    def decisao2_passo6(self):
        self.jogo.mostrar_texto('Até que: uma luz!')
        self.jogo.mostrar_texto('Ela flutua até você. Ou talvez você flutue até ela.')
        self.jogo.after(2000, self.decisao2_passo7)
    
    def decisao2_passo7(self):
        self.jogo.mostrar_texto('Mika\n"Um espelho?!"')
        self.jogo.after(3000, self.decisao2_passo8)
    
    def decisao2_passo8(self):
        self.jogo.mostrar_texto('Mas agora não é só um, são dois... três... variós! Talvez resquícios de outro universo? Não...')
        self.jogo.after(2500, self.decisao2_passo9)
    
    def decisao2_passo9(self):
        self.jogo.mostrar_texto('Reflexos de um tempo esquecido...')
        self.jogo.after(3000, self.decisao2_passo10)
    
    def decisao2_passo10(self):
        self.jogo.mostrar_texto('Vendo através de um dos espelhos, o jovem está ali novamente, o mesmo que te atacou, mas agora ele parecia mais esperançoso e sonhador.')
        self.jogo.mostrar_texto('"Se eu entender a origem da magia, poderei proteger todos de sua destruição."')
        self.jogo.after(3000, self.decisao2_passo11)

    def decisao2_passo11(self):
        self.jogo.mostrar_texto('Você flutua até outro espelho, era como se aquela dimensão quisesse te mostrar alguma coisa. Nesse novo espelho, o jovem parecia um pouco mais velho e mais... sombrio?')
        self.jogo.mostrar_texto('“Vocês queimaram florestas por poder. Escravizaram espíritos por luz. E agora me chamam de monstro por querer proteger o que restou?”')
        self.jogo.after(4000, self.decisao2_passo12)

    def decisao2_passo12(self):
        self.jogo.mostrar_texto('Novamente outro espelho, mas nesse havia duas pessoas, uma garota tentando alcançá-lo.')
        self.jogo.mostrar_texto('"Hekan, por favor-"')
        self.jogo.mostrar_texto('"Eles não me ouviram. Então eu falei com o mundo por meio do poder."')
        self.jogo.after(4000, self.decisao2_passo13)

    def decisao2_passo13(self):
        self.jogo.mostrar_texto('"Hekan?" Esse nome fica na sua mente, você entende que aquela dimensão, ou melhor, o fragmento, está tentando te mostrar a história de seu dono: o Arquimago.')
        self.jogo.after(4000, self.decisao2_passo14)

    def decisao2_passo14(self):
        self.jogo.mostrar_texto('Mais espelhos. Mais ecos de um passado em ruínas.')
        self.jogo.mostrar_texto('"Eu jurei nunca usar magia para dominar. Mas juras feitas sob luz morrem nas sombras."')
        self.jogo.after(4000, self.decisao2_passo15)
    
    def decisao2_passo15(self):
        self.jogo.mostrar_texto('A cada espelho, a dimensão treme. Tudo distorce ao seu redor, como se a própria lembrança estivesse se fragmentando. Você não sabe mais de onde veio ou onde está. A voz dele ressoa cada vez mais alto, quase um lamento:')
        self.jogo.mostrar_texto('"Cada silêncio me gritava. Cada sombra me sussurrava: continue."')
        self.jogo.after(4000, self.decisao2_passo16)
    
    def decisao2_passo16(self):
        self.jogo.mostrar_texto('Fica claro que aquele homem não era mais Hekan, não era mais aquele sonhador, foi assim que ele virou o tão conhecido Arquimago.')
        self.jogo.mostrar_texto('"Tornei-me o fardo que tentei destruir."')
        self.jogo.after(4000, self.decisao2_passo17)

    def decisao2_passo17(self):
        self.jogo.mostrar_texto('Então, finalmente, um pouco de lucidez, aquela dimensão se acalma e, consequentemente, sua mente também.')
        self.jogo.after(1000, self.decisao2_passo18)

    def decisao2_passo18(self):
        self.jogo.mostrar_texto('Você fica flutuando sem rumo por um tempo, sem ver ou ouvir nada, aquele breu do início se instala novamente. Até que você escuta Hekan dizendo (e você sabe que é Hekan e não o Arquimago):')
        self.jogo.mostrar_texto('"Se alguém ouvir este eco, que veja: não busque controle. Busque equilíbrio."')
        self.jogo.after(4000, self.decisao2_passo19)
    
    def decisao2_passo19(self):
        self.jogo.mostrar_texto('Subitamente, você volta a sua dimensão, era como acordar de um sonho, mas você sabe que era tudo real porque agora tem dois cristais na sua mão. Um deles brilha com uma luz antiga e profunda.')
        self.jogo.after(3000, self.decisao2_passo20)
    
    def decisao2_passo20(self):
        jogador.Mika.add_item('Memória do Arquimago')
        self.jogo.mostrar_texto('Você ganhou o fragmento sagrado "Memória do Arquimago".')

        self.jogo.after(3500, self.fim)

    def fim(self):
        if ('Verdade Humana' in jogador.Mika.inventario) and ('Coração do Mundo Verde' in jogador.Mika.inventario) and ('Memória do Arquimago' in jogador.Mika.inventario):
            self.jogo.mostrar_texto('Há uma missão secundária disponível. \n[1] SEGUIR EM MISSÃO PRINCIPAL \n[2] AVANÇAR EM MISSÃO SECUNDÁRIA')

            self.jogo.estado_jogo = self.fim_processar_decisao
            self.jogo.esperar_resposta()

    def fim_processar_decisao(self, decisao):
        if (decisao=='1'):
            self.jogo.mostrar_texto('Iniciando Missão 7 - Final')
            self.jogo.after(3500, lambda: self.jogo.iniciar_fase(10))

        elif (decisao=='2'):
            self.jogo.mostrar_texto('Iniciando Missão Secundária 3...')
            self.jogo.after(3500, self.mudar_fase)



# --- SECUNDÁRIA 3 ---
class Secundaria3(FasesBase):
    def iniciar(self):
        self.jogo.mostrar_texto('O amuleto começa a brilhar como nunca.')
        self.jogo.mostrar_texto('Era como se uma porta estivesse sendo aberta. Você corria no meio da floresta, entre os mistérios que este mundo guardava, a adrenalina correndo por seu corpo.')
        self.jogo.after(3000, self.passo2)
    
    def passo2(self):
        self.jogo.mostrar_texto('Você então chega ao meio da floresta. Há raízes como na Vila da Neblina, era outra fenda?!')
        self.jogo.after(2000, self.passo3)

    def passo3(self):
        self.jogo.mostrar_texto('Mika \n(O amuleto queria alertar isso?! É melhor eu resolver antes que se espalhe pela floresta!)')
        self.jogo.after(2000, self.passo4)

    def passo4(self):
        self.jogo.mostrar_texto('Você corta as raízes com sua espada e adentra o local, esperando ver monstros ou espíritos, mas muito pelo contrário: é um imenso corredor, diversas salas e você consegue ver estátuas de magos.')
        self.jogo.mostrar_texto('Mika \n(Os Quatro Magos Fundadores...)')
        self.jogo.after(3000, self.passo5)

    def passo5(self):
        self.jogo.mostrar_texto('O ambiente era adornado com belas pinturas, esculturas e adornos em ouro. Mas havia algo inquietante em tudo isso. Você ouvia alguns sussurros, mas não conseguia entender o que falavam, parecia que recitavam algo, ou tentavam dizer algo.')
        self.jogo.after(4000, self.passo6)

    def passo6(self):
        self.jogo.mostrar_texto('Ao final do imenso corredor, há uma grande sala. No meio dela, uma mesa.')
        self.jogo.after(2000, self.passo7)

    def passo7(self):
        self.jogo.mostrar_texto('“Altar das Convergências”')
        self.jogo.mostrar_texto('Está escrito em uma placa de ouro.')
        self.jogo.after(2000, self.passo8)

    def passo8(self):
        self.jogo.mostrar_texto('Os fragmentos “Verdade Humana”, “Coração do Mundo Verde” e “Memória do Arquimago” começam a brilhar, junto com seu amuleto.')
        self.jogo.after(2000, self.passo9_escolher_caminho)

    def passo9_escolher_caminho(self):
        self.jogo.mostrar_texto('Selecionar \n[1] COLOCAR OS FRAGMENTOS + AMULETO NO ALTAR')

        self.jogo.estado_jogo = self.passo9_processar_decisao
        self.jogo.esperar_resposta()

    def passo9_processar_decisao(self, decisao):
        if (decisao=='1'):
            self.jogo.mostrar_texto('Você tira o seu amuleto e o coloca no altar junto com os três fragmentos.')
            self.jogo.after(2000, self.passo10)
        else:
            self.jogo.mostrar_texto('Digite uma opção válida')
            self.jogo.after(1000, self.passo9_escolher_caminho)

    def passo10(self):
        self.jogo.mostrar_texto('Eles começam a brilhar fortemente e a flutuar, um fio de magia os interliga, era como se eles estivessem conversando.')
        self.jogo.after(2000, self.passo11)

    def passo11(self):
        self.jogo.mostrar_texto('As essências dos três fragmentos estavam sendo unidas e guardadas no seu amuleto.')
        self.jogo.after(3500, self.passo12)

    def passo12(self):
        self.jogo.mostrar_texto('No final do ritual, tudo volta ao normal. Os fragmentos param de brilhar, porém seu amuleto continua com aquela forte luz. Você sabe que é hora de seguir.')
        self.jogo.after(3000, self.fim)
    
    def fim(self):
        self.jogo.mostrar_texto('Você sai do Santuário dos Primevos.')
        self.jogo.after(3500, self.mudar_fase)



# ---  AGRADECIMENTO ---
class Fim(FasesBase):
    def iniciar(self):
        self.jogo.mostrar_texto('Olá! Agradecemos por jogar o nosso jogo!!')
        self.jogo.mostrar_texto('Esta foi uma demo, estamos trabalhando em atualizações para proporcionar uma melhor experiência e trazer o jogo completo. Ainda assim, esperamos ter proporcionado um bom momento para você.')
 