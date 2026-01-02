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