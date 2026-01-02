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



screen tela_chat(personagem_nome, personagem_avatar, mensagem_texto):
    modal True
    add Solid("#000000cc") # Escurece o fundo do jogo

    # Container principal que centraliza o celular na tela
    fixed:
        xalign 0.5 yalign 0.5
        xsize 500 ysize 900 # Tamanho aproximado da imagem do celular

        # 1. A Imagem do Smartphone
        add "smartphonemockup" xalign 0.5 yalign 0.5

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
        padding (30, 30)
        xsize 750
        ysize 650
        
        vbox:
            spacing 15
            text "CALENDÁRIO DE COMPETIÇÕES" xalign 0.5 size 32 color "#f1c40f" bold True
            null height 10
            
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                
                vbox:
                    spacing 12
                    xfill True
                    
                    for item in lista_torneios:
                        # Extração segura dos dados da sua lista
                        $ nome_t = item[0]
                        $ r_req = item[1]
                        $ l_alvo = item[2]
                        $ v_vitoria = item[3]
                        
                        # Verificação de status usando o persistent que você definiu
                        $ vencido = getattr(persistent, v_vitoria, False)
                        $ liberado = theo_rating >= r_req
                        
                        # Escolha da cor do fundo
                        $ cor_bg = "#1a1a1a" # Bloqueado
                        if vencido:
                            $ cor_bg = "#0e1a26"
                        elif liberado:
                            $ cor_bg = "#2c3e50"

                        frame:
                            background Solid(cor_bg)
                            padding (15, 10)
                            xfill True
                            
                            hbox:
                                spacing 20
                                xfill True
                                
                                # Ícone
                                if vencido:
                                    text "✅" size 25 yalign 0.5
                                elif not liberado:
                                    text "🔒" size 25 yalign 0.5
                                else:
                                    text "🏆" size 25 yalign 0.5 color "#f1c40f"

                                vbox:
                                    text "[nome_t]" size 22 color ("#7f8c8d" if (vencido or not liberado) else "#fff")
                                    
                                    if vencido:
                                        text "Torneio Concluído" size 14 color "#3498db"
                                    elif not liberado:
                                        text "Requer [r_req] Rating" size 14 color "#e74c3c"
                                    else:
                                        text "Inscrição Aberta!" size 14 color "#2ecc71"
                                
                                # Botão de ação
                                if not vencido:
                                    textbutton "INSCREVER":
                                        yalign 0.5
                                        xalign 1.0
                                        action [Hide("tela_torneios"), Jump(l_alvo)]
                                        sensitive liberado
                                else:
                                    text "FINALIZADO" yalign 0.5 xalign 1.0 size 18 italic True color "#3498db"
            
            null height 20
            textbutton "FECHAR":
                action Hide("tela_torneios")
                xalign 0.5
                text_hover_color "#f1c40f"

            