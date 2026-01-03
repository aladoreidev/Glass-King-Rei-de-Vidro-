screen status_personagem():
    frame:
        xalign 0.98 yalign 0.02
        padding (15, 15)
        background Frame(Solid("#00000088"), 4, 4) 
        
        vbox:
            spacing 5
            # Atributos Técnicos
            text "Rating: [theo_rating]" size 20 color "#f1c40f"
            text "Foco: [theo_foco]%" size 18 color "#3498db"
            text "Estabilidade: [theo_estabilidade]%" size 18 color "#9b59b6"
            text "Ousadia: [theo_ousadia]%" size 18 color "#e67e22"
            
            null height 10 # Pequeno espaço entre blocos
            
            # Níveis de Afeto
            text "Afeto Maya: [afeto_maya]" size 16 color "#e91e63"
            text "Amizade Léo: [afeto_leo]" size 16 color "#2ecc71"
            text "Respeito Luisa: [afeto_luisa]" size 16 color "#95a5a6"




# Tela da Boss Figth da Luisa
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



screen tela_stats_detalhada():
    modal True
    add Solid("#000000aa") 
    
    frame:
        xalign 0.5 yalign 0.5
        background Solid("#1c1c1c")
        padding (30, 30)
        xsize 480 # Aumentei um pouco a largura para caber tudo bem folgado
        
        vbox:
            spacing 15
            
            text "Estatísticas do Theo" xalign 0.5 size 30 color "#f1c40f"
            null height 10
            
            # --- ATRIBUTOS PRINCIPAIS ---
            
            hbox:
                xfill True
                text "Rating:" size 22 color "#fff"
                text "[theo_rating]" size 22 color "#3498db" xalign 1.0
                
            hbox:
                xfill True
                text "Foco:" size 22 color "#fff"
                text "[theo_foco]%" size 22 color "#2ecc71" xalign 1.0

            # --- NOVOS ATRIBUTOS ---

            hbox:
                xfill True
                text "Ousadia:" size 22 color "#fff"
                text "[theo_ousadia]%" size 22 color "#e74c3c" xalign 1.0 # Vermelho para ousadia

            hbox:
                xfill True
                text "Estabilidade:" size 22 color "#fff"
                text "[theo_estabilidade]%" size 22 color "#9b59b6" xalign 1.0 # Roxo para estabilidade

            null height 20
            
            textbutton "FECHAR":
                action Hide("tela_stats_detalhada")
                xalign 0.5
                text_size 24
                text_hover_color "#f1c40f"



screen tela_torneios():
    modal True
    add Solid("#000000aa")
    
    frame:
        xalign 0.5 yalign 0.5
        background Solid("#1c1c1c")
        padding (20, 20)
        xsize 750
        ysize 700 # Altura total do quadro
        
        vbox:
            xfill True
            
            text "CALENDÁRIO DE COMPETIÇÕES" xalign 0.5 size 30 color "#f1c40f" bold True
            null height 10
            
            viewport:
                ysize 520 
                scrollbars "vertical"
                mousewheel True
                draggable True
                
                vbox:
                    spacing 10
                    xfill True
                    
                    for item in lista_torneios:
                        $ nome_t = item[0]
                        $ r_req = item[1]
                        $ l_alvo = item[2]
                        $ v_vitoria = item[3]
                        
                        $ vencido = getattr(persistent, v_vitoria, False)
                        $ liberado = theo_rating >= r_req
                        
                        $ cor_bg = "#0e1a26" if vencido else ("#2c3e50" if liberado else "#1a1a1a")

                        frame:
                            background Solid(cor_bg)
                            padding (10, 10)
                            xfill True
                            
                            hbox:
                                spacing 15
                                xfill True 
                                
                                # 1. ÍCONE
                                if vencido:
                                    text "✅" size 22 yalign 0.5
                                elif not liberado:
                                    text "🔒" size 22 yalign 0.5
                                else:
                                    text "🏆" size 22 yalign 0.5 color "#f1c40f"

                                # 2. TEXTOS (Nome e Status)
                                vbox:
                                    yalign 0.5
                                    $ cor_txt = "#7f8c8d" if (vencido or not liberado) else "#fff"
                                    text "[nome_t]" size 20 color cor_txt
                                    
                                    if vencido:
                                        text "Concluído" size 12 color "#3498db"
                                    elif not liberado:
                                        text "Requer [r_req] Rating" size 12 color "#e74c3c"
                                    # --- NOVO: Mensagem visual de cansaço dentro da lista ---
                                    elif acoes_hoje >= 2:
                                        text "Theo está muito cansado hoje" size 12 color "#e67e22"
                                    else:
                                        text "Inscrição Aberta!" size 12 color "#2ecc71"
                                
                                # 3. ESPAÇADOR DINÂMICO
                                null width 10 

                                # 4. BOTÃO (Com a trava sensitive aplicada)
                                if not vencido:
                                    textbutton "INSCREVER":
                                        yalign 0.5
                                        xalign 1.0 
                                        action [Hide("tela_torneios"), Jump(l_alvo)]
                                        # ALTERAÇÃO AQUI: Só ativa se estiver liberado E tiver ações
                                        sensitive (liberado and acoes_hoje < 2)
                                        
                                        text_size 18
                                        background Frame(Solid("#34495e"), 4, 4)
                                        padding (10, 5)
                                else:
                                    text "FINALIZADO" yalign 0.5 xalign 1.0 size 16 italic True color "#3498db"
            
            null height 20
            
            vbox:
                xfill True 
                
                button: 
                    action Hide("tela_torneios")
                    xalign 0.5 
                    background Solid("#34495e") 
                    hover_background Solid("#f1c40f") 
                    padding (20, 10) 
                    
                    text "VOLTAR AO QUARTO":
                        align (0.5, 0.5) 
                        size 22
                        color "#fff"
                        hover_color "#1c1c1c" 
                        bold True

    key "game_menu" action Hide("tela_torneios")



