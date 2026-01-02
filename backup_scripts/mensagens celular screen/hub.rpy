# 1. DEFINIÇÃO DOS ESTILOS
style hub_button:
    background Frame(Solid("#2c3e50cc"), 4, 4) 
    hover_background Solid("#3498db")         
    insensitive_background Solid("#451a1acc") 
    padding (20, 15)
    xminimum 380 # Aumentei um pouco para os emojis não apertarem o texto

style hub_button_text:
    color "#ffffff"
    insensitive_color "#888888" 
    size 28 # Diminuí levemente para caber tudo bem em telas menores
    bold True
    xalign 0.5
    outlines [ (2, "#000000", 0, 0) ]

# 2. DEFINIÇÃO DA SCREEN
screen hub_principal():
    add "mapahub" 

    # Painel de Status
    frame:
        xalign 0.02 yalign 0.02
        background Solid("#00000088")
        padding (10, 10)
        vbox:
            text "Rating: [theo_rating]" size 22 color "#f1c40f"
            text "Foco: [theo_foco]%" size 22 color "#ecf0f1"
            text "Atividades: [acoes_hoje] / 2" size 20 color "#3498db"

    # Menu de Ações (Vinte única e organizada)
    vbox:
        xalign 0.5 yalign 0.65
        spacing 12 

        textbutton "🧠 Treinar Xadrez":
            action Jump("preparar_treino")
            style "hub_button"
            sensitive acoes_hoje < 2 and theo_foco >= 20 

        textbutton "🏆 Ver Torneios":
            action Show("tela_torneios")
            style "hub_button"
            sensitive acoes_hoje < 2 
        
        # Mensagem para Maya
        textbutton ("📱 " + ("🔴 " if nova_msg_maya else "") + "Mensagem para Maya"):
            action Jump("conversa_maya")
            style "hub_button"
            # MANTÉM A TRAVA: Se já fez 2 ações, o botão desativa
            sensitive acoes_hoje < 2

        # Mensagem para Leo
        textbutton ("📱 " + ("🔴 " if nova_msg_leo else "") + "Mensagem para Leo"):
            action Jump("conversa_leo")
            style "hub_button"
            sensitive acoes_hoje < 2

        # Mensagem para Luisa
        textbutton ("📱 " + ("🔴 " if nova_msg_luisa else "") + "Mensagem para Luisa"):
            action Jump("conversa_luisa")
            style "hub_button"
            # Luisa só aparece se já foi derrotada E ainda tem tempo no dia
            sensitive acoes_hoje < 2 and persistent.luisa_derrotada

        textbutton "💤 Descansar (Próximo Dia)":
            action Jump("proximo_dia")
            style "hub_button"

# 3. TELA DE TORNEIOS (Abaixo da principal)
screen tela_torneios():
    modal True 
    add Solid("#000000cc") 

    frame:
        xalign 0.5 yalign 0.5
        padding (20, 20)
        background Solid("#1c1c1c")
        
        vbox:
            spacing 10
            text "Calendário de Torneios" xalign 0.5 size 30 color "#f1c40f"
            null height 10
            
            vpgrid: 
                cols 1
                spacing 5
                draggable True
                mousewheel True
                scrollbars "vertical"
                xsize 500 ysize 400

                for nome, rating_req, destino in lista_torneios:
                    # LÓGICA ESPECIAL PARA O DESAFIO DA LUÍSA (CADEADO PÓS-VITÓRIA)
                    if nome == "Desafio da Luísa" and persistent.luisa_derrotada:
                        textbutton "🔒 [nome] (Concluído)":
                            action None
                            xfill True
                            style "hub_button"
                            sensitive False # Ativa o background avermelhado do seu style

                    # LÓGICA PARA TORNEIOS DISPONÍVEIS (RATING OK)
                    elif theo_rating >= rating_req:
                        textbutton "🏆 [nome] (Req: [rating_req])":
                            action [Hide("tela_torneios"), Jump(destino)]
                            xfill True
                            style "hub_button"
                    
                    # LÓGICA PARA TORNEIOS BLOQUEADOS (RATING BAIXO)
                    else:
                        textbutton "🔒 [nome] (Bloqueado: [rating_req])":
                            action None
                            xfill True
                            style "hub_button"
                            sensitive False

            null height 20
            textbutton "Voltar":
                action Hide("tela_torneios")
                xalign 0.5
                style "hub_button" # Opcional: aplica o estilo ao botão voltar também
