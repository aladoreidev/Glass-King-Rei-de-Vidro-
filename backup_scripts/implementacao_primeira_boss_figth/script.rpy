# --- COLOCAR NO TOPO DO SCRIPT.RPY ---
init python:
    import random

    respostas_maya = [
        "Oi Theo! Tô no meio de umas táticas aqui, falamos depois? ♟️",
        "Viu aquela partida do Magnus? Te mando o link mais tarde!",
        "Tô estudando a Defesa Caro-Kann, não consigo falar agora."
    ]
    
    respostas_leo = [
        "E aí fera! Agora não dá, tô levando um sacode no xadrez online. 😅",
        "Bora analisar umas partidas amanhã no clube?",
        "Tô saindo pra comer, depois a gente se fala!"
    ]

    respostas_luisa = [
        "Oi! Estou organizando o material do próximo torneio, te ligo depois? 😊",
        "Theo, você esqueceu sua anotação no clube? Eu guardei aqui.",
        "Não posso falar agora, mas amanhã chegarei cedo no clube!"
    ]

init python:
    # Nome, Rating Necessário, Label de destino
    lista_torneios = [
        ("Torneio Escolar", 1000, "torneio_escolar"),
        ("Copa Local", 1200, "copa_local"),
        ("Regional Amador", 1400, "regional_amador"),
        ("Aberto da Cidade", 1600, "aberto_cidade"),
        ("Estadual Sub-20", 1800, "estadual_sub20"),
        ("Memorial dos Mestres", 2000, "memorial_mestres"),
        ("Campeonato Nacional", 2200, "nacional"),
        ("Seletiva Internacional", 2400, "seletiva_inter"),
        ("Torneio dos Candidatos", 2600, "candidatos"),
        ("Campeonato Mundial", 2800, "mundial")
    ]

init python:
    import random

    # Esta é a lista que o seu erro diz que não existe (NameError)
    # Certifique-se de que os nomes das imagens (Ex: "puzzle01") existem na sua pasta images
    lista_puzzles_luisa = [
        ("puzzle01", "Luísa te colocou em xeque! Como sair?", "Rf1", "Kh8"),
        ("puzzle02", "O cavalo dela está ameaçando sua Dama. O que fazer?", "f4", "Dxd5"),
        ("puzzle03", "Final de peões. Qual a melhor casa para o Rei?", "Ke4", "Kg2"),
        ("puzzle04", "Tema de Cravada: Como ganhar a peça?", "Bb5", "a3"),
        ("puzzle05", "Sacrifício tático. O mate é inevitável?", "Sim", "Não")
    ]










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

# 1. Definição dos Personagens
define t = Character("Theo", color="#ffffff")
define l = Character("Léo", color="#2ecc71")   # Verde (Amigável/Equilibrado)
define ma = Character("Maya", color="#e91e63") # Rosa/Carmim (Intensa/Passional)
define lu = Character("Luisa", color="#95a5a6") # Cinza (Analítica/Fria)
define m = Character("Macedo", color="#7f8c8d") # Cinza Escuro (Antigo)


default theo_hp = 200
default theo_max = 200
default luisa_hp = 400
default luisa_max = 500
default round_atual = 1


# --- DEFINIÇÃO DE POSIÇÕES (TRANSFORMS) ---
# --- DEFINIÇÃO DE POSIÇÕES PADRONIZADAS ---
transform pos_leo:
    xalign 0.1 ypos 1.0 yanchor 1.0 zoom 0.3

transform pos_theo:
    xalign 0.5 ypos 1.0 yanchor 1.0 zoom 0.3

transform pos_luisa:
    xalign 0.95 ypos 1.0 yanchor 1.0 zoom 0.3

transform pos_maya:
    xalign 0.75 ypos 1.0 yanchor 1.0 zoom 0.3



