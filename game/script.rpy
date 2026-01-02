

# --- Status do Jogador ---
default theo_rating = 1200      # Necessário p/ torneios (Ex: 1500 p/ o Regional, 2200 p/ Nacional)
default theo_foco = 50         # Influencia a chance de ignorar distrações (como a xícara)
default theo_estabilidade = 50  # Menor variação de performance sob pressão
default theo_ousadia = 50       # Libera jogadas arriscadas ou táticas agressivas
default acoes_hoje = 0

# --- Relacionamentos (Pontos de Afeto) ---
default afeto_leo = 0           # Amizade com o melhor amigo/rival
default afeto_maya = 0       # Substitua pelo nome da personagem
default afeto_luisa = 0       # Substitua pelo nome da personagem
# default pressao_theo = 0
# default pressao_enzo = 0


# 1. Definição dos Personagens
define t = Character("Theo", color="#ffffff")
define l = Character("Léo", color="#2ecc71")   # Verde (Amigável/Equilibrado)
define ma = Character("Maya", color="#e91e63") # Rosa/Carmim (Intensa/Passional)
define lu = Character("Luisa", color="#95a5a6") # Cinza (Analítica/Fria)
define m = Character("Macedo", color="#7f8c8d") # Cinza Escuro (Antigo)
define ph = Character("Dr. Henrique", color="#7f8c8d") # Cor cinza sóbria
define enz = Character("Enzo", color="#e74c3c")


#Hh para Boss Figth
default theo_hp = 200
default theo_max = 200
default luisa_hp = 200
default luisa_max = 200
default enzo_max = 300
default dano_recebido = 0  

default round_atual = 1

# Mensagens 
default nova_msg_maya = False
default nova_msg_leo = False
default nova_msg_luisa = False

# Para garantir que eles não mandem a mesma mensagem várias vezes
default msg_luisa_derrotada_lida = False
default persistent.luisa_derrotada = False
default persistent.enzo_derrotado = False
default msg_enzo_derrotado_lida = False # Caso queira usar essa trava específica



# --- DEFINIÇÃO DE POSIÇÕES (TRANSFORMS) --- Fullbody e Busto

# --- POSIÇÕES Fullboddy (Novas) ---
transform pos_leo:
    xalign 0.1 ypos 1.0 yanchor 1.0 zoom 0.3

transform pos_theo:
    xalign 0.5 ypos 1.0 yanchor 1.0 zoom 0.3

transform pos_luisa:
    xalign 0.95 ypos 1.0 yanchor 1.0 zoom 0.3

transform pos_maya:
    xalign 0.75 ypos 1.0 yanchor 1.0 zoom 0.3

# --- POSIÇÕES BUSTO (Novas) ---
transform leo_busto:
    xalign 0.1 ypos 2.0 yanchor 1.0 zoom 0.6

transform theo_busto:
    xalign 0.5 ypos 2.0 yanchor 1.0 zoom 0.6

transform luisa_busto:
    xalign 0.95 ypos 2.0 yanchor 1.0 zoom 0.6

transform maya_busto:
    xalign 0.75 ypos 2.0 yanchor 1.0 zoom 0.6







# 2. Ponto de Partida
label start:
    show screen status_personagem
    #Escolha por onde começar o teste:
    #jump cena_derrota_clube
    #jump boss_fight_luisa
    #jump boss_fight_enzo
    #jump abrir_hub
    jump convidar_maya_para_role

