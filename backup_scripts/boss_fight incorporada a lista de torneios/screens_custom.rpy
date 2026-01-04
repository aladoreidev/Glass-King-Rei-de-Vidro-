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