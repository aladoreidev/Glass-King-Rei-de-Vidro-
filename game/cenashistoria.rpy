
label cena_derrota_clube:
    scene clubexadrez with fade

    # --- ENTRADA SUAVE (MOVIMENTO) ---
    show macedolado:
        xalign -0.5 yalign 0.35 zoom 0.7
        easein 1.5 xalign 0.05
    
    show theolado:
        xalign 1.5 yalign 0.20 zoom 0.6
        easein 1.5 xalign 0.5

    "Clube de Xadrez Ala do Rei"
    "Março de 2015"

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
    
    # --- EFEITO RÍTMICO DO ANEL ---
    "Começa a bater repetidamente o anel de metal na mesa... "
    "{b}TOC...{/b}" with vpunch
    pause 0.2
    "{b}TOC...{/b}" with vpunch
    pause 0.2
    "{b}TOC!{/b}" with vpunch

    "Theo, tenta ignorar...mas está cada vez mais difícil..."
    "O Árbitro adverte o velho Macedo..."
    "O ar parecia parado, denso como chumbo. Theo estava a um passo de consolidar sua vantagem... Mas, então, veio o golpe final. Não partiu do tabuleiro, mas do destino."
    "No fundo do salão, uma xícara de café escorregou de uma mesa. O tempo pareceu desacelerar enquanto a porcelana viajava em direção ao chão."

    # --- O IMPACTO DA XÍCARA ---
    stop music fadeout 0.5
    play sound "audio/glasscrash2.ogg"
    
    # Brilho de susto e tremor horizontal
    show white onlayer master:
        alpha 0.6
        linear 0.2 alpha 0.0
    with hpunch
    
    # Theo perde a cor (Choque Psicológico)
    show theolado:
        matrixcolor SaturationMatrix(0.0)
    with Dissolve(0.2)

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

    # --- STATUS ---
    $ theo_rating -= 30
    $ theo_foco -= 20
    $ theo_estabilidade -= 10
    $ theo_ousadia += 5

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

    # Reset da cor do Theo para a próxima cena
    show theolado:
        matrixcolor SaturationMatrix(1.0)
    with dissolve

    "A noite cai sobre a cidade, e o silêncio agora é o único companheiro de Theo."
    jump encontro_amigos_pos_derrota

