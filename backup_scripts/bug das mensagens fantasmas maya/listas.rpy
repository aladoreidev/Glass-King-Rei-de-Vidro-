init python:
    import random

    #Respostas das Mensagens Enviadas pelos amigos
    respostas_maya = [
        "Oi Theo! Tô no meio de umas táticas aqui, falamos depois? ♟️",
        "Viu aquela partida do Magnus? Te mando o link mais tarde!",
        "Tô estudando a Defesa Caro-Kann, não consigo falar agora.",
        "A tática de hoje estava impossível! Quase quebrei a cabeça. 🤯",
        "Você viu a nova linha que o pessoal tá usando na Siciliana? Doidera!",
        "Tô revisando minhas partidas do último torneio... Errei coisas bobas.",
        "Ei! Se vir o Leo, diz pra ele que ele ainda me deve uma revanche!",
        "Acabei de achar um puzzle de mate em 5 que é a sua cara. Vou te mandar.",
        "Theo! Tirei 10 na prova de Filosofia! O professor até elogiou meu ensaio. ✨",
        "Você ouviu o boato de que a Letícia está saindo com o capitão do time de basquete?",
        "Minha playlist de lofi hoje tá batendo certinho com o clima de chuva.",
        "Não aguento mais estudar Biologia... Por que eu preciso saber o que é uma mitocôndria?",
        "Tô pensando em mudar a cor do meu cabelo, o que você acha de um azul escuro?",
        "Vi você passando no corredor hoje, parecia que estava em outro planeta! kkkk",
        "O café da cantina hoje está parecendo água suja, não compre!"
    ]
    
    respostas_leo = [
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

    respostas_luisa = [
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
         
        ("Desafio do Enzo", 0, "boss_fight_enzo"),
        ("Desafio da Luísa", 1000, "boss_fight_luisa"),
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
    
    # Listas dos Puzzles do Desafio da Luiza
    lista_puzzles_luisa = [
        ("puzzle001", "Qual golpe Tático temos aqui?", "Ataque Duplo", "Cravada"),
        ("puzzle002", "Qual xeque mais eficiente", "Cf6+", "Cg5+"),
        ("puzzle003", "Qual Peão eu devo avançar?", "Peão g", "Peão h"),
        ("puzzle004", "O tabuleiro está montado corretamente?", "Não", "Sim"),
        ("puzzle005", "Em quantos lances as pretas dão mate", "3", "2")
    ]