# 3. Cena do Clube
label cena_derrota_clube:
    scene clubexadrez with fade

    "Clube de Xadrez Ala do Rei"
    "Março de 2015"

    show macedolado:
        xalign 0.05   
        yalign 0.35   
        zoom 0.7      

    show theolado:
        xalign 0.5   
        yalign 0.20   
        zoom 0.6      
    
    "O silêncio no Clube de Xadrez Ala do Rei era quase sólido, cortado apenas pelo tique-taque rítmico e implacável do relógio."
    "Para muitos, Theo não era apenas um jogador; era o prodígio local, a grande promessa destinada a ostentar o título de Grande Mestre e colocar o país no mapa do xadrez mundial."
    "Sua mente funcionava como um supercomputador, processando centenas de variantes em segundos... mas por trás dessa genialidade, escondia-se uma fissura perigosa."
    "Theo era volátil. Sua concentração, embora profunda, era uma lâmina de vidro: brilhante, porém capaz de se estilhaçar com o menor ruído ou provocação."
    "Macedo, um veterano cujas mãos carregavam o cheiro de tabaco e cujas vitórias carregavam o cheiro da dúvida, conhecia bem os segredos daquele salão."
    "Conhecido por um estilo de jogo 'sujo' e psicológico, o velho mestre não estava ali para vencer no tabuleiro... ele estava ali para quebrar a mente de Theo."
       
    t "Eu juro que calculei todas as variantes..."
    "As pessoas começavam a se aglomerar em volta da Mesa 1. O burburinho era baixo, mas a eletricidade no ar era evidente: a última rodada do torneio estava sendo decidida entre o jovem talento e o velho matreiro."
    t "Vamos, Theo, se concentra... Se Cavalo f3, Bispo, g5..."
    
    "Macedo percebeu a oportunidade perfeita. Ele parou de olhar para as casas do tabuleiro e passou a encarar o suor frio que escorria pela têmpora de Theo."
    "A cada movimento, Macedo não apenas posicionava as peças; ele as cravava no tabuleiro como se martelasse pregos em madeira bruta."
    "O pobre relógio também sofria. A cada pancada seca no botão metálico, o coração de Theo saltava, saindo perigosamente do compasso."

    t "Droga, perdi a linha de raciocínio..."
    "o suor escorria de sua tempora..."
    m "Cof... cof... cof..."

    "Macedo deslizou a Torre com uma confiança irritante. O som da base de feltro contra a madeira soou como uma sentença."
    "Mas Theo estava em vantagem, a linha que ele estava calculando era vencedora..."
    "Macedo sente que the posição está saindo do controle e apela..."
    "Começa a bater repetidamente o anel de metal na mesa... "
    "Theo, tenta ignorar...mas está cada vez mais difícil..."
    "O Árbitro adverte o velho Macedo..."
    "O ar parecia parado, denso como chumbo. Theo estava a um passo de consolidar sua vantagem... Mas, então, veio o golpe final. Não partiu do tabuleiro, mas do destino."
    "No fundo do salão, uma xícara de café escorregou de uma mesa. O tempo pareceu desacelerar enquanto a porcelana viajava em direção ao chão."

    play sound "audio/glasscrash2.ogg"
    "{b}CRACH!{/b}"

    "O som estridente da porcelana se desfazendo em mil pedaços ecoou pelas paredes de madeira como uma explosão. Foi o suficiente."
    "A mão de Theo fraquejou. O susto percorreu seu braço como uma corrente elétrica, fazendo-o soltar o Bispo na casa errada. O estalo da peça na posição fatal selou seu destino."
    "O silêncio que se seguiu foi sepulcral. Theo olhou para o tabuleiro e sentiu o sangue fugir do rosto. Era o fim. Sua Dama estava pendurada, entregue à própria sorte."
    "Nesse instante, o rosto de Macedo sofreu uma metamorfose sombria. A máscara carrancuda e as rugas de raiva acumulada deram lugar a algo muito pior: um sorriso malicioso que se espalhava lentamente."
    "Ele não apenas venceu; ele saboreou o momento em que a mente do jovem prodígio se estilhaçou junto com a xícara."

    m "Hehehehehehe..."
    m "O xadrez é um jogo de nervos, rapaz... e os seus acabam de virar poeira."
    m "Xeque-mate. Um belo Raio-X, não acha?"
    t "O quê?! A minha Dama... eu não queria soltar o Bispo ali!"

    # --- APLICAÇÃO DAS PERDAS DE STATUS ---
    $ theo_rating -= 30
    $ theo_foco -= 20
    $ theo_estabilidade -= 10
    $ theo_ousadia += 5
    # ---------------------------------------

    "Você sente um peso esmagador no peito. O silêncio do clube agora parece zombar de você."
    m "Hehehehe... Volte para casa, rapaz. O tabuleiro não é lugar para quem se assusta com xícaras quebradas."

    menu:
        "Encarar o velho Macedo":
            $ theo_ousadia += 10
            "Theo respira fundo, ignorando o tremor nas mãos. Ele levanta a cabeça e encara as rugas profundas e o sorriso vitorioso de Macedo."
            t "Foi um bom golpe... mas não espere que a sorte te ajude da próxima vez."
            m "Sorte? Hehehe... Chame do que quiser, rapaz. Mas o placar diz que eu ainda sou o rei desta mesa."
            "O olhar desafiador de Theo atrai a atenção de quem estava em volta. Ele perdeu o jogo, mas não a dignidade."

        "Abandonar o salão imediatamente":
            $ theo_estabilidade += 5
            $ theo_ousadia -= 5
            "Theo não consegue dizer uma palavra. O som da xícara quebrando ainda ecoa em sua mente como um trovão."
            "Ele junta suas coisas às pressas, sentindo o peso dos olhares de pena e deboche sobre suas costas."
            "O ar lá fora parece subitamente frio enquanto ele atravessa a porta, deixando o 'hehehe' de Macedo para trás."

    "A noite cai sobre a cidade, e o silêncio agora é o único companheiro de Theo."
    jump encontro_amigos_pos_derrota