# Cena do lado de fora do Clube
label encontro_amigos_pos_derrota:
    scene ruanoite with fade

    # Theo no centro com o novo padrão
    show theo triste at modo_full:
        xalign 0.5
    with moveinleft

    "O ar gelado da noite ajuda a baixar a adrenalina, mas o silêncio é logo interrompido por passos rápidos."

    # Léo aparece na esquerda
    show leo normal at modo_full:
        xalign 0.1
    with moveinleft  
    
    l "Theo! Cara, o que foi aquilo?..." 
    
    show theo normal at modo_full:
        xalign 0.5 
    t "Cara, eu não sei explicar... Estava ganho, mas de repente..."

    l "Mano, relaxa... aquele velho idiota só consegue vencer se for daquele jeito"

    t "Mas Leo, eu não podia ter caído na pilha dele..."

    l "Theo, pelo menos aquele velhote teve um motivo para sorrir..."

    l "Acho que a última vez que ele ficou feliz daquele jeito, Fischer ainda era juvenil..."
      
    # Luísa aparece na direita, mas o xalign 0.7 garante que ela não "atropele" o Theo
    # O 'behind theo' garante que, se eles se tocarem, ela fique atrás do braço dele
    show luisa normal at modo_full:
        xalign 0.95
    with moveinright
       
    lu "Não vejo graça nisso, Léo. Xadrez é autocontrole..."
    
    show theo triste at modo_full 
    lu "Fala sério Theo, aquele lance do Cavalo para c5 foi muito esquisito..."
    lu "Tudo bem que depois você ficou melhor, mas..."
    
    lu "Se você quer chegar ao Nacional..."

    # Maya aparece entre o Theo e a Luisa
    show maya normal at modo_full: 
        xalign 0.7 yalign 0.98
    with moveinright
    
    ma "Menos, Luisa. Ninguém precisa de uma autópsia da partida..."

    show theo normal at modo_full
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
            ma "Não seja tão duro com você mesmo Theo..."

        "Fazer uma piada junto com Léo":
            $ afeto_leo += 15
            $ theo_ousadia += 5
            t "É, Léo... acho que o relógio vai precisar de terapia depois de hoje."
            l "Hahaha! Boa! Vamos comer uma pizza, eu pago. O Rating a gente recupera, mas a minha fome é urgente!"

    "O clima entre o grupo começa a suavizar conforme vocês se afastam do clube."

    show leo feliz at modo_full:
        xalign 0.1
    l "Pô galerinha, a minha barriga tá roncando mais alto que o relógio do Macedo! O que vocês acham da gente colar lá na 'CheckMate Burguer'?"
    l "Dizem que o 'X-Bispo' de lá é imbatível, quase um xeque-mate no estômago!"

    # Adicionado o transform e posição para o Theo
    show theo normal at modo_full:
        xalign 0.5
    # Léo na esquerda
    show leo feliz at modo_full:
        xalign 0.1
    l "Pô galerinha, a minha barriga tá roncando mais alto que o relógio do Macedo! O que vocês acham da gente colar lá na 'CheckMate Burguer'?"
    l "Dizem que o 'X-Bispo' de lá é imbatível, quase um xeque-mate no estômago!"

    # Theo um pouco para a esquerda do centro
    show theo normal at modo_full:
        xalign 0.5
    t "Sabe de uma coisa? Eu topo. Acho que se eu ficar sozinho em casa agora, vou acabar jogando meu tabuleiro pela janela."

    # Luísa na direita. Removi o ":" para evitar o erro de bloco vazio
    show luisa raiva at modo_full behind theo:
        xalign 0.95
    with moveinright
    
    lu "Como é que é? Theo, você acabou de sofrer uma derrota técnica por falta de foco e sua solução é... comer um hambúrguer?"
    lu "Você deveria ir direto para o computador revisar. Cada minuto que você passa mastigando é um minuto a menos revisando onde sua estrutura de peões colapsou."

    # Maya no centro-direita
    show maya feliz at modo_full:
        xalign 0.7
    ma "Relaxa, Luisa. O cérebro dele ferveu lá dentro. Se ele tentar analisar algo agora, vai acabar confundindo o Rei com um pão de batata."

    show maya normal at modo_full:
        xalign 0.7
    ma "Eu apoio o Léo. Por incrível que pareça, ele teve uma ideia decente hoje. Vamos, Theo. A primeira rodada de fritas é por minha conta, pra compensar seu Rating perdido."

    show leo normal at modo_full:
        xalign 0.1
    l "Aê! Viu só? Até a Maya reconheceu minha genialidade oculta. Vamos logo antes que a Luisa comece a dar aula de abertura no meio da calçada!"

    # --- CORREÇÃO DOS ERROS DE INDENTAÇÃO ---
    # Aqui, cada 'show' tem seu próprio bloco de posição
    
    show leo feliz at modo_full:
        xalign 0.1

    
    show theo feliz at modo_full:
        xalign 0.4
        
    show maya feliz at modo_full:
        xalign 0.6
    
    "Theo, Leo e Maya sorriem um para o outro, prontos para o hambúrguer."


    # Transição para a lanchonete
    hide leo
    hide theo
    hide luisa
    hide maya
    with fade
    
    # Cena da Lanchonete Checkmate Burguer
    
    scene checkmateburger with fade
    
    "A lanchonete está movimentada. O cheiro de hambúrguer grelhado e o som de relógios de xadrez batendo nas mesas ao fundo criam um ambiente acolhedor."

    show leo normal at modo_busto:
        xalign 0
    show theo normal at modo_busto:
        xalign 0.29
    show luisa normal at modo_busto:
        xalign 0.9999
    show maya normal at modo_busto:
        xalign 0.65
    with dissolve

    l "Finalmente! Se eu demorasse mais cinco minutos, eu ia começar a comer as peças do meu tabuleiro."
    lu "Nossa Leo, que engraçado... To me acabando de rir aqui..."
    ma "Nossa. Lu, você hoje está de mau humor..."
    t "O lugar está cheio hoje. Pelo menos aqui ninguém parece se importar se alguém 'pendura' uma dama."
    show luisa feliz
    lu "Na verdade, Theo, a mesa 4 ali atrás está jogando uma Variante Tartakower bem interessante. Eu deveria ir lá dar uma olhada..."

    ma "Nada disso, Luisa! Hoje é noite de descompressão. Senta aí."

    show luisa triste
    

    show leo feliz
    l "Ei, Theo! Para de olhar para o cardápio e olha para isso aqui. Vi um carinha postar no fórum hoje cedo."
    "Léo rabisca rapidamente um diagrama de xadrez em um guardanapo engordurado e empurra para o centro da mesa."

    show leo normal


    l "Ele disse que é 'Mate em 2', mas eu acho que ele fumou meia. O que você acha? Se acertar, eu pago o seu refrigerante!"

    hide luisa
    hide maya


    call screen puzzle_guardanapo_circles

# --- DESAFIO PUZZLE: Do Guardanapo ---

label mate_correto:
    show luisa normal at modo_busto:
        xalign 0.99
    show maya feliz at modo_busto:
        xalign 0.65
    show theo feliz
    $ theo_rating += 25
    $ theo_foco += 5
    t "Xeque com o sacrifício de Dama em f7! Mate imparável!"
    jump segue_conversa_pizzaria

