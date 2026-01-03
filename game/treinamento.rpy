# ==============================================================================
# ESTILOS E TELAS (Mantidos conforme sua última versão compacta)
# ==============================================================================
style hub_button:
    background Frame(Solid("#2c3e50cc"), 4, 4) 
    hover_background Solid("#3498db") 
    padding (10, 5)
    xsize 350 
    ysize 70   
    
style hub_button_text:
    color "#ffffff"
    hover_color "#f1c40f"
    size 22    
    bold True
    xalign 0.5
    yalign 0.5
    text_align 0.5



# ==============================================================================
# LÓGICA DO TREINO (Com a trava de 2 atividades)
# ==============================================================================
label hub_treinar:
    # --- NOVO: Verificação de limite de atividades (2 por dia) ---
    if acoes_hoje >= 2:
        window show
        t "Já fiz muita coisa por hoje. Minha mente está exausta para cálculos pesados. Melhor descansar um pouco (Dormir)."
        window hide
        jump abrir_hub

    # 1. Verificação de Foco
    if theo_foco < 20:
        window show
        t "Estou exausto... Minha cabeça não consegue calcular nem um xeque-pastor agora. Preciso descansar."
        window hide
        jump abrir_hub

    # 2. Preparação do Cenário
    scene singlebedroom with fade
    $ acertos = 0
    $ total_puzzles = 5
    
    $ treino_do_dia = random.sample(lista_de_exercicios, total_puzzles)
    $ indice_treino = 0

    window show
    t "Vou resolver [total_puzzles] problemas para manter a forma."
    window hide 

    # 3. Loop de Exercícios
    while indice_treino < total_puzzles:
        $ puzzle = treino_do_dia[indice_treino]
        $ opcoes = [[puzzle[2], True], [puzzle[3], False]]
        $ random.shuffle(opcoes)
        
        call screen tela_treinamento(puzzle_atual=puzzle, opcoes_sorteadas=opcoes)
        $ resultado_obtido = _return

        if resultado_obtido:
            $ acertos += 1
            t "Boa! Acertei essa."
        else:
            t "Droga... calculei mal essa variante."
            
        $ indice_treino += 1

    # 4. Finalização e Recompensas
    scene singlebedroom with fade
    window show
    t "Treino finalizado. Acertei [acertos] de [total_puzzles] exercícios."
    
    $ pontos_ganhos = acertos * 5
    $ theo_rating += pontos_ganhos
    $ theo_foco -= 20
    
    # --- AQUI É ONDE ELE SOMA A ATIVIDADE ---
    $ acoes_hoje += 1
    
    "Seu Rating subiu em [pontos_ganhos] pontos! Novo Rating: [theo_rating]."
    "Foco consumido: -20. Foco atual: [theo_foco]."
    "Atividades pesadas realizadas hoje: [acoes_hoje]/2."
    
    window hide 
    jump abrir_hub