# Cena do lado de fora do Clube
label encontro_amigos_pos_derrota:
    scene ruanoite with fade

    # Theo no centro com o novo padrão
    show theo feliz at pos_theo 

    "O ar gelado da noite ajuda a baixar a adrenalina, mas o silêncio é logo interrompido por passos rápidos."

    # Léo aparece na esquerda
    show leo raiva at pos_leo
    
    l "Theo! Cara, que bizarro foi aquilo?..." 
    
    show theo normal 
    t "Não exagera, Léo..."

    # Luisa aparece na direita
    show luisa normal at pos_luisa with moveinright
    
    lu "Não vejo graça nisso, Léo. Xadrez é autocontrole..."
    
    show theo triste 
    lu "Se você quer chegar ao Nacional..."

    # Maya aparece entre o Theo e a Luisa
    show maya feliz at pos_maya with dissolve
    
    ma "Menos, Luisa. Ninguém precisa de uma autópsia da partida..."

    show theo normal
    "Maya se aproxima um pouco mais, e o tom de voz dela suaviza."
    ma "Você jogou bem até o incidente, Theo. Teve uma linha de ataque na abertura que foi... brilhante."
    ma "Não deixe o erro final apagar o que você construiu antes."

    $ afeto_maya += 5 

    menu:
        "Agradecer o apoio de Maya":
            $ afeto_maya += 10
            $ theo_estabilidade += 5
            t "Obrigado, Maya. Eu precisava ouvir isso. Luisa... você está certa sobre o foco, mas não precisa ser tão dura."
            lu "A verdade dói, Theo. Acostume-se."

        "Dar razão à critica de Luisa":
            $ afeto_luisa += 5
            $ theo_estabilidade += 10
            $ theo_ousadia -= 5
            t "A Luisa está certa. Eu fui fraco. Não posso culpar uma xícara pela minha falta de cálculo."
            lu "Finalmente um pouco de autocrítica. Agora, trate de voltar aos livros."
            ma "Cuidado para não ser seco demais, Theo. Coração de pedra não sente o fluxo do jogo."

        "Fazer uma piada junto com Léo":
            $ afeto_leo += 15
            $ theo_ousadia += 5
            t "É, Léo... acho que o relógio vai precisar de terapia depois de hoje."
            l "Hahaha! Boa! Vamos comer uma pizza, eu pago. O Rating a gente recupera, mas a minha fome é urgente!"

    "O clima entre o grupo começa a suavizar conforme vocês se afastam do clube."

    show leo feliz at pos_leo 
    l "Pô galerinha, a minha barriga tá roncando mais alto que o relógio do Macedo! O que vocês acham da gente colar lá na 'CheckMate Burguer'?"
    l "Dizem que o 'X-Bispo' de lá é imbatível, quase um xeque-mate no estômago!"

    show theo normal at pos_theo
    t "Sabe de uma coisa? Eu topo. Acho que se eu ficar sozinho em casa agora, vou acabar jogando meu tabuleiro pela janela."

    show luisa raiva at pos_luisa 
    lu "Como é que é? Theo, você acabou de sofrer uma derrota técnica por falta de foco e sua solução é... comer um hambúrguer?"
    lu "Você deveria ir direto para o motor de análise. Cada minuto que você passa mastigando é um minuto a menos revisando onde sua estrutura de peões colapsou."

    show maya feliz at pos_maya 
    ma "Relaxa, Luisa. O cérebro dele ferveu lá dentro. Se ele tentar analisar algo agora, vai acabar confundindo o Rei com um pão de batata."

    show maya normal 
    ma "Eu apoio o Léo. Por incrível que pareça, he teve uma ideia decente hoje. Vamos, Theo. A primeira rodada de fritas é por minha conta, pra compensar seu Rating perdido."

    show leo feliz
    l "Aê! Viu só? Até a Maya reconheceu minha genialidade oculta. Vamos logo antes que a Luisa comece a dar aula de abertura no meio da calçada!"

    # Transição para a lanchonete
    hide leo
    hide theo
    hide luisa
    hide maya
    with fade
    
    # Cena da Lanchonete Checkmate Burguer
    
    scene checkmateburger with fade
    
    "A lanchonete está movimentada. O cheiro de hambúrguer grelhado e o som de relógios de xadrez batendo nas mesas ao fundo criam um ambiente acolhedor."

    show leo feliz at pos_leo
    show theo normal at pos_theo
    show luisa normal at pos_luisa
    show maya feliz at pos_maya
    with dissolve

    l "Finalmente! Se eu demorasse mais cinco minutos, eu ia começar a comer as peças do meu tabuleiro reserva."
    t "O lugar está cheio hoje. Pelo menos aqui ninguém parece se importar se alguém 'pendura' uma dama."
    show luisa normal at pos_luisa
    lu "Na verdade, Theo, a mesa 4 ali atrás está jogando uma Variante Tartakower bem interessante. Eu deveria ir lá dar uma olhada..."
    ma "Nada disso, Luisa! Hoje é noite de descompressão. Senta aí."

    show leo feliz at pos_leo
    l "Ei, Theo! Para de olhar para o cardápio e olha para isso aqui. Vi um carinha postar no fórum hoje cedo."
    "Léo rabisca rapidamente um diagrama de xadrez em um guardanapo engordurado e empurra para o centro da mesa."
    l "Ele disse que é 'Mate em 2', mas eu acho que ele fumou meia. O que você acha? Se acertar, eu pago o seu refrigerante!"

    call screen puzzle_guardanapo_circles