label erro_bispo:
    show luisa raiva at modo_busto:
        xalign 0.99
    show maya triste at modo_busto:
        xalign 0.65
    show leo triste
    show theo triste
    t "Bispo em f7...?"
    lu "Errado. O Rei foge para h8."
    $ theo_rating -= 25
    $ theo_foco -= 5
    $ theo_ousadia -= 5
    jump segue_conversa_pizzaria

label erro_torre:
    show luisa raiva at modo_busto:
        xalign 0.99
    show maya triste at modo_busto:
        xalign 0.65
    show leo triste
    show theo triste 
    t "Torre em f8...?"
    lu "Tá Maluco, Theo. Você perde a Dama."
    $ theo_rating -= 25
    $ theo_estabilidade -= 5
    $ theo_ousadia -= 5
    jump segue_conversa_pizzaria

label segue_conversa_pizzaria:
    "Após o desafio, os vossos hambúrgueres finalmente chegam à mesa."
    "A noite termina com risadas, mas você sabe que amanhã o treino volta a ser sério."
    jump cena_jantar_pais


label cena_jantar_pais:
    scene salajantar with fade
    
    "O tilintar dos talheres na porcelana era o único som na sala. No xadrez, o silêncio é foco. Aqui, é julgamento."
    "Meu pai limpou o canto da boca com o guardanapo de linho. Ele ainda nem tinha olhado para mim."
    # Pai bem para a esquerda (valor negativo para compensar o zoom)
    show dr_henrique normal at modo_busto:
        xalign -0.2  # Empurra ele mais para a borda esquerda
    
    # Mãe bem para a direita (valor acima de 1.0)
    show dra_karolina normal at modo_busto:
        xalign 1.2   # Empurra ela mais para a borda direita

    # Theo no meio dos dois (ligeiramente ajustado)
    show theo triste at modo_busto:
        xalign 0.5   # Centro absoluto
    ph "Fiquei sabendo que o torneio no clube não correu como o esperado hoje, Theodoro. O Dr. Arnaldo mencionou que você... 'se atrapalhou'?"

    t "Foi um incidente técnico, pai. Eu estava com uma vantagem decisiva contra o Macedo."

    

    ph "Vantagem não ganha causas, nem partidas. No Direito, se você deixa uma prova escapar porque 'se atrapalhou', o cliente vai preso."
    ph "Um futuro jurista precisa de mais... Estabilidade." # Aspas fechadas aqui

    show theo raiva


    show dra_karolina feliz
    mae "Henrique, deixe o menino respirar. Querido, você não comeu quase nada ."
    mae "Theo querido... sua mão está tremendo um pouco? Você deve estar stressado. Talvez o xadrez esteja drenando o Foco que você deveria dedicar aos Estudos."


    show dra_karolina normal

    menu:
        "Tentar explicar o incidente da xícara.":
            $ theo_estabilidade -= 5
            $ theo_ousadia += 10
            $ theo_foco -= 5
            t "O ambiente estava um caos! Alguém quebrou uma xícara atrás de mim. O barulho me pegou de surpresa!"
            ph "Theodoro, para ser um homem bem sucedido você não pode se dar ao luxo de ser refém do ambiente."
            ph "O mundo é barulhento, Theo. Tribunais são barulhentos. Hospitais são caóticos."
            ph "Se uma xícara de porcelana é o suficiente para desestabilizar sua mão, então você ainda não passa de um amador brincando com bonecos de madeira."
            
            mae "Henrique, não seja tão duro... Mas ele tem um ponto, Theo. O autocontrole é a sua maior ferramenta"
            mae "Imagine, se durante uma cirurgia eu me desesperasse porque um enfermeiro deixou um instrumento cair, ou porque o monitor começou a apitar fora de hora?"
            mae "Vidas dependem da minha mão estar firme, não importa o barulho ao redor. Você precisa aprender que o seu foco deve ser uma fortaleza, Theo."
            
            ph "Exatamente. Agora, termine seu jantar. O silêncio é a melhor companhia para quem tem muito o que refletir."

        "Aceitar a crítica em silêncio.":
            $ theo_estabilidade += 15
            $ theo_ousadia -= 5
            "Aperto o garfo com tanta força que meus dedos ficam brancos. Engulo o orgulho junto com a comida insossa."
            t "Sim, senhor. Foi um erro grosseiro. Vou garantir que minha concentração seja impenetrável na próxima."
            
            ph "Bom. Disciplina é a única coisa que separa um Desembargador de um rábula. O rábula é barulhento, vive de desculpas e de 'quases'."
            ph "Um homem da sua linhagem não 'se atrapalha'. Ele domina. Se o ambiente o afetou, é porque você permitiu que o ambiente fosse maior que a sua vontade."
            
            mae "Veja pelo lado positivo, Henrique. Se ele reconhece a falha, pode focar em não repeti-la."
            mae "O erro no xadrez é um luxo que você pode cometer agora, Theo. Mas na mesa de cirurgia, o primeiro erro é o último."
            
            t "Eu entendo... Só preciso de tempo para treinar mais."
            
            ph "Tempo é o recurso mais caro que temos. Não o desperdice com partidas medíocres contra jogadores de clube."
            ph "Se quer ser um rei, comporte-se como um. Reis não dão desculpas para a coroa cair."

    mae "Sabe, filho, o vestibular está chegando. Não queremos que você pare de jogar, mas..."
    
    mae "Precisamos ser realistas. O xadrez é um jogo lindo para exercitar a mente, mas ele não sustenta uma casa, não paga as contas e, certamente, não impõe o respeito que o sobrenome da nossa família carrega."
    
    mae "Seu pai construiu um legado no Direito. Ele abriu um caminho de ouro para você seguir. Imagine o desperdício de trocar uma carreira sólida no Judiciário por... por tabuleiros de madeira e torneios em clubes empoeirados?"
    
    t "Mãe, não é só um jogo. Eu estou entre os melhores da minha categoria..."
    
    mae "Ser o melhor em um hobby ainda é ser um hobbista, Theo. O mundo não precisa de mais um 'Rei de Vidro' em um tabuleiro. O mundo precisa de homens como o seu pai, que decidem o destino das pessoas."
    
    ph "Escute sua mãe. O xadrez pode ser o seu lazer, mas o Direito será a sua armadura. Agora, vá para o seu quarto. Reflita sobre o que é ser um homem de verdade."

    t "Eu sei, mãe. Eu estou equilibrando as coisas."

    "A pressão deles é como uma prensa hidráulica."

    hide dr_henrique
    hide mae_medica
    with dissolve

    window hide
    jump pos_jantar_quarto 


