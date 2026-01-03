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
    $ persistent.enzo_vencido = True # Nova trava de história
    $ nova_msg_maya = True
    $ nova_msg_leo = True
    # Se a Luisa já foi derrotada, ela também manda mensagem:
    $ nova_msg_luisa = True
    $ acoes_hoje += 1  
    enz "Não é possível... isso não vai ficar assim."
    
    "Você derrotou o mestre da técnica. O silêncio no ginásio é quebrado apenas pelos gritos tímidos dos amigos de Theo!!!."
    
    jump cena_pos_vitoria_enzo

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
    # Verificação de segurança
    if acoes_hoje >= 2:
        jump theo_cansado

    # 1. Configurações Iniciais
    $ theo_hp = theo_max
    $ luisa_hp = luisa_max
    $ round_atual = 0
    $ puzzles_disponiveis = lista_puzzles_luisa[:]
    $ random.shuffle(puzzles_disponiveis)

    scene bibliotecajogo 
    show luisa normal at pos_luisa:
        xalign 1.0 yalign 0.1 zoom 1.9
    show theo normal at pos_theo:
        xalign 0.3 yalign 0.1 zoom 1.9
        
    lu "Você evoluiu, Theo. Mas vamos ver como sua mente lida com a pressão real."
    show screen status_boss_fight

    # 2. Loop de Combate
    while theo_hp > 0 and luisa_hp > 0:
        $ round_atual += 1

        if not puzzles_disponiveis:
            $ puzzles_disponiveis = lista_puzzles_luisa[:]
            $ random.shuffle(puzzles_disponiveis)
        
        $ puzzle = puzzles_disponiveis.pop()
        python:
            opcoes = [[puzzle[2], True], [puzzle[3], False]]
            random.shuffle(opcoes)

        # --- CHAMADA COM TÍTULO PERSONALIZADO ---
        $ resultado = renpy.call_screen("tela_treinamento", 
                                        puzzle_atual=puzzle, 
                                        opcoes_sorteadas=opcoes, 
                                        mostrar_fundo=False, 
                                        titulo_personalizado="DESAFIO DA LUÍSA")

        if resultado:
            python:
                base_dano = 20 + (theo_foco * 0.2) 
                multiplicador = 1.0 + (theo_estabilidade / 100.0)
                dano_final_theo = int((base_dano * multiplicador) + (theo_ousadia * 0.3))
                luisa_hp -= dano_final_theo
                theo_estabilidade = min(theo_estabilidade + 5, 100)
            
            with hpunch
            lu "Um movimento preciso! Você causou [dano_final_theo] de dano."
        else:
            python:
                penalidade_ousadia = int(theo_ousadia * 0.6)
                store.dano_recebido = 15 + penalidade_ousadia
                theo_hp -= store.dano_recebido
                theo_foco = max(theo_foco - 10, 0)
                theo_estabilidade = max(theo_estabilidade - 10, 0)
            
            show flash_vermelho zorder 100 with Dissolve(0.1)
            hide flash_vermelho with Dissolve(0.2)
            with vpunch
            lu "Sua leitura de jogo foi amadora. [dano_recebido] de dano!"

        # Verificação de fim de luta dentro do loop
        if theo_hp <= 0:
            jump derrota_boss
        if luisa_hp <= 0:
            jump vitoria_boss

    jump abrir_hub # Segurança extra caso saia do while de forma inesperada

label vitoria_boss:
    hide screen status_boss_fight
    show luisa raiva 
    lu "Incrível... Xeque-mate. Você me venceu, Theo."
    $ persistent.luisa_vencida = True
    $ theo_rating += 100
    $ theo_ousadia += 15
    $ acoes_hoje += 1 
    "Vitória épica! Rating +100."
    jump abrir_hub

label derrota_boss:
    hide screen status_boss_fight
    "Suas energias se esgotaram..."
    $ acoes_hoje += 1 
    $ theo_rating -= 150
    $ theo_foco = max(0, theo_foco - 20)
    jump abrir_hub