# --- DESAFIO PUZZLE: Do Guardanapo ---

label mate_correto:
    show luisa normal at pos_luisa
    show maya feliz at pos_maya
    show theo feliz at pos_theo
    $ theo_rating += 25
    $ theo_foco += 5
    t "Xeque com o sacrifício de Dama em f7! Mate imparável!"
    jump segue_conversa_pizzaria

label erro_bispo:
    show luisa raiva at pos_luisa
    show theo triste at pos_theo
    t "Bispo em f7...?"
    lu "Errado. O Rei foge para h8."
    $ theo_rating -= 25
    $ theo_foco -= 5
    $ theo_ousadia -= 5
    jump segue_conversa_pizzaria

label erro_torre:
    show luisa normal at pos_luisa
    show theo triste at pos_theo
    t "Torre em f8...?"
    lu "Tá Maluco, Theo. Você perde a Dama."
    $ theo_rating -= 25
    $ theo_estabilidade -= 5
    $ theo_ousadia -= 5
    jump segue_conversa_pizzaria

label segue_conversa_pizzaria:
    "Após o desafio, os vossos hambúrgueres finalmente chegam à mesa."
    "A noite termina com risadas, mas você sabe que amanhã o treino volta a ser sério."
    jump flashback_infancia


# --- SCREEN DO PUZZLE (Apenas para garantir que funcione se não estiver em outro arquivo) ---
screen puzzle_guardanapo_circles():
    zorder 100
    modal True
    vbox:
        xalign 0.95 yalign 0.2 spacing 20
        add "desafioguardanapo" zoom 0.45
        hbox:
            xalign 0.5 spacing 15
            button:
                action Jump("mate_correto")
                background Frame(Solid("#4CAF50"), 0, 0)
                xminimum 120 yminimum 120 padding (5, 5)
                text "Dxf7+" align (0.5, 0.5) size 18 color "#fff" bold True
            button:
                action Jump("erro_bispo")
                background Frame(Solid("#F44336"), 0, 0)
                xminimum 120 yminimum 120 padding (5, 5)
                text "Bxf7+" align (0.5, 0.5) size 18 color "#fff" bold True
            button:
                action Jump("erro_torre")
                background Frame(Solid("#2196F3"), 0, 0)
                xminimum 120 yminimum 120 padding (5, 5)
                text "Tf8" align (0.5, 0.5) size 18 color "#fff" bold True


#Flashback infância