label pos_jantar_quarto:
    scene quartonoite with fade
    play sound "audio/door_lock.ogg" # Som de porta trancando
    
    "O clique da fechadura é o único som que me traz paz. Trancar a porta não é apenas por privacidade... é para manter o mundo deles lá fora."
    
    show theo raiva at modo_busto:
        xalign 0.5
    
    "Sento-me na beira da cama. O silêncio do meu quarto ainda ecoa as palavras dos meus pais sobre Carreira, foco, estabilidade"
    
    t "(Pensamento) 'Linhagem'... 'Legado'... Eles falam como se eu fosse apenas uma peça no tabuleiro deles. Um peão que deve avançar até a última casa para se tornar o que eles querem."

    # Aqui os atributos moldam a reflexão do Theo
    if theo_estabilidade > 60:
        "Respiro fundo. O peso no meu peito é grande, mas minha mente está firme. Eu não vou quebrar. Se eles querem um mestre, eu vou dar um mestre a eles... mas no meu tabuleiro."
    elif theo_ousadia > 60:
        "Sinto uma queimação no estômago. A vontade é de abrir a porta e dizer que o xadrez é a única coisa que me faz sentir vivo. Mas ainda não é a hora. Eu preciso de resultados."
    else:
        "A dúvida rasteja pela minha mente. E se eles estiverem certos? E se eu for apenas um amador insistindo em um sonho frágil?"

    menu:
        "Ligar o computador e estudar a partida contra o Macedo. (Foco +10)":
            $ theo_foco += 10
            "Não posso mudar o jantar, mas posso mudar o próximo lance. Abro o banco de dados. O erro do Bispo não vai se repetir."
            
        "Deitar e encarar o teto, tentando silenciar as vozes. (Estabilidade +10)":
            $ theo_estabilidade += 10
            "Fecho os olhos. Ignoro a medicina, ignoro o direito. Tento encontrar o centro. Onde o barulho das xícaras não alcança."
            
        "Mandar mensagem para os amigos para desabafar. (Ousadia +5, Estabilidade +5)":
            $ theo_ousadia += 5
            $ theo_estabilidade += 5
            "Pego o celular. Preciso de gente que fale a minha língua. Gente que não me veja como um diploma ambulante."

    "O brilho do monitor é o meu farol. É aqui que o Theo morre e o enxadrista nasce."
    "Os olhos de Theo começam e se fechar e sua mente é tomada por uma lembrança de sua infância..."

    hide theo_reflexivo with dissolve
    window hide
    
    
    jump flashback_infancia


#Flashback infância