screen status_boss_fight():
    # Barra do Theo (Esquerda)
    frame:
        xalign 0.05 yalign 0.05
        background Solid("#000000aa")
        padding (10, 10)
        vbox:
            text "Theo" size 22 color "#fff"
            bar value theo_hp range theo_max:
                xmaximum 300
                # Parte cheia (Verde)
                left_bar Solid("#2ecc71") 
                # Parte vazia/Fundo (Vermelho Escuro)
                right_bar Solid("#96281b") 
            text "[theo_hp] / [theo_max]" size 18 xalign 0.5

    # Barra da Luísa (Direita)
    frame:
        xalign 0.95 yalign 0.05
        background Solid("#000000aa")
        padding (10, 10)
        vbox:
            text "Luísa" size 22 color "#fff" xalign 1.0
            bar value luisa_hp range luisa_max:
                xmaximum 300
                bar_invert True # Mantém a lógica de esvaziar para o centro
                # Como está invertida, left e right trocam de função visual
                left_bar Solid("#96281b") # Fundo
                right_bar Solid("#2ecc71") # Vida
            text "[luisa_hp] / [luisa_max]" size 18 xalign 0.5













# 2. Ponto de Partida
label start:
    show screen status_personagem
    #Escolha por onde começar o teste:
    #jump cena_derrota_clube
    jump boss_fight_luisa

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
            $ theo_foco += 5
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

# --- DESAFIO PUZZLE ---

label mate_correto:
    show luisa normal at pos_luisa
    show maya feliz at pos_maya
    show theo feliz at pos_theo
    $ theo_rating += 25
    t "Xeque com o sacrifício de Dama em f7! Mate imparável!"
    jump segue_conversa_pizzaria

label erro_bispo:
    show luisa raiva at pos_luisa
    show theo triste at pos_theo
    t "Bispo em f7...?"
    lu "Errado. O Rei foge para h8."
    jump segue_conversa_pizzaria

label erro_torre:
    show luisa normal at pos_luisa
    show theo triste at pos_theo
    t "Torre em f8...?"
    lu "Tá Maluco, Theo. Você perde a Dama."
    jump segue_conversa_pizzaria

label segue_conversa_pizzaria:
    "Após o desafio, os vossos hambúrgueres finalmente chegam à mesa."
    "A noite termina com risadas, mas você sabe que amanhã o treino volta a ser sério."
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
    
    # EM VEZ DE: "Você se dedica aos estudos..."
    # USE O JUMP PARA O MINIGAME:
    jump hub_treinar

label proximo_dia:
    $ theo_foco = 100
    $ acoes_hoje = 0 
    scene black with fade
    "Você descansou e o dia passou..."
    jump abrir_hub

# --- LIGAÇÕES ---

label conversa_maya:
    if acoes_hoje >= 2:
        t "Já está muito tarde para mandar mensagem... melhor dormir."
        jump abrir_hub
    $ acoes_hoje += 1
    $ msg = random.choice(respostas_maya)
    "📲 Mensagem de Maya: [msg]"
    jump abrir_hub

label conversa_leo:
    if acoes_hoje >= 2:
        t "O Leo deve estar dormindo, não vou incomodar a essa hora."
        jump abrir_hub
    $ acoes_hoje += 1
    $ msg = random.choice(respostas_leo)
    "📲 Mensagem de Leo: [msg]"
    jump abrir_hub

label conversa_luisa:
    if acoes_hoje >= 2:
        t "Não quero mandar mensagem para a Luisa agora, é falta de educação."
        jump abrir_hub
    $ acoes_hoje += 1
    $ msg = random.choice(respostas_luisa)
    "📲 Mensagem de Luisa: [msg]"
    jump abrir_hub

# --- TORNEIOS ---

label torneio_escolar:
    $ acoes_hoje += 1
    "Você entrou no Torneio Escolar. O ginásio está cheio de estudantes."
    "Após várias partidas cansativas, você sente que aprendeu muito."
    $ theo_rating += 10 
    "Seu rating subiu para [theo_rating]!"
    jump abrir_hub

label copa_local:
    $ acoes_hoje += 1
    "A Copa Local é frequentada pelos veteranos da cidade. O nível é bem mais alto aqui."
    jump abrir_hub

label regional_amador:
    $ acoes_hoje += 1
    "Viajando para a regional... A pressão é grande."
    jump abrir_hub

label aberto_cidade:
    "Torneio Aberto da Cidade em desenvolvimento."
    jump abrir_hub

label estadual_sub20:
    "Estadual Sub-20 em desenvolvimento."
    jump abrir_hub