label flashback_infancia:
    scene escritotiodrhenrique with fade # Um fundo de biblioteca ou escritório clássico
    play music "audio/tension_piano.mp3" fadein 2.0

    "Dez anos atrás..."

    "O escritório cheirava a couro e papel antigo. O único som era o do relógio de parede, rítmico e implacável."
    
    # Theo criança (você pode usar um zoom no sprite ou apenas texto)
    "Eu tinha apenas oito anos. Estava escondido atrás da poltrona, tentando resolver um problema de mate em dois num tabuleiro de bolso."

    show drhenrique normal at center with dissolve:
        zoom 0.45

    ph "Theodoro? O que eu disse sobre esses... brinquedos no meu escritório?"

    "Tentei fechar o tabuleiro rapidamente, mas as peças de plástico fizeram um barulho seco no chão de madeira."

    t "Eu... eu já terminei o dever de latim, pai. Só estava praticando um pouco."

    ph "Praticando? Pratica-se piano, pratica-se retórica, pratica-se o Direito."
    ph "Isso que você segura é um passatempo para quem não tem um legado a carregar."

    "Ele caminhou até mim. Cada passo parecia uma sentença judicial."

    show drhenrique raiva at center with dissolve:
        zoom 0.45

    ph "A vida não é um tabuleiro com regras claras e turnos alternados, meu filho."
    ph "A vida é uma disputa de influência. Enquanto você move cavalos de plástico, os seus concorrentes estão movendo o mundo real."

    "Ele pegou o tabuleiro da minha mão. Não com raiva, mas com uma frieza que doía muito mais."

    show drhenrique triste at center with dissolve:
        zoom 0.45
    ph "Vou guardar isso. Quando você for um Procurador, terá tempo para jogos de tabuleiro. Até lá, foque no que importa."

    stop music fadeout 3.0
    scene black with dissolve
    
    "Aquelas palavras ficaram gravadas. Cada vez que toco em uma peça, sinto o peso do olhar dele sobre meus ombros."

    $ theo_estabilidade -= 30

    jump abrir_hub

# --- SISTEMA DO HUB ---

label abrir_hub:
    scene singlebedroom with fade 
    call screen hub_principal
    return

label preparar_treino:
    if acoes_hoje >= 2:
        t "Já fiz muita coisa hoje, estou exausto. Melhor ir dormir."
        jump abrir_hub

    if theo_foco < 20:
        t "Estou sem foco para treinar agora..."
        jump abrir_hub

    # Se passou nas verificações acima, o treino começa:
    $ acoes_hoje += 1
       
    jump hub_treinar

label proximo_dia:
    #$ theo_foco = 100
    $ acoes_hoje = 0 
    scene black with fade
    "Você descansou e o dia passou..."
    jump abrir_hub

# --- LIGAÇÕES ---

screen tela_chat(personagem_nome, personagem_avatar, mensagem_texto):
    modal True
    add Solid("#000000cc") # Escurece o fundo do jogo

    # Container principal que centraliza o celular na tela
    fixed:
        xalign 0.5 yalign 0.5
        xsize 500 ysize 900 # Tamanho aproximado da imagem do celular

        # 1. A Imagem do Smartphone
        add "smartphone" xalign 0.5 yalign 0.5

        # 2. O Conteúdo (alinhado apenas na parte preta da tela)
        # Ajustamos as margens (padding) para o texto não bater nas bordas da tela preta
        vbox:
            xalign 0.5
            ypos 0.22 # Começa logo abaixo da barra de status (sinal/bateria)
            xsize 320 # Largura exata da área preta da tela
            spacing 20

            # Cabeçalho (Avatar e Nome)
            hbox:
                spacing 15
                xalign 0.1
                add personagem_avatar zoom 0.8 # Diminui o ícone se estiver grande
                
                vbox:
                    yalign 0.5
                    text "[personagem_nome]" color "#ffffff" size 22 bold True
                    text "online" color "#4df14d" size 14

            # Área da Mensagem (Balão)
            frame:
                background Frame(Solid("#2c3e50"), 10, 10) # Balão escuro
                padding (15, 15, 15, 15)
                xsize 300
                xalign 0.5
                
                text "[mensagem_texto]":
                    color "#ffffff"
                    size 20
                    line_spacing 5

            null height 100 # Espaço para o botão não ficar em cima do texto

            # Botão Fechar (Posicionado onde seria o botão "Home" do celular)
            textbutton "FECHAR":
                action Return()
                xalign 0.5
                ypos 0.85 # Ajusta para ficar perto do círculo branco debaixo
                style "hub_button"
                text_size 18
