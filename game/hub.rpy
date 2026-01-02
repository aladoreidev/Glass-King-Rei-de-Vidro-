# ==========================================
# 1. TRANSFORMAÇÃO (MANTENDO SEUS AJUSTES)
# ==========================================
transform prop_style:
    zoom 0.45
    on hover:
        matrixcolor BrightnessMatrix(0.15)
    on idle:
        matrixcolor BrightnessMatrix(0.0)

# ==========================================
# 2. SCREEN DO HUB (SUAS COORDENADAS)
# ==========================================
screen hub_principal():
    tag menu
    add "quartohubvazio"

    # Painel de Status
    frame:
        xalign 0.02 yalign 0.02
        background Solid("#00000088")
        padding (10, 10)
        vbox:
            # text "Rating: [theo_rating]" size 22 color "#f1c40f"
            # text "Foco: [theo_foco]%" size 22 color "#ecf0f1"
            text "Atividades: [acoes_hoje] / 2" size 20 color "#3498db"

    # LIVRO
    imagebutton:
        idle "props/livro.png"
        hover "props/livro hover.png"
        xpos 186 ypos 287 anchor (0.5, 1.0) 
        at prop_style
        focus_mask True
        action Jump("hub_treinar")

    # SMARTPHONE
    imagebutton:
        idle "props/smartphone.png"
        hover "props/smartphone hover.png"
        xpos 711 ypos 489 anchor (0.5, 1.0) 
        at prop_style
        focus_mask True
        action Jump("ver_mensagens")

    # CALENDÁRIO
    imagebutton:
        idle "props/calendario.png"
        hover "props/calendario hover.png"
        xpos 1150 ypos 100 anchor (0.5, 0.0)        
        at prop_style
        focus_mask True
        action Show("tela_torneios")

    # LAPTOP (Zoom 1.4)
    imagebutton:
        idle "props/laptop.png"
        hover "props/laptop hover.png"
        xpos 301 ypos 77 
        at prop_style, Transform(zoom=1.4) 
        focus_mask True
        action Jump("usar_laptop")

    # RETRATOS
    imagebutton:
        idle "props/luisaretrato.png"
        hover "props/luisaretrato hover.png"
        xpos 1200 ypos 456 anchor (0.5, 0.5)
        at prop_style
        focus_mask True
        action Jump("olhar_foto_luisa")

    imagebutton:
        idle "props/mayaretrato.png"
        hover "props/mayaretrato hover.png"
        xpos 1000 ypos 625 anchor (0.5, 0.5)
        at prop_style
        focus_mask True
        action Jump("olhar_foto_maya")

    imagebutton:
        idle "props/leoretrato.png"
        hover "props/leoretrato hover.png"
        xpos 985 ypos 398 anchor (0.5, 0.5)
        at prop_style
        focus_mask True
        action Jump("olhar_foto_leo")

    # TROFÉU / QUADRO (Para ver Stats)
    imagebutton:
        idle "props/trofeu.png"
        hover "props/trofeu hover.png"
        xpos 850 ypos 200 anchor (0.5, 0.5)
        at prop_style, Transform(zoom=1) # Ajuste o zoom se ele estiver grande também
        focus_mask True
        # Certifique-se que o nome aqui seja IGUAL ao da screen lá embaixo
        action Show("tela_stats_detalhada")

    # RELÓGIO (Ajustado para ficar menor)
    imagebutton:
        idle "props/relogio.png"
        hover "props/relogio hover.png"
        
        # Aqui está o segredo: diminuímos o zoom só para este botão
        at prop_style, Transform(zoom=0.7) 
        
        xpos 99 ypos 230 anchor (0.5, 0.5) 
        focus_mask True
        action Jump("confirmar_passar_dia")

# ==========================================
# 3. SUA SCREEN DE CHAT (RESTAURADA)
# ==========================================
screen tela_chat(personagem_nome, personagem_avatar, mensagem_texto):
    modal True
    add Solid("#000000cc") 

    fixed:
        xalign 0.5 yalign 0.5
        xsize 500 ysize 900 

        add "smartphonemockup" xalign 0.5 yalign 0.5

        vbox:
            xalign 0.5
            ypos 0.22 
            xsize 320 
            spacing 20

            hbox:
                spacing 15
                xalign 0.1
                add personagem_avatar zoom 0.8 
                
                vbox:
                    yalign 0.5
                    text "[personagem_nome]" color "#ffffff" size 22 bold True
                    text "online" color "#4df14d" size 14

            frame:
                background Frame(Solid("#2c3e50"), 10, 10) 
                padding (15, 15, 15, 15)
                xsize 300
                xalign 0.5
                
                text "[mensagem_texto]":
                    color "#ffffff"
                    size 20
                    line_spacing 5

            null height 100 

            textbutton "FECHAR":
                action Return()
                xalign 0.5
                ypos 0.85 
                text_size 18














# ==========================================
# 4. LABELS E LÓGICA ALEATÓRIA
# ==========================================
label ver_mensagens:
    python:
        import random
        quem_manda = random.randint(0, 2)
        if quem_manda == 0:
            n_chat, a_chat = "Maya", "mayaicone"
            t_chat = random.choice(respostas_maya)
        elif quem_manda == 1:
            n_chat, a_chat = "Leo", "leoicone"
            t_chat = random.choice(respostas_leo)
        else:
            n_chat, a_chat = "Luísa", "luisaicone"
            t_chat = random.choice(respostas_luisa)

    call screen tela_chat(n_chat, a_chat, t_chat)
    call screen hub_principal

label usar_laptop:
    "Theo" "Vou checar o fórum... nada de interessante hoje."
    call screen hub_principal

label olhar_foto_luisa:
    "Theo" "Minha mãe sempre foi meu porto seguro."
    call screen hub_principal

label olhar_foto_maya:
    "Theo" "Maya... ela é incrível no tabuleiro."
    call screen hub_principal

label olhar_foto_leo:
    "Theo" "Leo é um amigão, mesmo sendo meio doido."
    call screen hub_principal


label confirmar_passar_dia:
    show quartohubvazio
    menu:
        "O dia ainda não acabou. Deseja realmente ir dormir?"
        
        "Sim, ir dormir.":
            scene black with dissolve
            $ acoes_hoje = 0
            $ theo_foco = min(theo_foco + 50, 100)
            pause 1.0
            "Theo descansou e recuperou suas energias."
            
            # SOLUÇÃO: Em vez de jump hub_start, usamos:
            call screen hub_principal 

        "Não, ainda tenho coisas para fazer.":
            call screen hub_principal