# --- COLOCAR NO TOPO DO SCRIPT.RPY ---
init python:
    import random





    #Respostas das Mensagens Enviadas pelos amigos
    respostas_maya = respostas_maya = [
        "Oi Theo! Tô no meio de umas táticas aqui, falamos depois? ♟️",
        "Viu aquela partida do Magnus? Te mando o link mais tarde!",
        "Tô estudando a Defesa Caro-Kann, não consigo falar agora.",
        "A tática de hoje estava impossível! Quase quebrei a cabeça. 🤯",
        "Você viu a nova linha que o pessoal tá usando na Siciliana? Doidera!",
        "Tô revisando minhas partidas do último torneio... Errei coisas bobas.",
        "Ei! Se vir o Leo, diz pra ele que ele ainda me deve uma revanche!",
        "Acabei de achar um puzzle de mate em 5 que é a sua cara. Vou te mandar."
        "Theo! Tirei 10 na prova de Filosofia! O professor até elogiou meu ensaio. ✨",
        "Você ouviu o boato de que a Letícia está saindo com o capitão do time de basquete?",
        "Minha playlist de lofi hoje tá batendo certinho com o clima de chuva.",
        "Não aguento mais estudar Biologia... Por que eu preciso saber o que é uma mitocôndria?",
        "Tô pensando em mudar a cor do meu cabelo, o que você acha de um azul escuro?",
        "Vi você passando no corredor hoje, parecia que estava em outro planeta! kkkk",
        "O café da cantina hoje está parecendo água suja, não compre!"
    ]
    
    respostas_leo = respostas_leo = [
        "E aí fera! Agora não dá, tô levando um sacode no xadrez online. 😅",
        "Bora analisar umas partidas amanhã no clube?",
        "Tô saindo pra comer, depois a gente se fala!",
        "Cara, acabei de pendurar a dama num mouse-slip... Quero chorar. 💀",
        "Xadrez é legal, mas você já tentou dormir 12 horas seguidas? Recomendo.",
        "Tava vendo umas aberturas duvidosas aqui. O Gambito do Rei é muito divertido, kkkk!",
        "Se a Luísa perguntar, eu tô estudando finais de torres, tá? (Na verdade tô jogando videogame).",
        "Theo, me ajuda! Entrei num torneio 'Bullet' e meus dedos não acompanham!"
        "Cara, você não sabe da maior! O monitor de Física foi pego colando na própria prova! 😂",
        "Mano, é verdade que a fulaninha tá ficando com a Maria? O pessoal tá comentando no grupo.",
        "Tô aqui na aula de Geografia mas minha mente tá na pizza que vou comer mais tarde.",
        "Viu o meme que te mandei no Insta? É literalmente você na aula de matemática.",
        "Pô, esqueci meu lanche em casa... Se eu desmaiar de fome, diz que eu amava meus amigos.",
        "Tô precisando de uma série nova pra assistir, a minha acabou e agora sinto um vazio existencial.",
        "Bora marcar de fazer nada qualquer dia desses? Sou mestre nisso."
    ]

    respostas_luisa = respostas_luisa = [
        "Oi! Estou organizando o material do próximo torneio, te ligo depois? 😊",
        "Theo, você esqueceu sua anotação no clube? Eu guardei aqui.",
        "Não posso falar agora, mas amanhã chegarei cedo no clube!",
        "Disciplina é o que separa os amadores dos mestres. Continue treinando.",
        "Estou preparando um simulado de táticas para o grupo. Esteja pronto.",
        "Vi uma partida sua no servidor online. Você precisa melhorar esse desenvolvimento de cavalos.",
        "Não esqueça de descansar. O cérebro precisa de oxigênio tanto quanto de teoria.",
        "A biblioteca do clube recebeu livros novos. Tem um sobre o Kasparov excelente."
        "A biblioteca está muito barulhenta hoje. As pessoas perderam o respeito pelo silêncio?",
        "A prova de História estava razoável, mas a questão 5 era pura pegadinha.",
        "Você viu que abriram uma cafeteria nova perto do clube? O chá de lá é aceitável.",
        "Estou terminando de ler um livro sobre psicologia comportamental. É fascinante.",
        "Theo, não esqueça que o prazo do trabalho de Sociologia termina amanhã.",
        "Muitas pessoas falam demais sobre a vida alheia e estudam de menos. É um fenômeno curioso.",
        "Hoje o céu está com uma luz ótima para fotografia. Você já reparou?"
    ]