label memorial_mestres:
    "Memorial dos Mestres em desenvolvimento."
    jump abrir_hub

label nacional:
    "Campeonato Nacional em desenvolvimento."
    jump abrir_hub

label seletiva_inter:
    "Seletiva Internacional em desenvolvimento."
    jump abrir_hub

label candidatos:
    "Torneio dos Candidatos em desenvolvimento."
    jump abrir_hub

label mundial:
    "Campeonato Mundial em desenvolvimento."
    jump abrir_hub

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
    # 1. Configurações Iniciais e Reset de Status da Luta
    $ theo_hp = theo_max
    $ luisa_hp = luisa_max
    $ round_atual = 1
    
    # Sorteia 5 puzzles da lista exclusiva da Luísa
    $ puzzles_da_luta = random.sample(lista_puzzles_luisa, 5)
    
    scene bibliotecajogo 
    show luisa normal at pos_luisa:
        xalign 1.0 yalign 0.1 zoom 1.9
    show theo normal at pos_theo:
        xalign 0.3 yalign 0.1 zoom 1.9
        
    lu "Você evoluiu, Theo. Mas vamos ver como sua mente lida com a pressão real."

    show screen status_boss_fight

    # 2. Loop de Combate (5 Rounds)
    while round_atual <= 5:
        # Pega o puzzle do round
        $ puzzle = puzzles_da_luta[round_atual - 1]
        
        python:
            # Embaralha as opções
            opcoes = [[puzzle[2], True], [puzzle[3], False]]
            random.shuffle(opcoes)

        # Chama o puzzle (mostrar_fundo=False para manter a biblioteca visível)
        $ resultado = renpy.call_screen("tela_treinamento", puzzle_atual=puzzle, opcoes_sorteadas=opcoes, mostrar_fundo=False)

        if resultado:
            # --- LÓGICA DE ACERTO (Usa Foco e Estabilidade) ---
            python:
                base_dano = 20 + (theo_foco * 0.2) 
                multiplicador = 1.0 + (theo_estabilidade / 100.0)
                dano_final_theo = int((base_dano * multiplicador) + (theo_ousadia * 0.3))
                
                luisa_hp -= dano_final_theo
                # Acertar dá um bônus de Estabilidade
                theo_estabilidade = min(theo_estabilidade + 5, 100)
            
            with hpunch
            lu "Um movimento preciso! Você causou [dano_final_theo] de dano."

        else:
            # --- LÓGICA DE ERRO ---
            python:
                penalidade_ousadia = int(theo_ousadia * 0.6)
                dano_recebido = 15 + penalidade_ousadia
                theo_hp -= dano_recebido
                theo_foco = max(theo_foco - 10, 0)
                theo_estabilidade = max(theo_estabilidade - 10, 0)
            
            # 1. Mostra o flash
            show flash_vermelho
            with Dissolve(0.1)
            
            # 2. Garante que a Luísa continue aparecendo (Re-mostra a skin)
            # Isso força o Ren'Py a lembrar qual skin usar
            show luisa normal at pos_luisa 
            
            # 3. Esconde o flash
            hide flash_vermelho
            with Dissolve(0.2)
            
            # 4. Feedback visual e diálogo
            with vpunch
            lu "Lento demais! Você se arriscou e pagou o preço: -[dano_recebido] de HP."

        # Verifica morte instantânea
        if theo_hp <= 0:
            jump derrota_boss
        if luisa_hp <= 0:
            jump vitoria_boss

        $ round_atual += 1

    # 3. Verificação de Vencedor por Pontos
    if theo_hp >= luisa_hp:
        jump vitoria_boss
    else:
        jump derrota_boss

label vitoria_boss:
    hide screen status_boss_fight
    lu "Incrível... Xeque-mate. Você me venceu, Theo."
    $ theo_rating += 100
    $ theo_ousadia += 15 # Ganha ousadia pela vitória épica
    "Você derrotou Luísa! Rating: +100 | Ousadia: +15"
    jump abrir_hub

label derrota_boss:
    hide screen status_boss_fight
    lu "Ainda falta muito estudo. O tabuleiro não perdoa hesitação."
    "Você foi derrotado. Melhore seus status antes de tentar novamente!"
    jump abrir_hub



