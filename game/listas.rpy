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
    
    # Listas dos Puzzles do Desafio da Luiza
    lista_puzzles_luisa = [
        ("puzzle001", "Qual golpe Tático temos aqui?", "Ataque Duplo", "Cravada"),
        ("puzzle002", "Qual xeque mais eficiente", "Cf6+", "Cg5+"),
        ("puzzle003", "Qual Peão eu devo avançar?", "Peão g", "Peão h"),
        ("puzzle004", "O tabuleiro está montado corretamente?", "Não", "Sim"),
        ("puzzle005", "Em quantos lances as pretas dão mate", "3", "2")
    ]



init python:

    # 1. LISTA DE PUZZLES (Estrutura: Imagem, Pergunta, Correta, Errada)
    lista_de_exercicios = [
        ("puzzle01", "Pretas jogam: Qual o melhor lance?", "Cf3+", "Cd3+"),
        ("puzzle02", "Brancas jogam: Qual o tema tático?", "Descoberto", "Cravada"),
        ("puzzle03", "Brancas jogam: Mate em quantas jogadas?", "3", "2"),
        ("puzzle04", "Qual a melhor forma de salvar a Torre?", "Roque Grande", "Roque Curto"),
        ("puzzle05", "Brancas jogam, qual resultado:", "Vitória", "Empate")
    ]