label flashback_infancia:
    scene escritotiodrhenrique with fade 
    play music "audio/tension_piano.mp3" fadein 2.0

    "Dez anos atrás..."

    "O escritório cheirava a couro e papel antigo. O único som era o do relógio de parede, rítmico e implacável."
    
    "Eu tinha apenas oito anos. Estava escondido atrás da poltrona, tentando resolver um problema de mate em dois num tabuleiro de bolso."
    
    # CORRIGIDO: Removido o 's' extra de 'sshow' e adicionado ':'
    show dr_henrique normal at modo_busto:
        xalign -0.2

    ph "Theodoro? O que eu disse sobre esses... brinquedos no meu escritório?" 

    "Tentei fechar o tabuleiro rapidamente, mas as peças de plástico fizeram um barulho seco no chão de madeira."

    show theocriancafeliz:
        zoom 1.5
        xalign 0.9
        yalign 0.4

    t "Eu... eu já terminei o dever de latim, pai. Só estava praticando um pouco."

    ph "Praticando? Pratica-se piano, pratica-se retórica, pratica-se o Direito."
    ph "Isso que você segura é um passatempo para quem não tem um legado a carregar."

    "Ele caminhou até mim. Cada passo parecia uma sentença judicial."

    show dr_henrique raiva at modo_busto:
        xalign -0.2

    ph "A vida não é um tabuleiro com regras claras e turnos alternados, meu filho."
    ph "A vida é uma disputa de influência. Enquanto você move cavalos de plástico, os seus concorrentes estão movendo o mundo real."

    "Ele pegou o tabuleiro da minha mão. Não com raiva, mas com uma frieza que doía muito mais."

    hide theocriancafeliz
    show theocriancatriste:
        zoom 1.5
        xalign 0.9  # Corrigido: Estava 0.99, o que jogava ele para fora da tela
        yalign 0.4

    # CORRIGIDO: Adicionado ':' e corrigida a indentação do xalign abaixo
    show dr_henrique normal at modo_busto:
        xalign -0.2
        
    ph "Vou guardar isso. Quando você for um Procurador, terá tempo para jogos de tabuleiro. Até lá, foque no que importa."

    stop music fadeout 3.0
    scene black with dissolve
    
    "Aquelas palavras ficaram gravadas. Cada vez que toco em uma peça, sinto o peso do olhar dele sobre meus ombros."

    $ theo_estabilidade -= 30

    jump cena_escola_rival