label conversa_maya:
    if persistent.enzo_derrotado and not msg_enzo_derrotado_lida:
        # Incrementos ANTES da tela
        $ theo_estabilidade += 1
        $ nova_msg_maya = False
        $ msg_enzo_derrotado_lida = True
        call screen tela_chat("Maya", "mayaicone", "Theo! O clube tá fervendo!Você derrotou o Enzo Dias, ele bem que mereceu...")
        jump abrir_hub

    elif persistent.luisa_derrotada and nova_msg_maya:
        $ theo_estabilidade += 1
        $ nova_msg_maya = False
        call screen tela_chat("Maya", "mayaicone", "Theo! Eu nem acredito, a luisa veio se lamentar pela derrota na partida entre vocês...")
        jump abrir_hub
    
    else:
        $ msg_para_celular = random.choice(respostas_maya)
        call screen tela_chat("Maya", "mayaicone", msg_para_celular)
    jump abrir_hub

label conversa_leo:
    if persistent.enzo_derrotado and nova_msg_leo:
        $ theo_ousadia += 1 # Movemos para cima
        $ nova_msg_leo = False
        call screen tela_chat("Leo", "leoicone", "Mano, você passou pelo Enzo? Cara, que loucura. O moleque era carne de pescoço...")
        jump abrir_hub

    elif persistent.luisa_derrotada and nova_msg_leo:
        $ theo_ousadia += 1 # Movemos para cima
        $ nova_msg_leo = False
        call screen tela_chat("Leo", "leoicone", "Cara, bater a Luísa jogando contra a Francesinha dela, surreal...")
        jump abrir_hub
    
    else:
        $ msg_para_celular = random.choice(respostas_leo)
        call screen tela_chat("Leo", "leoicone", msg_para_celular)
    jump abrir_hub

label conversa_luisa:
    if persistent.enzo_derrotado and nova_msg_luisa:
        $ theo_foco += 5 # Dei um bônus maior aqui por ser o Enzo
        $ nova_msg_luisa = False
        call screen tela_chat("Luísa", "luisaicone", "Então você superou o Enzo, ótimo, mas vi que dava pra ter ganho sem sofrer tanto...")
        jump abrir_hub

    elif persistent.luisa_derrotada and nova_msg_luisa:
        $ theo_foco += 5
        $ nova_msg_luisa = False
        call screen tela_chat("Luísa", "luisaicone", "Analisei nossa partida, depois te mando o PGN, eu tinha uma linha que igualava, mas não viSSSSS...")
        jump abrir_hub
    
    else:
        $ msg_para_celular = random.choice(respostas_luisa)
        call screen tela_chat("Luísa", "luisaicone", msg_para_celular)
    jump abrir_hub



# # --- TORNEIOS ---

# label torneio_escolar:
#     $ acoes_hoje += 1
#     "Você entrou no Torneio Escolar. O ginásio está cheio de estudantes."
#     "Após várias partidas cansativas, você sente que aprendeu muito."
#     $ theo_rating += 10 
#     "Seu rating subiu para [theo_rating]!"
#     jump abrir_hub

# label copa_local:
#     $ acoes_hoje += 1
#     "A Copa Local é frequentada pelos veteranos da cidade. O nível é bem mais alto aqui."
#     jump abrir_hub

# label regional_amador:
#     $ acoes_hoje += 1
#     "Viajando para a regional... A pressão é grande."
#     jump abrir_hub

# label aberto_cidade:
#     "Torneio Aberto da Cidade em desenvolvimento."
#     jump abrir_hub

# label estadual_sub20:
#     "Estadual Sub-20 em desenvolvimento."
#     jump abrir_hub

# label memorial_mestres:
#     "Memorial dos Mestres em desenvolvimento."
#     jump abrir_hub

# label nacional:
#     "Campeonato Nacional em desenvolvimento."
#     jump abrir_hub

# label seletiva_inter:
#     "Seletiva Internacional em desenvolvimento."
#     jump abrir_hub

# label candidatos:
#     "Torneio dos Candidatos em desenvolvimento."
#     jump abrir_hub

# label mundial:
#     "Campeonato Mundial em desenvolvimento."
#     jump abrir_hub


# Boss Fight 1 (Enzo)

screen interface_duelo_mental():
    # Esta tela mostra as barras de pressão do Super Trunfo
    
    # Barra do Theo (Esquerda)
    vbox:
        xalign 0.15 yalign 0.05
        text "Pressão Theo: [pressao_theo]/10" size 20 color "#ffffff"
        bar:
            value AnimatedValue(pressao_theo, 10)
            xsize 300 ysize 20
            left_bar Solid("#ff0000") # Vermelho
            right_bar Solid("#333")

    # Barra do Enzo (Direita)
    vbox:
        xalign 0.85 yalign 0.05
        text "Pressão Enzo: [pressao_enzo]/10" size 20 color "#ffffff"
        bar:
            value AnimatedValue(pressao_enzo, 10)
            xsize 300 ysize 20
            left_bar Solid("#00ff00") # Verde
            right_bar Solid("#333")











