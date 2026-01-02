# 1. DEFINIÇÃO DOS ESTILOS
style hub_button:
    background Frame(Solid("#2c3e50cc"), 4, 4) 
    hover_background Solid("#3498db")          
    insensitive_background Solid("#451a1acc") 
    padding (20, 15)
    xminimum 380 

style hub_button_text:
    color "#ffffff"
    insensitive_color "#888888" 
    size 28 
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

    # Menu de Ações
    vbox:
        xalign 0.5 yalign 0.65
        spacing 12 

        textbutton "🧠 Treinar Xadrez":
            action Jump("preparar_treino")
            style "hub_button"
            sensitive acoes_hoje < 2 and theo_foco >= 20 

        # --- BOTÃO INSERIDO AQUI ---
        textbutton "☕ Convidar Maya para Rolê":
            action Jump("convidar_maya_para_role")
            style "hub_button"
            sensitive acoes_hoje < 2
        # ---------------------------

        textbutton "🏆 Ver Torneios":
            action Show("tela_torneios")
            style "hub_button"
            sensitive acoes_hoje < 2 
        
        # Mensagem para Maya
        textbutton ("📱 " + ("🔴 " if nova_msg_maya else "") + "Mensagem para Maya"):
            action Jump("conversa_maya")
            style "hub_button"

        # Mensagem para Leo
        textbutton ("📱 " + ("🔴 " if nova_msg_leo else "") + "Mensagem para Leo"):
            action Jump("conversa_leo")
            style "hub_button"

        # Mensagem para Luisa
        textbutton ("📱 " + ("🔴 " if nova_msg_luisa else "") + "Mensagem para Luisa"):
            action Jump("conversa_luisa")
            style "hub_button"

        textbutton "💤 Descansar (Próximo Dia)":
            action Jump("proximo_dia")
            style "hub_button"

screen tela_torneios():
    modal True 
    add Solid("#000000cc") 

    frame:
        xalign 0.5 yalign 0.5
        padding (20, 20)
        background Solid("#1c1c1c")
        xsize 600 ysize 550 

        vbox:
            spacing 10
            xfill True
            text "Calendário de Torneios" xalign 0.5 size 30 color "#f1c40f"
            null height 10
            
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                child_size (550, None)

                vbox:
                    spacing 15
                    xalign 0.5
                    
                    for item in lista_torneios:
                        $ nome = item[0]
                        $ rating_req = item[1]
                        $ destino = item[2]
                        
                        # --- VERIFICAÇÃO MANUAL (À prova de falhas) ---
                        $ ja_venceu = False
                        
                        if nome == "Desafio do Enzo" and persistent.enzo_derrotado:
                            $ ja_venceu = True
                        elif nome == "Desafio da Luísa" and persistent.luisa_derrotada:
                            $ ja_venceu = True
                        
                        # Se você tiver mais torneios com cadeado, adicione o 'elif' deles aqui

                        # --- EXIBIÇÃO DO BOTÃO ---
                        if ja_venceu:
                            textbutton "🔒 [nome] (Concluído)":
                                action None
                                xfill True
                                sensitive False 
                        
                        elif theo_rating >= rating_req:
                            textbutton "🏆 [nome] (Req: [rating_req])":
                                action [Hide("tela_torneios"), Jump(destino)]
                                xfill True
                        
                        else:
                            textbutton "🔒 [nome] (Bloqueado: [rating_req])":
                                action None
                                xfill True
                                sensitive False

            null height 20
            textbutton "Fechar":
                action Hide("tela_torneios")
                xalign 0.5
                            