screen tela_chat(personagem_nome, personagem_avatar, mensagem_texto):
    modal True
    add Solid("#000000cc") 

    fixed:
        xalign 0.5 yalign 0.5
        xsize 500 ysize 900 

        add "smartphonemockup" xalign 0.5 yalign 0.5

        # VBOX do Conteúdo (Balão e Topo)
        vbox:
            # xoffset empurra todo o grupo para a direita
            xoffset 40 
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
                text "[mensagem_texto]" color "#ffffff" size 20 line_spacing 5

        # --- BOTÃO FECHAR ---
        textbutton "FECHAR":
            action Return()
            
            # xpos 0.5 + xoffset 20 garante que ele siga o balão
            xpos 0.5 
            xoffset 40
            
            ypos 0.78 
            anchor (0.5, 0.5) 

            background Solid("#2980b9")
            idle_background Solid("#2980b9")
            hover_background Solid("#3498db")
            
            text_color "#ffffff"
            text_size 18
            text_bold True
            padding (40, 12)




# screen tela_treinamento(puzzle_atual, opcoes_sorteadas, **kwargs):
#     zorder 100
#     modal True
    
#     # Se 'mostrar_fundo' for False (como na Boss Fight), ele não adiciona o preto
#     if kwargs.get("mostrar_fundo", True):
#         add Solid("#000000aa")

#     frame:
#         xalign 0.5 yalign 0.5
#         background None 
        
#         vbox:
#             xalign 0.5
#             spacing 15 

#             text "TREINO TÁTICO" xalign 0.5 size 28 color "#f1c40f" bold True

#             frame:
#                 background Solid("#1a1a1a")
#                 padding (5, 5)
#                 xalign 0.5
#                 add puzzle_atual[0] zoom 0.5 

#             frame:
#                 xalign 0.5
#                 background Solid("#000000cc") 
#                 padding (15, 8)
#                 xmaximum 800
                
#                 text puzzle_atual[1]:
#                     size 24
#                     xalign 0.5
#                     color "#fff"
#                     text_align 0.5

#             hbox:
#                 xalign 0.5
#                 spacing 30 
#                 for item in opcoes_sorteadas:
#                     textbutton item[0]:
#                         action Return(item[1])
#                         style "hub_button"



# --- TELA DE TREINAMENTO / BOSS FIGHT ---
screen tela_treinamento(puzzle_atual, opcoes_sorteadas, **kwargs):
    zorder 100
    modal True
    
    # Controle de fundo (Boss Fight não tem fundo preto)
    if kwargs.get("mostrar_fundo", True):
        add Solid("#000000aa")

    frame:
        xalign 0.5 yalign 0.5
        background None 
        
        vbox:
            xalign 0.5
            spacing 15 

            # Título Dinâmico: Usa o que você mandar ou o padrão "TREINO TÁTICO"
            $ titulo_exibido = kwargs.get("titulo_personalizado", "TREINO TÁTICO")
            text "[titulo_exibido]" xalign 0.5 size 28 color "#f1c40f" bold True

            frame:
                background Solid("#1a1a1a")
                padding (5, 5)
                xalign 0.5
                add puzzle_atual[0] zoom 0.5 

            frame:
                xalign 0.5
                background Solid("#000000cc") 
                padding (15, 8)
                xmaximum 800
                
                text puzzle_atual[1]:
                    size 24
                    xalign 0.5
                    color "#fff"
                    text_align 0.5

            hbox:
                xalign 0.5
                spacing 30 
                for item in opcoes_sorteadas:
                    textbutton item[0]:
                        action Return(item[1])
                        style "hub_button"