# 1. Coloque isso fora de qualquer label (no topo do script)
default escolha_jogador = 0
default correta = 0

label boss_fight_enzo:
    $ pressao_theo = 0
    $ pressao_enzo = 0
    $ perguntas_disponiveis = list(puzzles_xadrez.keys())

    show screen interface_duelo_mental
    scene bibliotecajogo 
    show enzo normal at right:
        zoom 0.7
        yalign 0.9

    show theo normal at left:
        zoom 1.1
        yalign 1
    
    enz "O xadrez não é apenas mover peças, Theo. É conhecer a história e as regras."

label loop_quiz:
    if pressao_theo >= 10:
        jump derrota_mental_enzo
    if pressao_enzo >= 10:
        jump vitoria_mental_enzo
    
    if not perguntas_disponiveis:
        "As perguntas acabaram! Empate técnico."
        return

    python:
        pergunta_atual = random.choice(perguntas_disponiveis)
        perguntas_disponiveis.remove(pergunta_atual)
        dados = puzzles_xadrez[pergunta_atual]
        resp_a = dados[0]
        resp_b = dados[1]
        resp_c = dados[2]
        correta = dados[3] # A resposta correta fica guardada aqui

    enz "[pergunta_atual]"

    menu:
        "[resp_a]":
            $ escolha_jogador = 0
            jump checar_resposta
        "[resp_b]":
            $ escolha_jogador = 1
            jump checar_resposta
        "[resp_c]":
            $ escolha_jogador = 2
            jump checar_resposta

label checar_resposta:
    # Aqui fazemos a comparação fora do menu para evitar o NameError
    if escolha_jogador == correta:
        $ pressao_enzo += 1
        "Resposta correta! Você ganha terreno no tabuleiro."
        enz "Lógica impecável... continue assim."
    else:
        $ pressao_theo += 1
        with vpunch
        "Resposta errada! Enzo pune sua falta de conhecimento."
        enz "Você ainda é um amador, garoto."

    jump loop_quiz

label vitoria_mental_enzo:
    # ... seus diálogos de vitória aqui ...
    
    # GATILHOS DAS MENSAGENS:
    hide screen interface_duelo_mental
    $ theo_rating += 150
    $ theo_foco += 15
    $ theo_estabilidade += 10
    $ theo_ousadia += 5
    $ persistent.enzo_derrotado = True # Nova trava de história
    $ nova_msg_maya = True
    $ nova_msg_leo = True
    # Se a Luisa já foi derrotada, ela também manda mensagem:
    $ nova_msg_luisa = True
    $ acoes_hoje += 1  
    enz "Admito... sua base teórica é superior à minha expectativa."
    
    "Você derrotou o mestre da técnica. O silêncio no clube é quebrado apenas pelas notificações no seu bolso."
    
    jump abrir_hub # Ou o nome da sua label que chama o Hub

label derrota_mental_enzo:
    hide screen interface_duelo_mental
    enz "Estude mais. O tabuleiro não perdoa a ignorância."
    $ theo_rating -= 250
    $ theo_foco -= 15
    $ theo_ousadia -= 20
    $ theo_estabilidade -= 30
    $ acoes_hoje += 1 # Conta como uma atividade feita
    jump abrir_hub


#Boss Fight 2 (Luisa)

label calcular_poder_combate:
    python:
        # Foco define a base: Foco alto = mais força.
        # Se foco é 100, base é 40. Se foco é 20, base é 24.
        base_dano = 20 + (theo_foco * 0.2) 
        
        # Estabilidade é o multiplicador (ex: Estabilidade 50 = 1.5x de dano)
        multiplicador = 1.0 + (theo_estabilidade / 100.0)
        
        # Ousadia adiciona um bônus fixo, mas aumenta muito o risco
        dano_final_theo = int(base_dano * multiplicador + (theo_ousadia * 0.5))
        
        # Penalidade de Erro: Se errar, o dano recebido sobe com a Ousadia
        # Base de erro é 20. Se Ousadia for 100, Theo perde 70 de HP!
        dano_recebido_theo = 20 + int(theo_ousadia * 0.5)
    return