init python:
    # Lista de Torneios do Ano
    lista_torneios = [
        ("Desafio da Luísa", 0, "boss_fight_luisa"), 
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

    # Listas dos Puzzles do Desafio da Luiza
    lista_puzzles_luisa = [
        ("puzzle001", "Qual golpe Tático temos aqui?", "Ataque Duplo", "Cravada"),
        ("puzzle002", "Qual xeque mais eficiente", "Cf6+", "Cg5+"),
        ("puzzle003", "Qual Peão eu devo avançar?", "Peão g", "Peão h"),
        ("puzzle004", "O tabuleiro está montado corretamente?", "Não", "Sim"),
        ("puzzle005", "Em quantos lances as pretas dão mate", "3", "2")
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
default pressao_psicologica = 0 # Nova mecânica: se chegar a 10, o Theo comete um erro grave



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

default round_atual = 1

# Mensagens 
default nova_msg_maya = False
default nova_msg_leo = False
default nova_msg_luisa = False

# Para garantir que eles não mandem a mesma mensagem várias vezes
default msg_luisa_derrotada_lida = False
default persistent.luisa_derrotada = False


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


# Tela da Boss Figth
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
    #jump boss_fight_luisa
    jump boss_fight_enzo

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
    $ theo_foco = 100
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
    # 1. Se for história (Bolinha Vermelha), aparece o personagem falando
    if persistent.luisa_derrotada and nova_msg_maya:
        show maya normal at maya_busto with dissolve
        m "Theo! Eu não acredito! A Luísa me contou que você venceu ela!"
        $ nova_msg_maya = False
    
    # 2. Se for o dia a dia, aparece a tela do celular
    else:
        $ msg_para_celular = random.choice(respostas_maya)
        # Passamos a variável 'msg_para_celular' que acabamos de criar
        call screen tela_chat("Maya", "mayaicone", msg_para_celular)
    
    jump abrir_hub

label conversa_leo:
    if persistent.luisa_derrotada and nova_msg_leo:
        show leo feliz at leo_busto with dissolve
        l "Cara, bater a Luísa no Desafio de Abertura? Você é monstro!"
        $ nova_msg_leo = False
    else:
        $ msg_para_celular = random.choice(respostas_leo)
        call screen tela_chat("Leo", "leoicone", msg_para_celular)
    
    jump abrir_hub

label conversa_luisa:
    if persistent.luisa_derrotada and nova_msg_luisa:
        show luisa normal at luisa_busto with dissolve
        lu "Analisei nossa partida. Você foi preciso no endgame."
        $ nova_msg_luisa = False
    else:
        $ msg_para_celular = random.choice(respostas_luisa)
        call screen tela_chat("Luísa", "luisaicone", msg_para_celular)
    
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
    "Vitória épica! Luísa reconhece seu talento. Rating +100."
   
    jump abrir_hub

label derrota_boss:
    hide screen status_boss_fight
    show luisa feliz
    lu "Ainda falta muito estudo. O tabuleiro não perdoa hesitação."
    "Você foi derrotado. Melhore seus status antes de tentar novamente!"
    # Opcional: recupera um pouco de vida para não dar game over total
    $ theo_hp = 20
    jump abrir_hub


# 2 Boss Figth Enzo o Tubarão


screen interface_combate():
    # Contêiner principal que centraliza tudo no topo
    vbox:
        xalign 0.5
        ypos 30
        spacing 20 # Espaço entre o bloco do Enzo e o bloco do Theo

        # --- BLOCO DO ENZO ---
        vbox:
            spacing 5
            text "Enzo - Persistência" size 20 color "#16ae34" xalign 0.5 outlines [(2, "#000", 0, 0)]
            bar value AnimatedValue(hp_enzo, enzo_max):
                xalign 0.5
                xsize 600
                ysize 25
                left_bar Solid("#1edf0d") # Verde para a vida do Boss
                right_bar Solid("#d6190f")

        # --- BLOCO DA PRESSÃO (THEO) ---
        vbox:
            spacing 5
            text "Sua Pressão Psicológica" size 18 color "#ff4444" xalign 0.5 outlines [(2, "#000", 0, 0)]
            bar value AnimatedValue(pressao_psicologica, 10):
                xalign 0.5
                xsize 500 # Um pouco menor para diferenciar da barra do Boss
                ysize 15
                left_bar Solid("#f10808") # Vermelho para sua tensão
                right_bar Solid("#febc07")

    # Painel de Atributos (Mantido no canto para não poluir o centro)
    # frame:
    #     background Solid("#00000088")
    #     padding (10, 10)
    #     xalign 0.98
    #     yalign 0.02
    #     vbox:
    #         spacing 2
    #         text "Foco: [theo_foco]" size 16 color "#3498db"
    #         text "Ousadia: [theo_ousadia]" size 16 color "#e67e22"
    #         text "Estabilidade: [theo_estabilidade]" size 16 color "#2ecc71"


label boss_fight_enzo:
    scene bg_clube_noite
    show enzo normal at left
    
    enz "Ouvi dizer que você é bom, Theo. Mas o xadrez de verdade acontece aqui. Torneio Escolar é coisa para bebê"
    enz "Vou esmagar sua confiança antes de levar seu Rei."
    enz "Eu não jogo Xadrez, eu caço meus adversários!!!"

    $ pressao_psicologica = 0
    $ hp_enzo = enzo_max



    show screen interface_combate






label loop_batalha_enzo:
    # Verificação de Condição de Vitória/Derrota
    if pressao_psicologica >= 10:
        jump derrota_por_tilt
    if hp_enzo <= 0:
        jump vitoria_sobre_enzo

    # HUD de Combate
    "ENZO HP: [hp_enzo] | SUA PRESSÃO: [pressao_psicologica]/10"

    menu:
        "O Enzo bate no relógio com força e te encara fixamente. Ele deixou uma peça exposta, parece uma armadilha."

        "Analisar com Foco (Requer Foco 15)":
            if theo_foco >= 15:
                $ hp_enzo -= 10
                "Você ignora o olhar dele e calcula as variantes. É uma armadilha, mas você encontra o contra-golpe."
                enz "Maldição... você não se distrai tão fácil, não é?"
            else:
                $ pressao_psicologica += 3
                "Você tenta focar, mas o barulho do clube e as provocações dele te fazem perder o fio do cálculo."

        "Responder com Ousadia (Requer Ousadia 15)":
            if theo_ousadia >= 15:
                $ hp_enzo -= 15
                $ pressao_psicologica += 2
                "Você aceita o sacrifício dele e dobra a aposta! O jogo vira um caos que favorece sua agressividade."
                enz "Você é louco? Isso não deveria funcionar!"
            else:
                $ hp_enzo -= 5
                $ pressao_psicologica += 5
                "Sua jogada ousada foi precipitada. Você ganha espaço, mas entra em pânico com a resposta dele."

        "Manter a Estabilidade (Requer Estabilidade 15)":
            if theo_estabilidade >= 15:
                $ hp_enzo -= 5
                $ pressao_psicologica -= 4
                "Você respira fundo e faz uma jogada sólida. O caos que ele tentou criar se dissipa."
                "Sua mente se acalma."
            else:
                $ pressao_psicologica += 2
                "Você tenta se acalmar, mas a postura rígida do seu pai vem à mente, te deixando ainda mais tenso."

        "Ignorar Provocação":
            $ pressao_psicologica -= 1
            "Você fecha os olhos por um segundo. Não é sobre ele, é sobre o tabuleiro."

    jump loop_batalha_enzo


    label vitoria_sobre_enzo:
    show enzo derrotado
    enz "Como... Como sua mente não quebrou? Eu usei tudo que eu tinha!"
    "Você se levanta. A pressão dele não foi nada comparada à que você enfrenta em casa."
    $ persistent.boss_2_concluido = True
    jump pos_luta_dialogo

label derrota_por_tilt:
    scene black with vpunch
    "Sua visão escurece. O som do relógio parece uma bomba na sua cabeça."
    "Theo não consegue mais distinguir as peças. O trauma do julgamento do pai se mistura com a pressão do Enzo."
    enz "Acabou, garoto. Você não tem estômago para esse nível."
    jump abrir_hub


label pos_luta_dialogo:
    enz "Eu não acredito... Minha estratégia era infalível."
    t "No xadrez, Enzo, a mente é tão importante quanto as peças."
    "Você recolhe suas coisas enquanto Enzo fica encarando o tabuleiro vazio."
    
    # Depois daqui, você pode mandar o jogador de volta para o hub
    jump abrir_hub