label cena_escola_rival:
    scene escolamanha with fade
    play music "audio/school_ambience.ogg" fadein 1.0

    "Instituto Magnum. Onde os futuros líderes do país são forjados entre aulas de latim e cálculo avançado."
    
    "Acima do mural de carvalho, a placa de ouro polido exibe o lema que justifica cada humilhação sofrida nos corredores:"
    
    show muralmagnus at truecenter with dissolve
    
    "{i}'OPTMI SUPRA RELIQUOS'{/i}"
    
    "Os melhores acima dos demais." 
    "No Magnum, a mediocridade não é apenas uma falha; é um pecado social. E depois do que aconteceu no clube, eu sinto o olhar de todos me empurrando para baixo da linha."

    # ... código do mural anterior ...
    hide muralmagnus
    # Léo bem para a esquerda (fora do limite 0.0)
    show leo normal at modo_busto:
        xalign -0.25
        
    # Luísa centralizada (como ponto de referência)
    show luisa normal at modo_busto:
        xalign 0.5
        
    # Theo bem para a direita (além do limite 1.0)
    show theo normal at modo_busto:
        xalign 1.25

    # Aplica a transição de subida
    with easeinbottom

    l "Cara, esse lema do Magnum me dá arrepios. 'Os melhores acima dos demais'... parece frase de vilão de RPG."
    
    lu "É a realidade, Léo. Ou você é o martelo, ou é o prego."
    
    l "O 'Magnum Chess Masters'(Jogos Internos) deste ano vai ser no ginásio central, Theo. Ouvi dizer que um Árbitro Internacional vai arbitrar."
    
    lu "E parece que o prêmio para o primeiro lugar é uma bolsa integral para o intercâmbio de verão. Seus pais iam adorar isso, hein?"

    t "Eles iam adorar o intercâmbio... mas só se eu passasse o verão estudando Jurisprudência em Harvard."

    # Entrada do Rival
    play sound "audio/steps_shoes.ogg" # Som de sapatos sociais caros
    "O ritmo dos passos no corredor muda. É uma cadência precisa, de quem não tem pressa porque sabe que o espaço o pertence."
    
    "Enzo se aproxima. Ele não precisa de uniforme personalizado ou de um séquito; sua postura e o relógio de pulso que vale mais que o carro da maioria dos professores dizem tudo o que ele quer que saibamos."

    # Usando tudo na mesma linha para evitar erros de indentação
    show enzo normal at modo_busto:
        xalign 0.8
    
    show leo raiva at modo_busto:
        xalign -0.25
        
    show luisa triste at modo_busto:
        xalign 0.5
        
    show theo raiva at modo_busto:
        xalign 1.25

    with dissolve


    enz "Hum... Harvard... ouvi dizer que o 'Rei de Vidro' teve um colapso nervoso no clube por causa de uma xícara de café. Procede, Theo?"

    enz "Eu ia te oferecer um expresso agora, mas fiquei com medo de você derrubar o tabuleiro se a colher bater na borda da xícara."

   

    # Saída suave da Luísa e do Leo (primeira aparição)
    hide luisa
    hide leo
    with dissolve

    # Theo se move suavemente para a esquerda antes do menu
    show theo raiva at modo_busto:
        ease 0.5 xalign 0.0  # Removi o '5' que estava aqui

    
    show enzo esnobe at modo_busto: 
        xalign 0.8

    menu (menu_y=0.8):
        "Manter a elegância e não cair na pilha.":
            $ theo_estabilidade += 10
            t "A notícia corre rápido, Enzo. Mas não se preocupe, estarei preparado se por ventura nos encontrarmos na final"
            enz "Nossa, podemos marcar um CAFÉ qualquer dia desses, ops, esqueci, vai que uma xícara caia não é?"

        "Devolver a provocação à altura.":
            $ theo_ousadia += 10
            $ theo_foco -= 5
            t "Engraçado você falar de xadrez de elite, quando todo mundo sabe que você só é titular da equipe porque seu pai doou o novo laboratório de química."
            "Os olhos de Enzo brilham com uma raiva contida. Acertei no ponto fraco."
            enz "Cuidado, Theo. Vidro trinca fácil quando a pressão aumenta. E eu vou garantir que o Magnum inteiro veja você se estraçalhar no ginásio."

    # --- TRANSIÇÃO SUAVE ---
    
    # Saída suave do Theo deslizando para a esquerda
    hide theo with easeoutleft 

    # Entrada suave do Leo com as configurações que definimos
    show leo raiva at modo_busto:
        xpos 0.1
        zoom 1.1
        yoffset 50
    with easeinleft 

    l "Theo, não perde tempo com esse lixo! Enzo, você acha que o dinheiro do seu pai conserta seu caráter?"
    
    enz "Olha o bolsista tentando latir. Por que você não vai engraxar meus sapatos, Leo? Pelo menos assim você seria útil."

         
    enz "O Magnum Chess Masters... um nome que exige perfeição e elegância. Algo que parece estar em falta no seu jogo ultimamente, não é, Theo?"

    # Leo (o amigo) intervém
    l "Corta essa, seu babaca. Todo mundo sabe que o Theo em um dia ruim ainda joga o dobro que você. Deixa o cara em paz."

    # enz vira o alvo para o Leo
    enz "Ah, o fiel escudeiro resolveu se manifestar? É fascinante a coragem que a gratuidade escolar dá para certas pessoas."
    
    enz "Diga-me, Leo, sua mãe — a nossa estimada professora de {b}Filosofia{/b} — sabe que você gasta seu tempo de 'cota social' defendendo causas perdidas?"
    
    enz "Ou ela está ocupada demais tentando convencer o conselho de que o filho da funcionária merece uma vaga que deveria ser de um aluno pagante?"

    # Escurece as bordas da tela para focar no conflito
    show layer master:
        matrixcolor TintMatrix("#ccc") * SaturationMatrix(0.9)
    with dissolve

    l "O cargo da minha mãe e a minha bolsa não são da sua conta, seu esnobe de merda!"
    l "Eu posso até não ter as melhores notas, mas pelo menos eu não sou um projeto de ditador que precisa de um relógio de ouro e do sobrenome do papai pra se sentir alguém!"

    "Leo perde o controle e avança."
    play sound "audio/grab.ogg" # Som de pano sendo puxado
    with hpunch # Treme a tela horizontalmente
    "Leo agarra Enzo pelo colarinho com uma força que faz o herdeiro perder o equilíbrio por um segundo."

    show enzo raiva at modo_busto:
        xalign 0.75
        yalign 1.1
        


    # Leo se aproxima ou aponta o dedo, e enz reage com nojo
    enz "Me larga, seu... seu projeto de marginal!"

    enz "Não encoste em mim com essas mãos de quem limpa os banheiros da escola depois da aula. Você não tem o direito de respirar o mesmo ar que eu, quanto mais de gritar comigo."


    

    l "Direito? Eu vou te mostrar o meu direito se você falar da minha mãe ou da minha bolsa de novo!"

    # O clima pesa. Luísa tenta intervir.
    show luisa raiva at modo_busto:
        xalign 1.1  # Valor seguro para aparecer na direita sem sumir
        yalign 1.0
    with easeinright



    lu "Leo, para! Não vale a pena. É isso que ele quer, que você perca a bolsa por agressão!"

    # O clima pesa. Vico tenta intervir.
    lu "Leo, para! Não vale a pena. É isso que ele quer, que você perca a bolsa por agressão!"
  

    enz "Ouça a garota, bolsista. Ela é mais inteligente que você. Um toque em mim e você está fora do Magnum antes de conseguir soletrar 'Filosofia'."

    # enz se vira para Theo, ignorando Leo como se ele fosse lixo
    enz "E você, Theo? Vai ficar aí parado assistindo seu cão de guarda latir, ou vai admitir que ele é a única coisa que sobrou do seu prestígio?"


    
    hide luisa

    # O Theo se move e cresce ANTES do jogador escolher, 
    # criando o clima de "hora da decisão".
    show theo raiva at modo_busto:
        ease 0.5 xpos 0.5 zoom 1.3 yoffset 200

    show enzo raiva at modo_busto:
        xalign 0.7

    menu:
        "Ficar entre os dois e encerrar a briga.":
            $ theo_estabilidade += 15
            t "Acabou, Enzo. Some daqui antes que eu decida que a minha reputação vale menos que o prazer de te ver no chão."
            t "A gente se vê no Magnum Chess Masters. Tente não engasgar com o próprio ego até lá."
            
            # Enzo reage antes de sair
            show enzo raiva at modo_busto:
                xalign 0.7
            enz "O vidro está trincando, Theo... eu consigo ouvir daqui."

        "Explodir com Enzo.":
            $ theo_ousadia += 20
            $ theo_foco -= 10
            # Efeito de Flash para a explosão de raiva
            show white onlayer overlay:
                alpha 0.6
                linear 0.2 alpha 0.0
                
            t "O único 'marginal' aqui é você, que precisa diminuir os outros pra se sentir grande!"
            t "O Leo vale dez de você, e no torneio, eu vou te enterrar tão fundo que nem o dinheiro do seu pai vai te achar."
            enz "Que dramático. Guarde esse fôlego para quando você estiver perdendo por tempo no ginásio."
    hide luisa
    # Agora mostramos ela do zero com uma posição fixa
    show luisa raiva at modo_busto:
        xalign 0.4 
    with dissolve
    

    show enzo arrogante

    hide enzo with moveoutright
    play sound "audio/steps_fast.ogg"

    "Enzo se retira, ajeitando o blazer como se tivesse sido contaminado por estar perto de nós."

    l "Desculpa, Theo... eu perdi a cabeça. É que esse desgraçado sabe onde dói."

    t "Ele é um covarde, Leo. Ele ataca quem ele não consegue vencer no tabuleiro."

    show luisa raiva at modo_busto:
        xalign 0.7
        
    with easeinleft # Alinhado na mesma coluna do 'show'
        
    

    lu "Minha nossa, esse Enzo é horrível! Ele se acha só porque o pai dele é o dono da {b}Logos S.A.{/b}."
    
    lu "Metade dos laboratórios novos do Magnum foram 'doação' da empresa dele. O Enzo age como se fosse o dono do colégio porque, tecnicamente, o pai dele é o dono das paredes onde a gente estuda."

    
    l "E ele sabe que a diretoria nunca ganharia uma queda de braço com um acionista desse nível. Por isso ele pisa em quem quer."

    t "Ele pode ser dono das paredes, mas o tabuleiro não tem dono. No Magnum Chess Masters, o dinheiro da Logos não move as peças por ele."

    l "Espero que você esteja certo, Theo... Porque se eu perder minha bolsa, minha mãe me mataria. O Magnum não admite erros."

    "O peso da responsabilidade esmaga o que sobrou da minha tranquilidade. Olho para o cartaz do torneio uma última vez."
    
    "{i}Optmi Supra Reliquos.{/i}"
    
    "Eu preciso ser o melhor. Não só por mim, mas para que o vidro não quebre e leve meus amigos junto."

    window hide
    stop music fadeout 3.0
    
    # Tela fica preta e o lema aparece no centro
    scene black with Dissolve(2.0)
    pause 1.0
    show text "{i}{size=60}Optmi Supra Reliquos.{/size}{/i}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    
    $ hist_magnum = True

    # Remove os efeitos de cor que aplicamos antes
    show layer master:
        matrixcolor IdentityMatrix()
        
    jump abrir_hub
    window hide
    with dissolve
    
    stop music fadeout 2.0
    jump abrir_hub