image flash_vermelho = Solid("#ff0000")


label boss_fight_luisa:
    # 1. Configurações Iniciais e Reset de Status
    $ theo_hp = theo_max
    $ luisa_hp = luisa_max
    $ round_atual = 0
    
    # Prepara a lista de puzzles para a luta
    $ puzzles_disponiveis = lista_puzzles_luisa[:]
    $ random.shuffle(puzzles_disponiveis)

    # Cenário e Personagens
    scene bibliotecajogo 
    show luisa normal at pos_luisa:
        xalign 1.0 yalign 0.1 zoom 1.9
    show theo normal at pos_theo:
        xalign 0.3 yalign 0.1 zoom 1.9
        
    lu "Você evoluiu, Theo. Mas vamos ver como sua mente lida com a pressão real."

    # Mostra a interface de HP
    show screen status_boss_fight

    # 2. Loop de Combate (Dura até alguém zerar o HP)
    while theo_hp > 0 and luisa_hp > 0:
        $ round_atual += 1

        # Verifica se precisa recarregar os puzzles
        if not puzzles_disponiveis:
            $ puzzles_disponiveis = lista_puzzles_luisa[:]
            $ random.shuffle(puzzles_disponiveis)
        
        # Pega um puzzle e prepara as opções
        $ puzzle = puzzles_disponiveis.pop()
        python:
            opcoes = [[puzzle[2], True], [puzzle[3], False]]
            random.shuffle(opcoes)

        # Chama a tela do puzzle
        $ resultado = renpy.call_screen("tela_treinamento", puzzle_atual=puzzle, opcoes_sorteadas=opcoes, mostrar_fundo=False)

        if resultado:
            # --- LÓGICA DE ACERTO ---
            python:
                base_dano = 20 + (theo_foco * 0.2) 
                multiplicador = 1.0 + (theo_estabilidade / 100.0)
                dano_final_theo = int((base_dano * multiplicador) + (theo_ousadia * 0.3))
                
                luisa_hp -= dano_final_theo
                theo_estabilidade = min(theo_estabilidade + 5, 100)
            
            with hpunch
            lu "Um movimento preciso! Você causou [dano_final_theo] de dano."

        else:
            # --- LÓGICA DE ERRO ---
            python:
                # Usamos 'store.' para garantir que o diálogo [dano_recebido] funcione
                penalidade_ousadia = int(theo_ousadia * 0.6)
                store.dano_recebido = 15 + penalidade_ousadia
                theo_hp -= store.dano_recebido
                theo_foco = max(theo_foco - 10, 0)
                theo_estabilidade = max(theo_estabilidade - 10, 0)
            
            show flash_vermelho zorder 100
            with Dissolve(0.1)
            
            show luisa normal at pos_luisa zorder 50
            
            hide flash_vermelho
            with Dissolve(0.2)
            
            with vpunch
            # Agora o Ren'Py vai encontrar a variável store.dano_recebido
            lu "Sua leitura de jogo foi amadora. Você entregou a posição e agora está pagando o preço: [dano_recebido] de dano!"

        # Verificação de fim de luta dentro do loop para interrupção imediata
        if theo_hp <= 0:
            jump derrota_boss
        if luisa_hp <= 0:
            jump vitoria_boss

    return

# --- RESULTADOS ---

label vitoria_boss:
    hide screen status_boss_fight
    show luisa raiva # Expressão de quem perdeu
    lu "Incrível... Xeque-mate. Você me venceu, Theo."
    $ persistent.luisa_derrotada = True
    $ theo_rating += 100
    $ theo_ousadia += 15
    $ nova_msg_maya = True
    $ nova_msg_leo = True
    $ nova_msg_luisa = True
    $ acoes_hoje += 1 
    "Vitória épica! Luísa reconhece seu talento. Rating +100."
   
    jump abrir_hub


label derrota_boss:
    "Suas energias se esgotaram e você não consegue mais manter a concentração no tabuleiro."
    "O adversário percebe sua hesitação e finaliza a partida com precisão."
    "Theo: (Droga... eu preciso estudar mais a tática deles...)"
    
    # Penalidade leve para dar peso à derrota
    $ theo_foco = max(10, theo_foco - 10)
    $ acoes_hoje += 1 
    $ theo_rating -= 150
    $ theo_ousadia -= 20
    $ theo_foco -= 10
    $ theo_estabilidade -= 10
    # Faz o jogo voltar para o mapa principal
    jump abrir_hub