init python:
    import random

    # "Pergunta": ["Opção A", "Opção B", "Opção C", Índice_Resposta_Correta]
    puzzles_xadrez = {
        "Qual peça pode saltar sobre outras peças?": ["Torre", "Rainha", "Cavalo", 2],
        "Como se chama o xeque-mate dado apenas por um Cavalo contra o Rei sufocado por suas próprias peças?": ["Mate de Pastor", "Mate Sufocado", "Mate de Anastácia", 1],
        "Qual a pontuação atribuída a um Bispo?": ["3 pontos", "5 pontos", "1 ponto", 0],
        "O que é o 'Roque'?": ["Um movimento do Rei e da Torre", "Uma captura de Peão", "Uma promoção de Dama", 0],
        "Quem foi o primeiro Campeão Mundial oficial de xadrez?": ["Wilhelm Steinitz", "Paul Morphy", "Emmanuel Lasker", 0],
        "Qual abertura é caracterizada pelos lances 1. e4 c5?": ["Defesa Francesa", "Defesa Siciliana", "Defesa Caro-Kann", 1],
        "Qual é a casa de cor correta que deve estar à direita de cada jogador?": ["Casa preta", "Casa branca", "Qualquer uma", 1],
        "O que significa o termo 'Gambito'?": ["Um empate forçado", "Sacrifício de material por vantagem", "Um xeque duplo", 1],
        "Quantas casas um Rei pode se mover por vez (exceto no roque)?": ["Duas", "Uma", "Quantas quiser", 1],
        "Qual peça é a mais valiosa do jogo depois do Rei?": ["Torre", "Bispo", "Dama", 2],
        "Em qual Defesa o jogador usa 1. e4 c6?": ["Defesa Eslava", "Defesa Caro-Kann", "Defesa Escandinava", 1],
        "Quem é o atual prodígio norueguês e ex-campeão mundial?": ["Hikaru Nakamura", "Magnus Carlsen", "Fabiano Caruana", 1],
        "O que é 'Stalemate' (Afogamento)?": ["Vitória das brancas", "Vitória das pretas", "Empate", 2],
        "Qual peça se move em diagonais?": ["Torre", "Bispo", "Rei", 1],
        "Como se chama o mate mais rápido possível no xadrez?": ["Mate do Louco", "Mate do Pastor", "Mate de Legal", 0],
        "No início do jogo, onde ficam os Cavalos?": ["Ao lado das Torres", "Ao lado do Rei e Dama", "Nas pontas", 0],
        "Qual destas peças NÃO pode ser promovida?": ["Peão", "Torre", "Rei", 2],
        "Qual é o objetivo final do xadrez?": ["Capturar todas as peças", "Xeque-mate no Rei", "Chegar ao outro lado", 1],
        "O que acontece se um Rei ficar em xeque e não tiver saída?": ["O jogo continua", "É xeque-mate", "É empate", 1],
        "Quantas colunas tem um tabuleiro de xadrez?": ["8", "10", "64", 0],
        "O Rei pode se mover para uma casa sob ataque?": ["Sim", "Não", "Apenas se capturar", 1],
        "Qual é a melhor resposta para um ataque descoberto?": ["Ignorar", "Mover a peça atacada ou bloquear", "Promover um peão", 1],
        "O que é o 'Centro' no xadrez?": ["As casas e4, e5, d4, d5", "As bordas do tabuleiro", "As casas das Torres", 0],
        "A Defesa Francesa começa com quais lances?": ["1. e4 e5", "1. e4 e6", "1. d4 d5", 1],
        "O que é um 'Peão Passado'?": ["Um peão que foi capturado", "Um peão sem peões adversários para bloqueá-lo", "Um peão promovido", 1],
        "Qual cor sempre começa a partida?": ["Pretas", "Brancas", "Sorteio", 1],
        "Qual o valor de um Peão?": ["1 ponto", "3 pontos", "0 pontos", 0],
        "O que é o 'Relógio de Xadrez'?": ["Um cronômetro de cozinha", "Um dispositivo para controlar o tempo dos jogadores", "Um enfeite", 1],
        "O termo 'Fianchetto' refere-se a qual peça?": ["Cavalo", "Bispo", "Torre", 1],
        "Quantas peças cada jogador tem no início da partida?": ["12", "16", "32", 1],
        "Qual peça é a única que não pode recuar?": ["Peão", "Bispo", "Torre", 0],
        "Quantas rainhas cada jogador pode ter no máximo por meio da promoção?": ["1", "8", "9", 2],
        "Em qual casa o Rei Preto sempre começa o jogo?": ["e8", "d8", "e1", 0],
        "O movimento 'En Passant' só pode ser feito por qual peça?": ["Cavalo", "Peão", "Torre", 1],
        "Qual é o nome da situação onde qualquer lance que o jogador faça piora sua posição?": ["Fianchetto", "Zugzwang", "Gambito", 1],
        "O que acontece se a mesma posição ocorrer três vezes no tabuleiro?": ["Vitória das brancas", "Empate", "Derrota das pretas", 1],
        "Como se chama a abertura que começa com 1. e4 e5 2. f4?": ["Gambito do Rei", "Gambito da Dama", "Abertura Espanhola", 0],
        "Qual mestre mundial era conhecido como 'O Ogro de Baku'?": ["Magnus Carlsen", "Garry Kasparov", "Bobby Fischer", 1],
        "Qual o valor aproximado de pontos de uma Torre?": ["3 pontos", "5 pontos", "9 pontos", 1],
        "Qual o tempo médio de uma partida de xadrez 'Blitz'?": ["Entre 3 a 5 minutos", "60 minutos", "10 segundos", 0]
    }

    def sortear_puzzle():
        pergunta = random.choice(list(puzzles_xadrez.keys()))
        return pergunta, puzzles_xadrez[pergunta]



# No arquivo listas.rpy (fora de qualquer bloco python)
    
# Lista mestra de torneios
# Formato: ("Nome", Rating Necessário, "Label de Destino", "Nome da Variável de Vitória")
default lista_torneios = [
    ("Desafio do Enzo", 0, "boss_fight_enzo", "enzo_vencido"),
    ("Desafio da Luísa", 1000, "boss_fight_luisa", "luisa_vencida"),
    ("Copa Local", 1200, "copa_local", "copa_local_vencida"),
    ("Regional Amador", 1400, "regional_amador", "regional_vencido"),
    ("Aberto da Cidade", 1600, "aberto_cidade", "aberto_cidade_vencido"),
    ("Estadual Sub-20", 1800, "estadual_sub20", "estadual_vencido"),
    ("Memorial dos Mestres", 2000, "memorial_mestres", "memorial_vencido"),
    ("Campeonato Nacional", 2200, "nacional", "nacional_vencido"),
    ("Seletiva Internacional", 2400, "seletiva_inter", "seletiva_vencido"),
    ("Torneio dos Candidatos", 2600, "candidatos", "candidatos_vencido"),
    ("Campeonato Mundial", 2800, "mundial", "mundial_vencido")
]