label abrir_hub:
    # 1. Limpa qualquer resquício de personagens ou telas anteriores
    $ renpy.free_memory() 
    
    # 2. Transição de entrada: 'with fade' faz o efeito de fechar/abrir os olhos
    scene singlebedroom with fade 
    
    # 3. Chama a tela do quarto
    call screen hub_principal

    
label cena_pos_vitoria_enzo:
    scene bibliotecajogo with hpunch
    
    
    show theo feliz at left
    show leo feliz at center
    show maya feliz at left
    show luisa feliz
    with dissolve

    l "EU SABIA! Theo, você não jogou xadrez, você deu uma aula de etiqueta! O Enzo saiu tão humilhado que eu achei que ele ia pedir desculpas por existir!"
    
    lu "Menos, Leo. O Theo cometeu uma imprecisão grave na abertura. Se o Enzo não fosse tão arrogante, teria punido o cavalo em C6."

    ma "ISSO! Theo, você foi impecável!"
    l "Ah, Luísa, deixa disso! Ele venceu o cara mais pé no saco da escola. Hoje é dia de comemorar, não de revisar planilha!"
    
    # 2. A CHEGADA DO ENZO (Clima pesado)
    show enzo raiva at pos_luisa with easeinright
    
    enz "Riam enquanto podem. Aproveitem esse 'golpe de sorte' para se sentirem importantes por cinco minutos."

    show leo feliz
    l "Sorte? Enzo, sua cara de quem engoliu um limão mofado diz que foi puro talento. Quer um lenço?"

    # 3. A TRETA E A AMEAÇA
    show enzo raiva:
        xalign 0.7 zoom 2.2
    with EaseIn(0.5)

    enz "Você fala demais para alguém que depende da caridade da diretoria, Leo. Onde você vai fazer suas piadinhas quando sua bolsa for cancelada semana que vem?"
    
    show leo triste
    le "O-o quê? Você tá louco? Eu vou arrebentar sua cara!"

    enz "Se você encostar suas mãos imundas em mim, será seu fim."

    with hpunch
    "Leo avança um passo, fechando os punhos. Maya tenta segurá-lo, sem sucesso."

    # Efeito sonoro de soco (se você tiver) e tremor de tela
    play sound "audio/soco.mp3"
    with vpunch
    "{b}PUNCH!{/b} Leo acerta um soco em cheio no nariz de Enzo!"

    show enzo choque at right:
        xoffset 20
    "O impacto joga a cabeça de Enzo para trás. O sangue começa a escorrer instantaneamente."

    "Os dois garotos que estavam com Enzo entram na confusão, avançando contra Leo!"

    # --- MENU DE DECISÃO DO THEO ---
    menu:
        "O que você vai fazer?"

        "Entrar na briga para defender o Leo":
            $ theo_ousadia += 15
            $ theo_estabilidade -= 10
            "Você não pensa duas vezes. Se o Leo vai cair, você cai com ele!"
            show theo raiva at center with easeinleft
            "Você se joga na frente de um dos amigos de Enzo, empurrando-o com força."
            t "Tira a mão dele! Se quiserem bater em alguém, batam em mim!"
            "O Ginásio vira um caos de empurrões e gritos."

        "Tentar separar a briga e apaziguar":
            $ theo_foco += 10
            $ theo_estabilidade += 5
            "Você corre para o meio do conflito, tentando criar uma barreira entre eles."
            t "PAROU! Leo, solta ele! Enzo, recua agora!"
            show maya triste
            ma "Theo, me ajuda! Eles vão se matar!"
            "Você segura Leo pelo ombro, tentando forçá-lo a olhar para você e recuperar a razão."
            lu "Leo, cuidado!!!"

        "Ficar paralisado pelo choque (Instabilidade)":
            $ theo_estabilidade -= 20
            $ theo_foco -= 10
            "Seu coração dispara. O som do soco ecoa na sua mente e você simplesmente trava."
            "As vozes ao redor parecem abafadas. Você vê a bolsa do Leo e o futuro de vocês escorrendo junto com o sangue no chão."
            ma "THEO! NÃO FICA AÍ PARADO! FAZ ALGUMA COISA!"
            lu "THEO! VOCÊ PRECISA AJUDÁ-LO"

    # --- A CHEGADA DOS INSPETORES ---
    "O som de um apito estridente corta o barulho da briga."

    show inspetor_npc at center with moveintop
    
    ins "{b}PAREM AGORA!{/b}"
    
    ins "Theo, Leo, Enzo e os demais... PARA A DIRETORIA! AGORA!"

    show enzo raiva:
        xalign 0.7 zoom 2.2
    enz "Ele me agrediu! Vocês viram! Eu vou processar esse animal e garantir que ele nunca mais pise em uma escola!"

    show leo triste
    "Leo olha para as próprias mãos, tremendo. A ficha do que ele acabou de fazer começa a cair."

    $ acoes_hoje += 1


    jump abrir_hub

  

   

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












