# 2. DEFINIÇÃO DE ESTILOS (Para botões legíveis)
style hub_button:
    background Frame(Solid("#2c3e50cc"), 4, 4) 
    padding (20, 15)
    hover_background Solid("#3498db") 
    xminimum 300 

style hub_button_text:
    color "#ffffff"
    hover_color "#f1c40f"
    size 34      
    bold True
    outlines [ (2, "#000000", 0, 0) ]
    xalign 0.5

# 3. TELA DE INTERFACE (Visual do Treino)
screen tela_treinamento(puzzle_atual, opcoes_sorteadas, mostrar_fundo=False):
    zorder 100
    modal True
    
    # Adicione este bloco para controlar o fundo
    if mostrar_fundo:
        add "singlebedroom"

    vbox:
        xalign 0.5 yalign 0.7
        spacing 25

        # Imagem do Tabuleiro
        add puzzle_atual[0] xalign 0.5 zoom 0.6 

        # Pergunta com fundo escuro para leitura
        frame:
            xalign 0.5
            background Solid("#000000aa") 
            padding (25, 10)
            xmaximum 850
            
            text puzzle_atual[1]:
                size 32
                xalign 0.5
                color "#fff"
                text_align 0.5
                outlines [(2, "#000", 0, 0)]

        # Botões de resposta
        hbox:
            xalign 0.5
            spacing 60 
            
            for item in opcoes_sorteadas:
                textbutton item[0]:
                    action Return(item[1])
                    style "hub_button"

# 4. LÓGICA DO JOGO
label hub_treinar:
    $ acertos = 0
    $ total_puzzles = 5
    
    # Sorteia 5 puzzles da lista principal
    $ treino_do_dia = random.sample(lista_de_exercicios, total_puzzles)

    window show
    t "Vou resolver [total_puzzles] problemas para manter a forma."
    window hide

    python:
        for puzzle in treino_do_dia:
            # Prepara e embaralha as opções para não ficarem sempre no mesmo lado
            opcoes = [
                [puzzle[2], True],
                [puzzle[3], False]
            ]
            random.shuffle(opcoes)
            
            # Chama a tela e espera a resposta
            resultado = renpy.call_screen("tela_treinamento", puzzle_atual=puzzle, opcoes_sorteadas=opcoes)
            
            if resultado:
                renpy.say(t, "Boa! Acertei essa.")
                acertos += 1
            else:
                renpy.say(t, "Droga... calculei mal.")

    window show
    t "Treino finalizado. Acertei [acertos] de [total_puzzles] exercícios."
    
    # Atualização de Pontos
    $ pontos_ganhos = acertos * 5
    $ theo_rating += pontos_ganhos
    $ theo_foco -= 20
    
    "Seu Rating subiu em [pontos_ganhos] pontos! Novo Rating: [theo_rating]."
    
    jump abrir_hub

